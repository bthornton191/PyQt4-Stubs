import argparse

from bs4 import BeautifulSoup
from collections import OrderedDict


def parse_enumerations(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    enumerations = OrderedDict()

    for enumeration_header in soup.find_all("h3"):
        if len(enumeration_header.contents) < 2:
            print "Ignoring tag without enough sub elements: " + str(enumeration_header.contents)
            continue
        elif not enumeration_header.contents[1]:
            print "Ignoring tag with empty second sub element: " + str(enumeration_header.contents)
            continue
        elif not enumeration_header.contents[1].string.lower() == "enum qt::":
            print "Ignoring non enum tag: " + str(enumeration_header.contents)
            continue

        enumeration_name = enumeration_header.span.string
        enumeration_description = ""

        if enumeration_name not in enumerations:
            enumerations[enumeration_name] = OrderedDict()

        for tag in enumeration_header.next_siblings:
            if tag.name == "h3":
                break
            elif tag.name == "p" and tag.string:
                enumeration_description += tag.string + "\n"
            elif tag.name == "div" and "table" in tag["class"]:
                enumerations[enumeration_name]["docstring"] = enumeration_description

                for table_row in tag.find_all("tr")[1:]:
                    columns = table_row.find_all("td")
                    name = columns[0].string
                    value = columns[1].string

                    if len(columns) >= 3:
                        description = columns[2].string
                    else:
                        description = ""

                    if not name:
                        continue

                    name = name.replace("Qt::", "")

                    if not value:
                        continue

                    value = value.replace("Qt::", "")

                    if not description:
                        description = ""

                    if value.strip() == "?":
                        value = '"?"'

                    enumerations[enumeration_name][name] = (value, description)

    return enumerations


def write_enumerations(enumerations, output_filepath):
    with open(output_filepath, "w") as output_file:
        output_file.write("""
class QtEnumeration(object):
    def __init__(self, value):
        self.value = value

    def __or__(self, other):
        return self.value | other.value


""")

        for enumeration_name, enumeration_values in enumerations.iteritems():
            output_file.write("""
class {0}(QtEnumeration):
    ""\" {1}
    ""\"
    ...


""".format(enumeration_name, enumeration_values.pop("docstring")))

            for enumeration_key, enumeration_value_tuple in enumeration_values.iteritems():
                enumeration_value, enumeration_description = enumeration_value_tuple
                if enumeration_value not in enumeration_values:
                    output_file.write(u"""
{0} = {1}({2})
""\" {3}
""\"
""".format(enumeration_key, enumeration_name, enumeration_value, enumeration_description).lstrip().encode("utf-8"))
                else:
                    output_file.write(u"""
{0} = {1}
""\" {2}
""\"
""".format(enumeration_key, enumeration_value, enumeration_description).lstrip().encode("utf-8"))

            if enumeration_values:
                output_file.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Qt documentation enumeration scrubber.")
    parser.add_argument("html_filepath")
    parser.add_argument("output_filepath")
    args = parser.parse_args()
    html_filepath = args.html_filepath

    with open(html_filepath, "rb") as html_file:
        file_data = html_file.read()

    write_enumerations(parse_enumerations(file_data), args.output_filepath)
