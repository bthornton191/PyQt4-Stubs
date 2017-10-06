import argparse

from bs4 import BeautifulSoup


def parse_class_definition(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    functions = []
    class_name = soup.find_all("h1", class_="title")[-1].string.replace(" Class", "")
    properties_element = soup.find_all("div", class_="prop")[-1]
    functions_element = soup.find_all("div", class_="func")[-1]
    property_headers = properties_element.find_all("h3")
    function_headers = functions_element.find_all("h3")

    for property_header in property_headers:
        name_span = property_header.find_all("span", class_="name")[-1]
        type_span = property_header.find_all("span", class_="type")[-1]
        property_name = name_span.string
        property_type = type_span.string
        property_description = ""

        for tag in property_header.next_siblings:
            if tag.name == "h3":
                functions.append({
                    "name": property_name,
                    "type": property_type,
                    "description": property_description,
                    "parameters": [],
                })
                functions.append({
                    "name": "set{0}".format(property_name[0].upper() + property_name[1:]),
                    "type": "None",
                    "description": property_description,
                    "parameters": ["({0}: {1})".format(property_name.lower(), property_type),]
                })
                break
            elif tag.name == "p" and tag.string:
                property_description += tag.string + "\n"
            else:
                continue

    for function_header in function_headers:
        name_span = function_header.find_all("span", class_="name")
        function_name = name_span.string
        parameter_type_spans = function_header.find_all("span", class_="type")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A Qt documentation class scrubber.")
    parser.add_argument("html_filepath")
    parser.add_argument("output_filepath")
    args = parser.parse_args()
    html_filepath = args.html_filepath

    with open(html_filepath, "rb") as html_file:
        file_data = html_file.read()

    parse_class_definition(file_data)
