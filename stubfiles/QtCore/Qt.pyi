
class QtEnumeration(object):
    def __init__(self, value):
        self.value = value

    def __or__(self, other):
        return self.value | other.value



class AlignmentFlag(QtEnumeration):
    """ This enum type is used to describe alignment. It contains horizontal and vertical flags that can be combined to produce the required effect.
The horizontal flags are:
The vertical flags are:
You can use only one of the horizontal flags at a time. There is one two-dimensional flag:
You can use at most one horizontal and one vertical flag at a time. Qt.AlignCenter counts as both horizontal and vertical.
Three enum values are useful in applications that can be run in right-to-left mode:
Masks:

    """
    ...


AlignLeft = AlignmentFlag(0x0001)
""" Aligns with the left edge.
"""
AlignRight = AlignmentFlag(0x0002)
""" Aligns with the right edge.
"""
AlignHCenter = AlignmentFlag(0x0004)
""" Centers horizontally in the available space.
"""
AlignJustify = AlignmentFlag(0x0008)
""" Justifies the text in the available space.
"""
AlignTop = AlignmentFlag(0x0020)
""" Aligns with the top.
"""
AlignBottom = AlignmentFlag(0x0040)
""" Aligns with the bottom.
"""
AlignVCenter = AlignmentFlag(0x0080)
""" Centers vertically in the available space.
"""
AlignCenter = AlignmentFlag(AlignVCenter | AlignHCenter)
""" Centers in both dimensions.
"""
AlignAbsolute = AlignmentFlag(0x0010)
""" 
"""
AlignLeading = AlignLeft
""" Synonym for Qt.AlignLeft.
"""
AlignTrailing = AlignRight
""" Synonym for Qt.AlignRight.
"""
AlignHorizontal_Mask = AlignmentFlag(AlignLeft | AlignRight | AlignHCenter | AlignJustify | AlignAbsolute)
""" 
"""
AlignVertical_Mask = AlignmentFlag(AlignTop | AlignBottom | AlignVCenter)
""" 
"""


class AnchorAttribute(QtEnumeration):
    """ An anchor has one or more of the following attributes:

    """
    ...


AnchorName = AnchorAttribute(0)
""" the name attribute of the anchor. This attribute is used when scrolling to an anchor in the document.
"""
AnchorHref = AnchorAttribute(1)
""" the href attribute of the anchor. This attribute is used when a link is clicked to determine what content to load.
"""


class AnchorPoint(QtEnumeration):
    """
    """
    ...


AnchorLeft = AnchorPoint(0)
""" The left side of a layout item.
"""
AnchorHorizontalCenter = AnchorPoint(1)
""" A "virtual" side that is centered between the left and the right side of a layout item.
"""
AnchorRight = AnchorPoint(2)
""" The right side of a layout item.
"""
AnchorTop = AnchorPoint(3)
""" The top side of a layout item.
"""
AnchorVerticalCenter = AnchorPoint(4)
""" A "virtual" side that is centered between the top and the bottom side of a layout item.
"""
AnchorBottom = AnchorPoint(5)
""" The bottom side of a layout item.
"""


class ApplicationAttribute(QtEnumeration):
    """
    """
    ...


AA_ImmediateWidgetCreation = ApplicationAttribute(0)
""" Ensures that widgets are created as soon as they are constructed. By default, resources for widgets are allocated on demand to improve efficiency and minimize resource usage. Setting or clearing this attribute affects widgets constructed after the change. Setting it tells Qt to create toplevel windows immediately. Therefore, if it is important to minimize resource consumption, do not set this attribute.
"""
AA_MSWindowsUseDirect3DByDefault = ApplicationAttribute(1)
""" This value is obsolete and has no effect.
"""
AA_DontShowIconsInMenus = ApplicationAttribute(2)
""" 
"""
AA_NativeWindows = ApplicationAttribute(3)
""" Ensures that widgets have native windows.
"""
AA_DontCreateNativeWidgetSiblings = ApplicationAttribute(4)
""" 
"""
AA_MacPluginApplication = ApplicationAttribute(5)
""" Stops the Qt mac application from doing specific initializations that do not necessarily make sense when using Qt to author a plugin. This includes avoiding loading our nib for the main menu and not taking possession of the native menu bar. When setting this attribute to true will also set the AA_DontUseNativeMenuBar attribute to true.
"""
AA_DontUseNativeMenuBar = ApplicationAttribute(6)
""" All menubars created while this attribute is set to true won't be used as a native menubar (e.g, the menubar at the top of the main screen on Mac OS X or at the bottom in Windows CE).
"""
AA_MacDontSwapCtrlAndMeta = ApplicationAttribute(7)
""" 
"""
AA_S60DontConstructApplicationPanes = ApplicationAttribute(8)
""" 
"""
AA_S60DisablePartialScreenInputMode = ApplicationAttribute(9)
""" 
"""
AA_X11InitThreads = ApplicationAttribute(10)
""" 
"""
AA_CaptureMultimediaKeys = ApplicationAttribute(11)
""" 
"""


class ArrowType(QtEnumeration):
    """
    """
    ...


NoArrow = ArrowType(0)
""" 
"""
UpArrow = ArrowType(1)
""" 
"""
DownArrow = ArrowType(2)
""" 
"""
LeftArrow = ArrowType(3)
""" 
"""
RightArrow = ArrowType(4)
""" 
"""


class AspectRatioMode(QtEnumeration):
    """ This enum type defines what happens to the aspect ratio when scaling an rectangle.

    """
    ...


IgnoreAspectRatio = AspectRatioMode(0)
""" The size is scaled freely. The aspect ratio is not preserved.
"""
KeepAspectRatio = AspectRatioMode(1)
""" The size is scaled to a rectangle as large as possible inside a given rectangle, preserving the aspect ratio.
"""
KeepAspectRatioByExpanding = AspectRatioMode(2)
""" The size is scaled to a rectangle as small as possible outside a given rectangle, preserving the aspect ratio.
"""


class Axis(QtEnumeration):
    """ This enum type defines three values to represent the three axes in the cartesian coordinate system.

    """
    ...


XAxis = Axis(0)
""" The X axis.
"""
YAxis = Axis(1)
""" The Y axis.
"""
ZAxis = Axis(2)
""" The Z axis.
"""


class BGMode(QtEnumeration):
    """ Background mode:

    """
    ...


TransparentMode = BGMode(0)
""" 
"""
OpaqueMode = BGMode(1)
""" 
"""


class BrushStyle(QtEnumeration):
    """
    """
    ...


NoBrush = BrushStyle(0)
""" No brush pattern.
"""
SolidPattern = BrushStyle(1)
""" Uniform color.
"""
Dense1Pattern = BrushStyle(2)
""" Extremely dense brush pattern.
"""
Dense2Pattern = BrushStyle(3)
""" Very dense brush pattern.
"""
Dense3Pattern = BrushStyle(4)
""" Somewhat dense brush pattern.
"""
Dense4Pattern = BrushStyle(5)
""" Half dense brush pattern.
"""
Dense5Pattern = BrushStyle(6)
""" Somewhat sparse brush pattern.
"""
Dense6Pattern = BrushStyle(7)
""" Very sparse brush pattern.
"""
Dense7Pattern = BrushStyle(8)
""" Extremely sparse brush pattern.
"""
HorPattern = BrushStyle(9)
""" Horizontal lines.
"""
VerPattern = BrushStyle(10)
""" Vertical lines.
"""
CrossPattern = BrushStyle(11)
""" Crossing horizontal and vertical lines.
"""
BDiagPattern = BrushStyle(12)
""" Backward diagonal lines.
"""
FDiagPattern = BrushStyle(13)
""" Forward diagonal lines.
"""
DiagCrossPattern = BrushStyle(14)
""" Crossing diagonal lines.
"""
LinearGradientPattern = BrushStyle(15)
""" 
"""
ConicalGradientPattern = BrushStyle(17)
""" 
"""
RadialGradientPattern = BrushStyle(16)
""" 
"""
TexturePattern = BrushStyle(24)
""" 
"""


class CaseSensitivity(QtEnumeration):
    """
    """
    ...


CaseInsensitive = CaseSensitivity(0)
""" 
"""
CaseSensitive = CaseSensitivity(1)
""" 
"""


class CheckState(QtEnumeration):
    """ This enum describes the state of checkable items, controls, and widgets.

    """
    ...


Unchecked = CheckState(0)
""" The item is unchecked.
"""
PartiallyChecked = CheckState(1)
""" The item is partially checked. Items in hierarchical models may be partially checked if some, but not all, of their children are checked.
"""
Checked = CheckState(2)
""" The item is checked.
"""


class ClipOperation(QtEnumeration):
    """
    """
    ...


NoClip = ClipOperation(0)
""" This operation turns clipping off.
"""
ReplaceClip = ClipOperation(1)
""" Replaces the current clip path/rect/region with the one supplied in the function call.
"""
IntersectClip = ClipOperation(2)
""" Intersects the current clip path/rect/region with the one supplied in the function call.
"""
UniteClip = ClipOperation(3)
""" Unites the current clip path/rect/region with the one supplied in the function call.
"""


class ConnectionType(QtEnumeration):
    """ This enum describes the types of connection that can be used between signals and slots. In particular, it determines whether a particular signal is delivered to a slot immediately or queued for delivery at a later time.

    """
    ...


AutoConnection = ConnectionType(0)
""" (default) If the signal is emitted from a different thread than the receiving object, the signal is queued, behaving as Qt.QueuedConnection. Otherwise, the slot is invoked directly, behaving as Qt.DirectConnection. The type of connection is determined when the signal is emitted.
"""
DirectConnection = ConnectionType(1)
""" The slot is invoked immediately, when the signal is emitted.
"""
QueuedConnection = ConnectionType(2)
""" The slot is invoked when control returns to the event loop of the receiver's thread. The slot is executed in the receiver's thread.
"""
BlockingQueuedConnection = ConnectionType(4)
""" Same as QueuedConnection, except the current thread blocks until the slot returns. This connection type should only be used where the emitter and receiver are in different threads.
"""
UniqueConnection = ConnectionType(0x80)
""" Same as AutoConnection, but the connection is made only if it does not duplicate an existing connection. i.e., if the same signal is already connected to the same slot for the same pair of objects, then the connection will fail. This connection type was introduced in Qt 4.6.
"""
AutoCompatConnection = ConnectionType(3)
""" 
"""


class ContextMenuPolicy(QtEnumeration):
    """ This enum type defines the various policies a widget can have with respect to showing a context menu.

    """
    ...


NoContextMenu = ContextMenuPolicy(0)
""" the widget does not feature a context menu, context menu handling is deferred to the widget's parent.
"""
PreventContextMenu = ContextMenuPolicy(4)
""" 
"""
DefaultContextMenu = ContextMenuPolicy(1)
""" 
"""
ActionsContextMenu = ContextMenuPolicy(2)
""" 
"""
CustomContextMenu = ContextMenuPolicy(3)
""" 
"""


class CoordinateSystem(QtEnumeration):
    """ This enum specifies the coordinate system.

    """
    ...


DeviceCoordinates = CoordinateSystem(0)
""" Coordinates are relative to the upper-left corner of the object's paint device.
"""
LogicalCoordinates = CoordinateSystem(1)
""" Coordinates are relative to the upper-left corner of the object.
"""


class Corner(QtEnumeration):
    """ This enum type specifies a corner in a rectangle:

    """
    ...


TopLeftCorner = Corner(0x00000)
""" The top-left corner of the rectangle.
"""
TopRightCorner = Corner(0x00001)
""" The top-right corner of the rectangle.
"""
BottomLeftCorner = Corner(0x00002)
""" The bottom-left corner of the rectangle.
"""
BottomRightCorner = Corner(0x00003)
""" The bottom-right corner of the rectangle.
"""


class CursorMoveStyle(QtEnumeration):
    """ This enum describes the movement style available to text cursors. The options are:

    """
    ...


LogicalMoveStyle = CursorMoveStyle(0)
""" Within a left-to-right text block, decrease cursor position when pressing left arrow key, increase cursor position when pressing the right arrow key. If the text block is right-to-left, the opposite behavior applies.
"""
VisualMoveStyle = CursorMoveStyle(1)
""" Pressing the left arrow key will always cause the cursor to move left, regardless of the text's writing direction. Pressing the right arrow key will always cause the cursor to move right.
"""


class CursorShape(QtEnumeration):
    """ This enum type defines the various cursors that can be used.
The standard arrow cursor is the default for widgets in a normal state.

    """
    ...


ArrowCursor = CursorShape(0)
""" 
"""
UpArrowCursor = CursorShape(1)
""" 
"""
CrossCursor = CursorShape(2)
""" 
"""
WaitCursor = CursorShape(3)
""" 
"""
IBeamCursor = CursorShape(4)
""" 
"""
SizeVerCursor = CursorShape(5)
""" 
"""
SizeHorCursor = CursorShape(6)
""" 
"""
SizeBDiagCursor = CursorShape(7)
""" 
"""
SizeFDiagCursor = CursorShape(8)
""" 
"""
SizeAllCursor = CursorShape(9)
""" 
"""
BlankCursor = CursorShape(10)
""" A blank/invisible cursor, typically used when the cursor shape needs to be hidden.
"""
SplitVCursor = CursorShape(11)
""" 
"""
SplitHCursor = CursorShape(12)
""" 
"""
PointingHandCursor = CursorShape(13)
""" 
"""
ForbiddenCursor = CursorShape(14)
""" 
"""
OpenHandCursor = CursorShape(17)
""" 
"""
ClosedHandCursor = CursorShape(18)
""" 
"""
WhatsThisCursor = CursorShape(15)
""" 
"""
BusyCursor = CursorShape(16)
""" 
"""
DragMoveCursor = CursorShape(20)
""" A cursor that is usually used when dragging an item.
"""
DragCopyCursor = CursorShape(19)
""" A cursor that is usually used when dragging an item to copy it.
"""
DragLinkCursor = CursorShape(21)
""" A cursor that is usually used when dragging an item to make a link to it.
"""
BitmapCursor = CursorShape(24)
"""  
"""


class DateFormat(QtEnumeration):
    """
    """
    ...


TextDate = DateFormat(0)
""" 
"""
ISODate = DateFormat(1)
""" 
"""
SystemLocaleShortDate = DateFormat("?")
""" 
"""
SystemLocaleLongDate = DateFormat("?")
""" 
"""
DefaultLocaleShortDate = DateFormat("?")
""" 
"""
DefaultLocaleLongDate = DateFormat("?")
""" 
"""
SystemLocaleDate = DateFormat(2)
""" 
"""
LocaleDate = DateFormat("?")
""" 
"""
LocalDate = SystemLocaleDate
""" 
"""


class DayOfWeek(QtEnumeration):
    """
    """
    ...


Monday = DayOfWeek(1)
""" 
"""
Tuesday = DayOfWeek(2)
""" 
"""
Wednesday = DayOfWeek(3)
""" 
"""
Thursday = DayOfWeek(4)
""" 
"""
Friday = DayOfWeek(5)
""" 
"""
Saturday = DayOfWeek(6)
""" 
"""
Sunday = DayOfWeek(7)
""" 
"""


class DockWidgetArea(QtEnumeration):
    """
    """
    ...


LeftDockWidgetArea = DockWidgetArea(0x1)
""" 
"""
RightDockWidgetArea = DockWidgetArea(0x2)
""" 
"""
TopDockWidgetArea = DockWidgetArea(0x4)
""" 
"""
BottomDockWidgetArea = DockWidgetArea(0x8)
""" 
"""
AllDockWidgetAreas = DockWidgetArea("DockWidgetArea_Mask")
""" 
"""
NoDockWidgetArea = DockWidgetArea(0)
""" 
"""


class DropAction(QtEnumeration):
    """
    """
    ...


CopyAction = DropAction(0x1)
""" Copy the data to the target.
"""
MoveAction = DropAction(0x2)
""" Move the data from the source to the target.
"""
LinkAction = DropAction(0x4)
""" Create a link from the source to the target.
"""
ActionMask = DropAction(0xff)
"""  
"""
IgnoreAction = DropAction(0x0)
""" Ignore the action (do nothing with the data).
"""
TargetMoveAction = DropAction(0x8002)
""" 
"""


class EventPriority(QtEnumeration):
    """ This enum can be used to specify event priorities.

    """
    ...


HighEventPriority = EventPriority(1)
""" Events with this priority are sent before events with NormalEventPriority or LowEventPriority.
"""
NormalEventPriority = EventPriority(0)
""" Events with this priority are sent after events with HighEventPriority, but before events with LowEventPriority.
"""
LowEventPriority = EventPriority(-1)
""" Events with this priority are sent after events with HighEventPriority or NormalEventPriority.
"""


class FillRule(QtEnumeration):
    """ Specifies which method should be used to fill the paths and polygons.

    """
    ...


OddEvenFill = FillRule(0)
""" Specifies that the region is filled using the odd even fill rule. With this rule, we determine whether a point is inside the shape by using the following method. Draw a horizontal line from the point to a location outside the shape, and count the number of intersections. If the number of intersections is an odd number, the point is inside the shape. This mode is the default.
"""
WindingFill = FillRule(1)
""" Specifies that the region is filled using the non zero winding rule. With this rule, we determine whether a point is inside the shape by using the following method. Draw a horizontal line from the point to a location outside the shape. Determine whether the direction of the line at each intersection point is up or down. The winding number is determined by summing the direction of each intersection. If the number is non zero, the point is inside the shape. This fill mode can also in most cases be considered as the intersection of closed shapes.
"""


class FocusPolicy(QtEnumeration):
    """ This enum type defines the various policies a widget can have with respect to acquiring keyboard focus.
    """
    ...


TabFocus = FocusPolicy(0x1)
""" the widget accepts focus by tabbing.
"""
ClickFocus = FocusPolicy(0x2)
""" the widget accepts focus by clicking.
"""
StrongFocus = FocusPolicy(TabFocus | ClickFocus | 0x8)
""" the widget accepts focus by both tabbing and clicking. On Mac OS X this will also be indicate that the widget accepts tab focus when in 'Text/List focus mode'.
"""
WheelFocus = FocusPolicy(StrongFocus | 0x4)
""" like Qt.StrongFocus plus the widget accepts focus by using the mouse wheel.
"""
NoFocus = FocusPolicy(0)
""" the widget does not accept focus.
"""


class FocusReason(QtEnumeration):
    """
    """
    ...


MouseFocusReason = FocusReason(0)
""" A mouse action occurred.
"""
TabFocusReason = FocusReason(1)
""" The Tab key was pressed.
"""
BacktabFocusReason = FocusReason(2)
""" A Backtab occurred. The input for this may include the Shift or Control keys; e.g. Shift+Tab.
"""
ActiveWindowFocusReason = FocusReason(3)
""" The window system made this window either active or inactive.
"""
PopupFocusReason = FocusReason(4)
""" The application opened/closed a pop-up that grabbed/released the keyboard focus.
"""
ShortcutFocusReason = FocusReason(5)
""" The user typed a label's buddy shortcut
"""
MenuBarFocusReason = FocusReason(6)
""" The menu bar took focus.
"""
OtherFocusReason = FocusReason(7)
""" Another reason, usually application-specific.
"""


class GestureFlag(QtEnumeration):
    """ This enum type describes additional flags that can be used when subscribing to a gesture.

    """
    ...


DontStartGestureOnChildren = GestureFlag(0x01)
""" By default gestures can start on the widget or over any of its children. Use this flag to disable this and allow a gesture to start on the widget only.
"""
ReceivePartialGestures = GestureFlag(0x02)
""" 
"""
IgnoredGesturesPropagateToParent = GestureFlag(0x04)
""" 
"""


class GestureState(QtEnumeration):
    """ This enum type describes the state of a gesture.

    """
    ...


GestureStarted = GestureState(1)
""" A continuous gesture has started.
"""
GestureUpdated = GestureState(2)
""" A gesture continues.
"""
GestureFinished = GestureState(3)
""" A gesture has finished.
"""
GestureCanceled = GestureState(4)
""" A gesture was canceled.
"""


class GestureType(QtEnumeration):
    """ This enum type describes the standard gestures.

    """
    ...


TapGesture = GestureType(1)
""" A Tap gesture.
"""
TapAndHoldGesture = GestureType(2)
""" A Tap-And-Hold (Long-Tap) gesture.
"""
PanGesture = GestureType(3)
""" A Pan gesture.
"""
PinchGesture = GestureType(4)
""" A Pinch gesture.
"""
SwipeGesture = GestureType(5)
""" A Swipe gesture.
"""
CustomGesture = GestureType(0x0100)
""" A flag that can be used to test if the gesture is a user-defined gesture ID.
"""


class GlobalColor(QtEnumeration):
    """
    """
    ...


white = GlobalColor(3)
""" White (#ffffff) 
"""
black = GlobalColor(2)
""" Black (#000000) 
"""
red = GlobalColor(7)
""" Red (#ff0000) 
"""
darkRed = GlobalColor(13)
""" Dark red (#800000) 
"""
green = GlobalColor(8)
""" Green (#00ff00) 
"""
darkGreen = GlobalColor(14)
""" Dark green (#008000) 
"""
blue = GlobalColor(9)
""" Blue (#0000ff) 
"""
darkBlue = GlobalColor(15)
""" Dark blue (#000080) 
"""
cyan = GlobalColor(10)
""" Cyan (#00ffff) 
"""
darkCyan = GlobalColor(16)
""" Dark cyan (#008080) 
"""
magenta = GlobalColor(11)
""" Magenta (#ff00ff) 
"""
darkMagenta = GlobalColor(17)
""" Dark magenta (#800080) 
"""
yellow = GlobalColor(12)
""" Yellow (#ffff00) 
"""
darkYellow = GlobalColor(18)
""" Dark yellow (#808000) 
"""
gray = GlobalColor(5)
""" Gray (#a0a0a4) 
"""
darkGray = GlobalColor(4)
""" Dark gray (#808080) 
"""
lightGray = GlobalColor(6)
""" Light gray (#c0c0c0) 
"""
transparent = GlobalColor(19)
""" 
"""
color0 = GlobalColor(0)
""" 0 pixel value (for bitmaps)
"""
color1 = GlobalColor(1)
""" 1 pixel value (for bitmaps)
"""


class HitTestAccuracy(QtEnumeration):
    """
    """
    ...


ExactHit = HitTestAccuracy(0)
""" The point at which input occurred must coincide exactly with input-sensitive parts of the document.
"""
FuzzyHit = HitTestAccuracy(1)
""" The point at which input occurred can lie close to input-sensitive parts of the document.
"""


class ImageConversionFlag(QtEnumeration):
    """ The options marked "(default)" are set if no other values from the list are included (since the defaults are zero):
Dithering mode preference for RGB channels:
Dithering mode preference for alpha channel:
Color matching versus dithering preference:

    """
    ...


AutoColor = ImageConversionFlag(0x00000000)
""" 
"""
ColorOnly = ImageConversionFlag(0x00000003)
""" 
"""
MonoOnly = ImageConversionFlag(0x00000002)
""" The pixmap becomes monochrome. If necessary, it is dithered using the chosen dithering algorithm.
"""
DiffuseDither = ImageConversionFlag(0x00000000)
""" (default) - A high-quality dither.
"""
OrderedDither = ImageConversionFlag(0x00000010)
""" A faster, more ordered dither.
"""
ThresholdDither = ImageConversionFlag(0x00000020)
""" No dithering; closest color is used.
"""
ThresholdAlphaDither = ImageConversionFlag(0x00000000)
""" (default) - No dithering.
"""
OrderedAlphaDither = ImageConversionFlag(0x00000004)
""" A faster, more ordered dither.
"""
DiffuseAlphaDither = ImageConversionFlag(0x00000008)
""" A high-quality dither.
"""
PreferDither = ImageConversionFlag(0x00000040)
""" (default when converting to a pixmap) - Always dither 32-bit images when the image is converted to 8 bits.
"""
AvoidDither = ImageConversionFlag(0x00000080)
""" (default when converting for the purpose of saving to file) - Dither 32-bit images only if the image has more than 256 colors and it is being converted to 8 bits.
"""
NoOpaqueDetection = ImageConversionFlag(0x00000100)
""" Do not check whether the image contains non-opaque pixels. Use this if you know that the image is semi-transparent and you want to avoid the overhead of checking the pixels in the image until a non-opaque pixel is found, or if you want the pixmap to retain an alpha channel for some other reason. If the image has no alpha channel this flag has no effect.
"""


class InputMethodHint(QtEnumeration):
    """ Flags that alter the behavior:
Flags that restrict input (exclusive flags):
Masks:

    """
    ...


ImhNone = InputMethodHint(0x0)
""" No hints.
"""
ImhHiddenText = InputMethodHint(0x1)
""" 
"""
ImhNoAutoUppercase = InputMethodHint(0x2)
""" The input method should not try to automatically switch to upper case when a sentence ends.
"""
ImhPreferNumbers = InputMethodHint(0x4)
""" Numbers are preferred (but not required).
"""
ImhPreferUppercase = InputMethodHint(0x8)
""" Upper case letters are preferred (but not required).
"""
ImhPreferLowercase = InputMethodHint(0x10)
""" Lower case letters are preferred (but not required).
"""
ImhNoPredictiveText = InputMethodHint(0x20)
""" Do not use predictive text (i.e. dictionary lookup) while typing.
"""
ImhDigitsOnly = InputMethodHint(0x10000)
""" Only digits are allowed.
"""
ImhFormattedNumbersOnly = InputMethodHint(0x20000)
""" Only number input is allowed. This includes decimal point and minus sign.
"""
ImhUppercaseOnly = InputMethodHint(0x40000)
""" Only upper case letter input is allowed.
"""
ImhLowercaseOnly = InputMethodHint(0x80000)
""" Only lower case letter input is allowed.
"""
ImhDialableCharactersOnly = InputMethodHint(0x100000)
""" Only characters suitable for phone dialling are allowed.
"""
ImhEmailCharactersOnly = InputMethodHint(0x200000)
""" Only characters suitable for email addresses are allowed.
"""
ImhUrlCharactersOnly = InputMethodHint(0x400000)
""" Only characters suitable for URLs are allowed.
"""
ImhExclusiveInputMask = InputMethodHint(0xffff0000)
""" This mask yields nonzero if any of the exclusive flags are used.
"""


class InputMethodQuery(QtEnumeration):
    """
    """
    ...


ImMicroFocus = InputMethodQuery(0)
""" The rectangle covering the area of the input cursor in widget coordinates.
"""
ImFont = InputMethodQuery(1)
""" The currently used font for text input.
"""
ImCursorPosition = InputMethodQuery(2)
""" 
"""
ImSurroundingText = InputMethodQuery(3)
""" The plain text around the input area, for example the current paragraph.
"""
ImCurrentSelection = InputMethodQuery(4)
""" The currently selected text.
"""
ImMaximumTextLength = InputMethodQuery(5)
""" The maximum number of characters that the widget can hold. If there is no limit, QVariant() is returned.
"""
ImAnchorPosition = InputMethodQuery(6)
""" 
"""


class ItemDataRole(QtEnumeration):
    """ Each item in the model has a set of data elements associated with it, each with its own role. The roles are used by the view to indicate to the model which type of data it needs. Custom models should return data in these types.
The general purpose roles (and the associated types) are:
Roles describing appearance and meta data (with associated types):
Accessibility roles (with associated types):
User roles:

    """
    ...


DisplayRole = ItemDataRole(0)
""" 
"""
DecorationRole = ItemDataRole(1)
""" 
"""
EditRole = ItemDataRole(2)
""" 
"""
ToolTipRole = ItemDataRole(3)
""" 
"""
StatusTipRole = ItemDataRole(4)
""" 
"""
WhatsThisRole = ItemDataRole(5)
""" 
"""
SizeHintRole = ItemDataRole(13)
""" 
"""
FontRole = ItemDataRole(6)
""" 
"""
TextAlignmentRole = ItemDataRole(7)
""" 
"""
BackgroundRole = ItemDataRole(8)
""" 
"""
BackgroundColorRole = ItemDataRole(8)
""" This role is obsolete. Use BackgroundRole instead.
"""
ForegroundRole = ItemDataRole(9)
""" 
"""
TextColorRole = ItemDataRole(9)
""" This role is obsolete. Use ForegroundRole instead.
"""
CheckStateRole = ItemDataRole(10)
""" 
"""
InitialSortOrderRole = ItemDataRole(14)
""" 
"""
AccessibleTextRole = ItemDataRole(11)
""" 
"""
AccessibleDescriptionRole = ItemDataRole(12)
""" 
"""
UserRole = ItemDataRole(32)
""" The first role that can be used for application-specific purposes.
"""


class ItemFlag(QtEnumeration):
    """ This enum describes the properties of an item:

    """
    ...


NoItemFlags = ItemFlag(0)
""" It does not have any properties set.
"""
ItemIsSelectable = ItemFlag(1)
""" It can be selected.
"""
ItemIsEditable = ItemFlag(2)
""" It can be edited.
"""
ItemIsDragEnabled = ItemFlag(4)
""" It can be dragged.
"""
ItemIsDropEnabled = ItemFlag(8)
""" It can be used as a drop target.
"""
ItemIsUserCheckable = ItemFlag(16)
""" It can be checked or unchecked by the user.
"""
ItemIsEnabled = ItemFlag(32)
""" The user can interact with the item.
"""
ItemIsTristate = ItemFlag(64)
""" The item is checkable with three separate states.
"""


class ItemSelectionMode(QtEnumeration):
    """
    """
    ...


ContainsItemShape = ItemSelectionMode(0x0)
""" 
"""
IntersectsItemShape = ItemSelectionMode(0x1)
""" 
"""
ContainsItemBoundingRect = ItemSelectionMode(0x2)
""" 
"""
IntersectsItemBoundingRect = ItemSelectionMode(0x3)
""" 
"""


class Key(QtEnumeration):
    """ The key names used by Qt.

    """
    ...


Key_Escape = Key(0x01000000)
"""  
"""
Key_Tab = Key(0x01000001)
"""  
"""
Key_Backtab = Key(0x01000002)
"""  
"""
Key_Backspace = Key(0x01000003)
"""  
"""
Key_Return = Key(0x01000004)
"""  
"""
Key_Enter = Key(0x01000005)
""" Typically located on the keypad.
"""
Key_Insert = Key(0x01000006)
"""  
"""
Key_Delete = Key(0x01000007)
"""  
"""
Key_Pause = Key(0x01000008)
""" The Pause/Break key (
"""
Key_Print = Key(0x01000009)
"""  
"""
Key_SysReq = Key(0x0100000a)
"""  
"""
Key_Clear = Key(0x0100000b)
"""  
"""
Key_Home = Key(0x01000010)
"""  
"""
Key_End = Key(0x01000011)
"""  
"""
Key_Left = Key(0x01000012)
"""  
"""
Key_Up = Key(0x01000013)
"""  
"""
Key_Right = Key(0x01000014)
"""  
"""
Key_Down = Key(0x01000015)
"""  
"""
Key_PageUp = Key(0x01000016)
"""  
"""
Key_PageDown = Key(0x01000017)
"""  
"""
Key_Shift = Key(0x01000020)
"""  
"""
Key_Control = Key(0x01000021)
""" On Mac OS X, this corresponds to the Command keys.
"""
Key_Meta = Key(0x01000022)
""" On Mac OS X, this corresponds to the Control keys. On Windows keyboards, this key is mapped to the Windows key.
"""
Key_Alt = Key(0x01000023)
"""  
"""
Key_AltGr = Key(0x01001103)
""" On Windows, when the KeyDown event for this key is sent, the Ctrl+Alt modifiers are also set.
"""
Key_CapsLock = Key(0x01000024)
"""  
"""
Key_NumLock = Key(0x01000025)
"""  
"""
Key_ScrollLock = Key(0x01000026)
"""  
"""
Key_F1 = Key(0x01000030)
"""  
"""
Key_F2 = Key(0x01000031)
"""  
"""
Key_F3 = Key(0x01000032)
"""  
"""
Key_F4 = Key(0x01000033)
"""  
"""
Key_F5 = Key(0x01000034)
"""  
"""
Key_F6 = Key(0x01000035)
"""  
"""
Key_F7 = Key(0x01000036)
"""  
"""
Key_F8 = Key(0x01000037)
"""  
"""
Key_F9 = Key(0x01000038)
"""  
"""
Key_F10 = Key(0x01000039)
"""  
"""
Key_F11 = Key(0x0100003a)
"""  
"""
Key_F12 = Key(0x0100003b)
"""  
"""
Key_F13 = Key(0x0100003c)
"""  
"""
Key_F14 = Key(0x0100003d)
"""  
"""
Key_F15 = Key(0x0100003e)
"""  
"""
Key_F16 = Key(0x0100003f)
"""  
"""
Key_F17 = Key(0x01000040)
"""  
"""
Key_F18 = Key(0x01000041)
"""  
"""
Key_F19 = Key(0x01000042)
"""  
"""
Key_F20 = Key(0x01000043)
"""  
"""
Key_F21 = Key(0x01000044)
"""  
"""
Key_F22 = Key(0x01000045)
"""  
"""
Key_F23 = Key(0x01000046)
"""  
"""
Key_F24 = Key(0x01000047)
"""  
"""
Key_F25 = Key(0x01000048)
"""  
"""
Key_F26 = Key(0x01000049)
"""  
"""
Key_F27 = Key(0x0100004a)
"""  
"""
Key_F28 = Key(0x0100004b)
"""  
"""
Key_F29 = Key(0x0100004c)
"""  
"""
Key_F30 = Key(0x0100004d)
"""  
"""
Key_F31 = Key(0x0100004e)
"""  
"""
Key_F32 = Key(0x0100004f)
"""  
"""
Key_F33 = Key(0x01000050)
"""  
"""
Key_F34 = Key(0x01000051)
"""  
"""
Key_F35 = Key(0x01000052)
"""  
"""
Key_Super_L = Key(0x01000053)
"""  
"""
Key_Super_R = Key(0x01000054)
"""  
"""
Key_Menu = Key(0x01000055)
"""  
"""
Key_Hyper_L = Key(0x01000056)
"""  
"""
Key_Hyper_R = Key(0x01000057)
"""  
"""
Key_Help = Key(0x01000058)
"""  
"""
Key_Direction_L = Key(0x01000059)
"""  
"""
Key_Direction_R = Key(0x01000060)
"""  
"""
Key_Space = Key(0x20)
"""  
"""
Key_Any = Key_Space
"""  
"""
Key_Exclam = Key(0x21)
"""  
"""
Key_QuoteDbl = Key(0x22)
"""  
"""
Key_NumberSign = Key(0x23)
"""  
"""
Key_Dollar = Key(0x24)
"""  
"""
Key_Percent = Key(0x25)
"""  
"""
Key_Ampersand = Key(0x26)
"""  
"""
Key_Apostrophe = Key(0x27)
"""  
"""
Key_ParenLeft = Key(0x28)
"""  
"""
Key_ParenRight = Key(0x29)
"""  
"""
Key_Asterisk = Key(0x2a)
"""  
"""
Key_Plus = Key(0x2b)
"""  
"""
Key_Comma = Key(0x2c)
"""  
"""
Key_Minus = Key(0x2d)
"""  
"""
Key_Period = Key(0x2e)
"""  
"""
Key_Slash = Key(0x2f)
"""  
"""
Key_0 = Key(0x30)
"""  
"""
Key_1 = Key(0x31)
"""  
"""
Key_2 = Key(0x32)
"""  
"""
Key_3 = Key(0x33)
"""  
"""
Key_4 = Key(0x34)
"""  
"""
Key_5 = Key(0x35)
"""  
"""
Key_6 = Key(0x36)
"""  
"""
Key_7 = Key(0x37)
"""  
"""
Key_8 = Key(0x38)
"""  
"""
Key_9 = Key(0x39)
"""  
"""
Key_Colon = Key(0x3a)
"""  
"""
Key_Semicolon = Key(0x3b)
"""  
"""
Key_Less = Key(0x3c)
"""  
"""
Key_Equal = Key(0x3d)
"""  
"""
Key_Greater = Key(0x3e)
"""  
"""
Key_Question = Key(0x3f)
"""  
"""
Key_At = Key(0x40)
"""  
"""
Key_A = Key(0x41)
"""  
"""
Key_B = Key(0x42)
"""  
"""
Key_C = Key(0x43)
"""  
"""
Key_D = Key(0x44)
"""  
"""
Key_E = Key(0x45)
"""  
"""
Key_F = Key(0x46)
"""  
"""
Key_G = Key(0x47)
"""  
"""
Key_H = Key(0x48)
"""  
"""
Key_I = Key(0x49)
"""  
"""
Key_J = Key(0x4a)
"""  
"""
Key_K = Key(0x4b)
"""  
"""
Key_L = Key(0x4c)
"""  
"""
Key_M = Key(0x4d)
"""  
"""
Key_N = Key(0x4e)
"""  
"""
Key_O = Key(0x4f)
"""  
"""
Key_P = Key(0x50)
"""  
"""
Key_Q = Key(0x51)
"""  
"""
Key_R = Key(0x52)
"""  
"""
Key_S = Key(0x53)
"""  
"""
Key_T = Key(0x54)
"""  
"""
Key_U = Key(0x55)
"""  
"""
Key_V = Key(0x56)
"""  
"""
Key_W = Key(0x57)
"""  
"""
Key_X = Key(0x58)
"""  
"""
Key_Y = Key(0x59)
"""  
"""
Key_Z = Key(0x5a)
"""  
"""
Key_BracketLeft = Key(0x5b)
"""  
"""
Key_Backslash = Key(0x5c)
"""  
"""
Key_BracketRight = Key(0x5d)
"""  
"""
Key_AsciiCircum = Key(0x5e)
"""  
"""
Key_Underscore = Key(0x5f)
"""  
"""
Key_QuoteLeft = Key(0x60)
"""  
"""
Key_BraceLeft = Key(0x7b)
"""  
"""
Key_Bar = Key(0x7c)
"""  
"""
Key_BraceRight = Key(0x7d)
"""  
"""
Key_AsciiTilde = Key(0x7e)
"""  
"""
Key_nobreakspace = Key(0x0a0)
"""  
"""
Key_exclamdown = Key(0x0a1)
"""  
"""
Key_cent = Key(0x0a2)
"""  
"""
Key_sterling = Key(0x0a3)
"""  
"""
Key_currency = Key(0x0a4)
"""  
"""
Key_yen = Key(0x0a5)
"""  
"""
Key_brokenbar = Key(0x0a6)
"""  
"""
Key_section = Key(0x0a7)
"""  
"""
Key_diaeresis = Key(0x0a8)
"""  
"""
Key_copyright = Key(0x0a9)
"""  
"""
Key_ordfeminine = Key(0x0aa)
"""  
"""
Key_guillemotleft = Key(0x0ab)
"""  
"""
Key_notsign = Key(0x0ac)
"""  
"""
Key_hyphen = Key(0x0ad)
"""  
"""
Key_registered = Key(0x0ae)
"""  
"""
Key_macron = Key(0x0af)
"""  
"""
Key_degree = Key(0x0b0)
"""  
"""
Key_plusminus = Key(0x0b1)
"""  
"""
Key_twosuperior = Key(0x0b2)
"""  
"""
Key_threesuperior = Key(0x0b3)
"""  
"""
Key_acute = Key(0x0b4)
"""  
"""
Key_mu = Key(0x0b5)
"""  
"""
Key_paragraph = Key(0x0b6)
"""  
"""
Key_periodcentered = Key(0x0b7)
"""  
"""
Key_cedilla = Key(0x0b8)
"""  
"""
Key_onesuperior = Key(0x0b9)
"""  
"""
Key_masculine = Key(0x0ba)
"""  
"""
Key_guillemotright = Key(0x0bb)
"""  
"""
Key_onequarter = Key(0x0bc)
"""  
"""
Key_onehalf = Key(0x0bd)
"""  
"""
Key_threequarters = Key(0x0be)
"""  
"""
Key_questiondown = Key(0x0bf)
"""  
"""
Key_Agrave = Key(0x0c0)
"""  
"""
Key_Aacute = Key(0x0c1)
"""  
"""
Key_Acircumflex = Key(0x0c2)
"""  
"""
Key_Atilde = Key(0x0c3)
"""  
"""
Key_Adiaeresis = Key(0x0c4)
"""  
"""
Key_Aring = Key(0x0c5)
"""  
"""
Key_AE = Key(0x0c6)
"""  
"""
Key_Ccedilla = Key(0x0c7)
"""  
"""
Key_Egrave = Key(0x0c8)
"""  
"""
Key_Eacute = Key(0x0c9)
"""  
"""
Key_Ecircumflex = Key(0x0ca)
"""  
"""
Key_Ediaeresis = Key(0x0cb)
"""  
"""
Key_Igrave = Key(0x0cc)
"""  
"""
Key_Iacute = Key(0x0cd)
"""  
"""
Key_Icircumflex = Key(0x0ce)
"""  
"""
Key_Idiaeresis = Key(0x0cf)
"""  
"""
Key_ETH = Key(0x0d0)
"""  
"""
Key_Ntilde = Key(0x0d1)
"""  
"""
Key_Ograve = Key(0x0d2)
"""  
"""
Key_Oacute = Key(0x0d3)
"""  
"""
Key_Ocircumflex = Key(0x0d4)
"""  
"""
Key_Otilde = Key(0x0d5)
"""  
"""
Key_Odiaeresis = Key(0x0d6)
"""  
"""
Key_multiply = Key(0x0d7)
"""  
"""
Key_Ooblique = Key(0x0d8)
"""  
"""
Key_Ugrave = Key(0x0d9)
"""  
"""
Key_Uacute = Key(0x0da)
"""  
"""
Key_Ucircumflex = Key(0x0db)
"""  
"""
Key_Udiaeresis = Key(0x0dc)
"""  
"""
Key_Yacute = Key(0x0dd)
"""  
"""
Key_THORN = Key(0x0de)
"""  
"""
Key_ssharp = Key(0x0df)
"""  
"""
Key_division = Key(0x0f7)
"""  
"""
Key_ydiaeresis = Key(0x0ff)
"""  
"""
Key_Multi_key = Key(0x01001120)
"""  
"""
Key_Codeinput = Key(0x01001137)
"""  
"""
Key_SingleCandidate = Key(0x0100113c)
"""  
"""
Key_MultipleCandidate = Key(0x0100113d)
"""  
"""
Key_PreviousCandidate = Key(0x0100113e)
"""  
"""
Key_Mode_switch = Key(0x0100117e)
"""  
"""
Key_Kanji = Key(0x01001121)
"""  
"""
Key_Muhenkan = Key(0x01001122)
"""  
"""
Key_Henkan = Key(0x01001123)
"""  
"""
Key_Romaji = Key(0x01001124)
"""  
"""
Key_Hiragana = Key(0x01001125)
"""  
"""
Key_Katakana = Key(0x01001126)
"""  
"""
Key_Hiragana_Katakana = Key(0x01001127)
"""  
"""
Key_Zenkaku = Key(0x01001128)
"""  
"""
Key_Hankaku = Key(0x01001129)
"""  
"""
Key_Zenkaku_Hankaku = Key(0x0100112a)
"""  
"""
Key_Touroku = Key(0x0100112b)
"""  
"""
Key_Massyo = Key(0x0100112c)
"""  
"""
Key_Kana_Lock = Key(0x0100112d)
"""  
"""
Key_Kana_Shift = Key(0x0100112e)
"""  
"""
Key_Eisu_Shift = Key(0x0100112f)
"""  
"""
Key_Eisu_toggle = Key(0x01001130)
"""  
"""
Key_Hangul = Key(0x01001131)
"""  
"""
Key_Hangul_Start = Key(0x01001132)
"""  
"""
Key_Hangul_End = Key(0x01001133)
"""  
"""
Key_Hangul_Hanja = Key(0x01001134)
"""  
"""
Key_Hangul_Jamo = Key(0x01001135)
"""  
"""
Key_Hangul_Romaja = Key(0x01001136)
"""  
"""
Key_Hangul_Jeonja = Key(0x01001138)
"""  
"""
Key_Hangul_Banja = Key(0x01001139)
"""  
"""
Key_Hangul_PreHanja = Key(0x0100113a)
"""  
"""
Key_Hangul_PostHanja = Key(0x0100113b)
"""  
"""
Key_Hangul_Special = Key(0x0100113f)
"""  
"""
Key_Dead_Grave = Key(0x01001250)
"""  
"""
Key_Dead_Acute = Key(0x01001251)
"""  
"""
Key_Dead_Circumflex = Key(0x01001252)
"""  
"""
Key_Dead_Tilde = Key(0x01001253)
"""  
"""
Key_Dead_Macron = Key(0x01001254)
"""  
"""
Key_Dead_Breve = Key(0x01001255)
"""  
"""
Key_Dead_Abovedot = Key(0x01001256)
"""  
"""
Key_Dead_Diaeresis = Key(0x01001257)
"""  
"""
Key_Dead_Abovering = Key(0x01001258)
"""  
"""
Key_Dead_Doubleacute = Key(0x01001259)
"""  
"""
Key_Dead_Caron = Key(0x0100125a)
"""  
"""
Key_Dead_Cedilla = Key(0x0100125b)
"""  
"""
Key_Dead_Ogonek = Key(0x0100125c)
"""  
"""
Key_Dead_Iota = Key(0x0100125d)
"""  
"""
Key_Dead_Voiced_Sound = Key(0x0100125e)
"""  
"""
Key_Dead_Semivoiced_Sound = Key(0x0100125f)
"""  
"""
Key_Dead_Belowdot = Key(0x01001260)
"""  
"""
Key_Dead_Hook = Key(0x01001261)
"""  
"""
Key_Dead_Horn = Key(0x01001262)
"""  
"""
Key_Back = Key(0x01000061)
"""  
"""
Key_Forward = Key(0x01000062)
"""  
"""
Key_Stop = Key(0x01000063)
"""  
"""
Key_Refresh = Key(0x01000064)
"""  
"""
Key_VolumeDown = Key(0x01000070)
"""  
"""
Key_VolumeMute = Key(0x01000071)
"""  
"""
Key_VolumeUp = Key(0x01000072)
"""  
"""
Key_BassBoost = Key(0x01000073)
"""  
"""
Key_BassUp = Key(0x01000074)
"""  
"""
Key_BassDown = Key(0x01000075)
"""  
"""
Key_TrebleUp = Key(0x01000076)
"""  
"""
Key_TrebleDown = Key(0x01000077)
"""  
"""
Key_MediaPlay = Key(0x01000080)
""" A key setting the state of the media player to play
"""
Key_MediaStop = Key(0x01000081)
""" A key setting the state of the media player to stop
"""
Key_MediaPrevious = Key(0x01000082)
"""  
"""
Key_MediaNext = Key(0x01000083)
"""  
"""
Key_MediaRecord = Key(0x01000084)
"""  
"""
Key_MediaPause = Key(0x1000085)
""" A key setting the state of the media player to pause (
"""
Key_MediaTogglePlayPause = Key(0x1000086)
""" A key to toggle the play/pause state in the media player (rather than setting an absolute state)
"""
Key_HomePage = Key(0x01000090)
"""  
"""
Key_Favorites = Key(0x01000091)
"""  
"""
Key_Search = Key(0x01000092)
"""  
"""
Key_Standby = Key(0x01000093)
"""  
"""
Key_OpenUrl = Key(0x01000094)
"""  
"""
Key_LaunchMail = Key(0x010000a0)
"""  
"""
Key_LaunchMedia = Key(0x010000a1)
"""  
"""
Key_Launch0 = Key(0x010000a2)
""" On X11 this key is mapped to "My Computer" (XF86XK_MyComputer) key for legacy reasons.
"""
Key_Launch1 = Key(0x010000a3)
""" On X11 this key is mapped to "Calculator" (XF86XK_Calculator) key for legacy reasons.
"""
Key_Launch2 = Key(0x010000a4)
""" On X11 this key is mapped to XF86XK_Launch0 key for legacy reasons.
"""
Key_Launch3 = Key(0x010000a5)
""" On X11 this key is mapped to XF86XK_Launch1 key for legacy reasons.
"""
Key_Launch4 = Key(0x010000a6)
""" On X11 this key is mapped to XF86XK_Launch2 key for legacy reasons.
"""
Key_Launch5 = Key(0x010000a7)
""" On X11 this key is mapped to XF86XK_Launch3 key for legacy reasons.
"""
Key_Launch6 = Key(0x010000a8)
""" On X11 this key is mapped to XF86XK_Launch4 key for legacy reasons.
"""
Key_Launch7 = Key(0x010000a9)
""" On X11 this key is mapped to XF86XK_Launch5 key for legacy reasons.
"""
Key_Launch8 = Key(0x010000aa)
""" On X11 this key is mapped to XF86XK_Launch6 key for legacy reasons.
"""
Key_Launch9 = Key(0x010000ab)
""" On X11 this key is mapped to XF86XK_Launch7 key for legacy reasons.
"""
Key_LaunchA = Key(0x010000ac)
""" On X11 this key is mapped to XF86XK_Launch8 key for legacy reasons.
"""
Key_LaunchB = Key(0x010000ad)
""" On X11 this key is mapped to XF86XK_Launch9 key for legacy reasons.
"""
Key_LaunchC = Key(0x010000ae)
""" On X11 this key is mapped to XF86XK_LaunchA key for legacy reasons.
"""
Key_LaunchD = Key(0x010000af)
""" On X11 this key is mapped to XF86XK_LaunchB key for legacy reasons.
"""
Key_LaunchE = Key(0x010000b0)
""" On X11 this key is mapped to XF86XK_LaunchC key for legacy reasons.
"""
Key_LaunchF = Key(0x010000b1)
""" On X11 this key is mapped to XF86XK_LaunchD key for legacy reasons.
"""
Key_LaunchG = Key(0x0100010e)
""" On X11 this key is mapped to XF86XK_LaunchE key for legacy reasons.
"""
Key_LaunchH = Key(0x0100010f)
""" On X11 this key is mapped to XF86XK_LaunchF key for legacy reasons.
"""
Key_MonBrightnessUp = Key(0x010000b2)
"""  
"""
Key_MonBrightnessDown = Key(0x010000b3)
"""  
"""
Key_KeyboardLightOnOff = Key(0x010000b4)
"""  
"""
Key_KeyboardBrightnessUp = Key(0x010000b5)
"""  
"""
Key_KeyboardBrightnessDown = Key(0x010000b6)
"""  
"""
Key_PowerOff = Key(0x010000b7)
"""  
"""
Key_WakeUp = Key(0x010000b8)
"""  
"""
Key_Eject = Key(0x010000b9)
"""  
"""
Key_ScreenSaver = Key(0x010000ba)
"""  
"""
Key_WWW = Key(0x010000bb)
"""  
"""
Key_Memo = Key(0x010000bc)
"""  
"""
Key_LightBulb = Key(0x010000bd)
"""  
"""
Key_Shop = Key(0x010000be)
"""  
"""
Key_History = Key(0x010000bf)
"""  
"""
Key_AddFavorite = Key(0x010000c0)
"""  
"""
Key_HotLinks = Key(0x010000c1)
"""  
"""
Key_BrightnessAdjust = Key(0x010000c2)
"""  
"""
Key_Finance = Key(0x010000c3)
"""  
"""
Key_Community = Key(0x010000c4)
"""  
"""
Key_AudioRewind = Key(0x010000c5)
"""  
"""
Key_BackForward = Key(0x010000c6)
"""  
"""
Key_ApplicationLeft = Key(0x010000c7)
"""  
"""
Key_ApplicationRight = Key(0x010000c8)
"""  
"""
Key_Book = Key(0x010000c9)
"""  
"""
Key_CD = Key(0x010000ca)
"""  
"""
Key_Calculator = Key(0x010000cb)
""" On X11 this key is not mapped for legacy reasons. Use Qt.Key_Launch1 instead.
"""
Key_ToDoList = Key(0x010000cc)
"""  
"""
Key_ClearGrab = Key(0x010000cd)
"""  
"""
Key_Close = Key(0x010000ce)
"""  
"""
Key_Copy = Key(0x010000cf)
"""  
"""
Key_Cut = Key(0x010000d0)
"""  
"""
Key_Display = Key(0x010000d1)
"""  
"""
Key_DOS = Key(0x010000d2)
"""  
"""
Key_Documents = Key(0x010000d3)
"""  
"""
Key_Excel = Key(0x010000d4)
"""  
"""
Key_Explorer = Key(0x010000d5)
"""  
"""
Key_Game = Key(0x010000d6)
"""  
"""
Key_Go = Key(0x010000d7)
"""  
"""
Key_iTouch = Key(0x010000d8)
"""  
"""
Key_LogOff = Key(0x010000d9)
"""  
"""
Key_Market = Key(0x010000da)
"""  
"""
Key_Meeting = Key(0x010000db)
"""  
"""
Key_MenuKB = Key(0x010000dc)
"""  
"""
Key_MenuPB = Key(0x010000dd)
"""  
"""
Key_MySites = Key(0x010000de)
"""  
"""
Key_News = Key(0x010000df)
"""  
"""
Key_OfficeHome = Key(0x010000e0)
"""  
"""
Key_Option = Key(0x010000e1)
"""  
"""
Key_Paste = Key(0x010000e2)
"""  
"""
Key_Phone = Key(0x010000e3)
"""  
"""
Key_Calendar = Key(0x010000e4)
"""  
"""
Key_Reply = Key(0x010000e5)
"""  
"""
Key_Reload = Key(0x010000e6)
"""  
"""
Key_RotateWindows = Key(0x010000e7)
"""  
"""
Key_RotationPB = Key(0x010000e8)
"""  
"""
Key_RotationKB = Key(0x010000e9)
"""  
"""
Key_Save = Key(0x010000ea)
"""  
"""
Key_Send = Key(0x010000eb)
"""  
"""
Key_Spell = Key(0x010000ec)
"""  
"""
Key_SplitScreen = Key(0x010000ed)
"""  
"""
Key_Support = Key(0x010000ee)
"""  
"""
Key_TaskPane = Key(0x010000ef)
"""  
"""
Key_Terminal = Key(0x010000f0)
"""  
"""
Key_Tools = Key(0x010000f1)
"""  
"""
Key_Travel = Key(0x010000f2)
"""  
"""
Key_Video = Key(0x010000f3)
"""  
"""
Key_Word = Key(0x010000f4)
"""  
"""
Key_Xfer = Key(0x010000f5)
"""  
"""
Key_ZoomIn = Key(0x010000f6)
"""  
"""
Key_ZoomOut = Key(0x010000f7)
"""  
"""
Key_Away = Key(0x010000f8)
"""  
"""
Key_Messenger = Key(0x010000f9)
"""  
"""
Key_WebCam = Key(0x010000fa)
"""  
"""
Key_MailForward = Key(0x010000fb)
"""  
"""
Key_Pictures = Key(0x010000fc)
"""  
"""
Key_Music = Key(0x010000fd)
"""  
"""
Key_Battery = Key(0x010000fe)
"""  
"""
Key_Bluetooth = Key(0x010000ff)
"""  
"""
Key_WLAN = Key(0x01000100)
"""  
"""
Key_UWB = Key(0x01000101)
"""  
"""
Key_AudioForward = Key(0x01000102)
"""  
"""
Key_AudioRepeat = Key(0x01000103)
"""  
"""
Key_AudioRandomPlay = Key(0x01000104)
"""  
"""
Key_Subtitle = Key(0x01000105)
"""  
"""
Key_AudioCycleTrack = Key(0x01000106)
"""  
"""
Key_Time = Key(0x01000107)
"""  
"""
Key_Hibernate = Key(0x01000108)
"""  
"""
Key_View = Key(0x01000109)
"""  
"""
Key_TopMenu = Key(0x0100010a)
"""  
"""
Key_PowerDown = Key(0x0100010b)
"""  
"""
Key_Suspend = Key(0x0100010c)
"""  
"""
Key_ContrastAdjust = Key(0x0100010d)
"""  
"""
Key_MediaLast = Key(0x0100ffff)
"""  
"""
Key_unknown = Key(0x01ffffff)
"""  
"""
Key_Call = Key(0x01100004)
""" A key to answer or initiate a call (see Qt.Key_ToggleCallHangup for a key to toggle current call state)
"""
Key_Camera = Key(0x01100020)
""" A key to activate the camera shutter
"""
Key_CameraFocus = Key(0x01100021)
""" A key to focus the camera
"""
Key_Context1 = Key(0x01100000)
"""  
"""
Key_Context2 = Key(0x01100001)
"""  
"""
Key_Context3 = Key(0x01100002)
"""  
"""
Key_Context4 = Key(0x01100003)
"""  
"""
Key_Flip = Key(0x01100006)
"""  
"""
Key_Hangup = Key(0x01100005)
""" A key to end an ongoing call (see Qt.Key_ToggleCallHangup for a key to toggle current call state)
"""
Key_No = Key(0x01010002)
"""  
"""
Key_Select = Key(0x01010000)
"""  
"""
Key_Yes = Key(0x01010001)
"""  
"""
Key_ToggleCallHangup = Key(0x01100007)
""" A key to toggle the current call state (ie. either answer, or hangup) depending on current call state
"""
Key_VoiceDial = Key(0x01100008)
"""  
"""
Key_LastNumberRedial = Key(0x01100009)
"""  
"""
Key_Execute = Key(0x01020003)
"""  
"""
Key_Printer = Key(0x01020002)
"""  
"""
Key_Play = Key(0x01020005)
"""  
"""
Key_Sleep = Key(0x01020004)
"""  
"""
Key_Zoom = Key(0x01020006)
"""  
"""
Key_Cancel = Key(0x01020001)
"""  
"""


class KeyboardModifier(QtEnumeration):
    """ This enum describes the modifier keys.

    """
    ...


NoModifier = KeyboardModifier(0x00000000)
""" No modifier key is pressed.
"""
ShiftModifier = KeyboardModifier(0x02000000)
""" A Shift key on the keyboard is pressed.
"""
ControlModifier = KeyboardModifier(0x04000000)
""" A Ctrl key on the keyboard is pressed.
"""
AltModifier = KeyboardModifier(0x08000000)
""" An Alt key on the keyboard is pressed.
"""
MetaModifier = KeyboardModifier(0x10000000)
""" A Meta key on the keyboard is pressed.
"""
KeypadModifier = KeyboardModifier(0x20000000)
""" A keypad button is pressed.
"""
GroupSwitchModifier = KeyboardModifier(0x40000000)
""" X11 only. A Mode_switch key on the keyboard is pressed.
"""


class LayoutDirection(QtEnumeration):
    """ Specifies the direction of Qt's layouts and text handling.

    """
    ...


LeftToRight = LayoutDirection(0)
""" Left-to-right layout.
"""
RightToLeft = LayoutDirection(1)
""" Right-to-left layout.
"""
LayoutDirectionAuto = LayoutDirection(2)
""" Automatic layout.
"""


class MaskMode(QtEnumeration):
    """
    """
    ...


MaskInColor = MaskMode(0)
""" Creates a mask where all pixels matching the given color are opaque.
"""
MaskOutColor = MaskMode(1)
""" Creates a mask where all pixels matching the given color are transparent.
"""


class MatchFlag(QtEnumeration):
    """ This enum describes the type of matches that can be used when searching for items in a model.

    """
    ...


MatchExactly = MatchFlag(0)
""" 
"""
MatchFixedString = MatchFlag(8)
""" 
"""
MatchContains = MatchFlag(1)
""" The search term is contained in the item.
"""
MatchStartsWith = MatchFlag(2)
""" The search term matches the start of the item.
"""
MatchEndsWith = MatchFlag(3)
""" The search term matches the end of the item.
"""
MatchCaseSensitive = MatchFlag(16)
""" The search is case sensitive.
"""
MatchRegExp = MatchFlag(4)
""" Performs string-based matching using a regular expression as the search term.
"""
MatchWildcard = MatchFlag(5)
""" Performs string-based matching using a string with wildcards as the search term.
"""
MatchWrap = MatchFlag(32)
""" Perform a search that wraps around, so that when the search reaches the last item in the model, it begins again at the first item and continues until all items have been examined.
"""
MatchRecursive = MatchFlag(64)
""" Searches the entire hierarchy.
"""


class Modifier(QtEnumeration):
    """ This enum provides shorter names for the keyboard modifier keys supported by Qt.

    """
    ...


SHIFT = Modifier(ShiftModifier)
""" The Shift keys provided on all standard keyboards.
"""
META = Modifier(MetaModifier)
""" The Meta keys.
"""
CTRL = Modifier(ControlModifier)
""" The Ctrl keys.
"""
ALT = Modifier(AltModifier)
""" The normal Alt keys, but not keys like AltGr.
"""
UNICODE_ACCEL = Modifier(0x00000000)
""" The shortcut is specified as a Unicode code point, not as a Qt Key.
"""


class MouseButton(QtEnumeration):
    """ This enum type describes the different mouse buttons.

    """
    ...


NoButton = MouseButton(0x00000000)
""" 
"""
LeftButton = MouseButton(0x00000001)
""" The left button is pressed, or an event refers to the left button. (The left button may be the right button on left-handed mice.)
"""
RightButton = MouseButton(0x00000002)
""" The right button.
"""
MidButton = MouseButton(0x00000004)
""" The middle button.
"""
MiddleButton = MidButton
""" The middle button.
"""
XButton1 = MouseButton(0x00000008)
""" The first X button.
"""
XButton2 = MouseButton(0x00000010)
""" The second X button.
"""


class NavigationMode(QtEnumeration):
    """ This enum type describes the mode for moving focus.

    """
    ...


NavigationModeNone = NavigationMode(0)
""" Only the touch screen is used.
"""
NavigationModeKeypadTabOrder = NavigationMode(1)
""" 
"""
NavigationModeKeypadDirectional = NavigationMode(2)
""" 
"""
NavigationModeCursorAuto = NavigationMode(3)
""" The mouse cursor is used to change focus, it is displayed only on non touchscreen devices. The keypad is used to implement a virtual cursor, unless the device has an analog mouse type of input device (e.g. touchpad). This is the recommended setting for an application such as a web browser that needs pointer control on both touch and non-touch devices.
"""
NavigationModeCursorForceVisible = NavigationMode(4)
""" The mouse cursor is used to change focus, it is displayed regardless of device type. The keypad is used to implement a virtual cursor, unless the device has an analog mouse type of input device (e.g. touchpad)
"""


class Orientation(QtEnumeration):
    """ This type is used to signify an object's orientation.

    """
    ...


Horizontal = Orientation(0x1)
""" 
"""
Vertical = Orientation(0x2)
""" 
"""


class PenCapStyle(QtEnumeration):
    """
    """
    ...


SquareCap = PenCapStyle(0x10)
""" a square line end that covers the end point and extends beyond it by half the line width.
"""
FlatCap = PenCapStyle(0x00)
""" a square line end that does not cover the end point of the line.
"""
RoundCap = PenCapStyle(0x20)
""" a rounded line end.
"""


class PenJoinStyle(QtEnumeration):
    """
    """
    ...


BevelJoin = PenJoinStyle(0x40)
""" The triangular notch between the two lines is filled.
"""
MiterJoin = PenJoinStyle(0x00)
""" The outer edges of the lines are extended to meet at an angle, and this area is filled.
"""
RoundJoin = PenJoinStyle(0x80)
""" A circular arc between the two lines is filled.
"""
SvgMiterJoin = PenJoinStyle(0x100)
""" 
"""


class PenStyle(QtEnumeration):
    """
    """
    ...


SolidLine = PenStyle(1)
""" A plain line.
"""
DashDotLine = PenStyle(4)
""" Alternate dots and dashes.
"""
NoPen = PenStyle(0)
""" 
"""
DashLine = PenStyle(2)
""" Dashes separated by a few pixels.
"""
DotLine = PenStyle(3)
""" Dots separated by a few pixels.
"""
DashDotDotLine = PenStyle(5)
""" One dash, two dots, one dash, two dots.
"""
CustomDashLine = PenStyle(6)
""" 
"""


class ScrollBarPolicy(QtEnumeration):
    """
    """
    ...


ScrollBarAsNeeded = ScrollBarPolicy(0)
""" 
"""
ScrollBarAlwaysOff = ScrollBarPolicy(1)
""" 
"""
ScrollBarAlwaysOn = ScrollBarPolicy(2)
""" 
"""


class ShortcutContext(QtEnumeration):
    """
    """
    ...


WidgetShortcut = ShortcutContext(0)
""" The shortcut is active when its parent widget has focus.
"""
WidgetWithChildrenShortcut = ShortcutContext(3)
""" The shortcut is active when its parent widget, or any of its children has focus. Children which are top-level widgets, except pop-ups, are not affected by this shortcut context.
"""
WindowShortcut = ShortcutContext(1)
""" The shortcut is active when its parent widget is a logical subwidget of the active top-level window.
"""
ApplicationShortcut = ShortcutContext(2)
""" The shortcut is active when one of the applications windows are active.
"""


class SizeHint(QtEnumeration):
    """
    """
    ...


MinimumSize = SizeHint(0)
""" is used to specify the minimum size of a graphics layout item.
"""
PreferredSize = SizeHint(1)
""" is used to specify the preferred size of a graphics layout item.
"""
MaximumSize = SizeHint(2)
""" is used to specify the maximum size of a graphics layout item.
"""
MinimumDescent = SizeHint(3)
""" is used to specify the minimum descent of a text string in a graphics layout item.
"""


class SizeMode(QtEnumeration):
    """
    """
    ...


AbsoluteSize = SizeMode(0)
""" Specifies the size using absolute measurements.
"""
RelativeSize = SizeMode(1)
""" Specifies the size relative to the bounding rectangle, typically using percentage measurements.
"""


class SortOrder(QtEnumeration):
    """ This enum describes how the items in a widget are sorted.

    """
    ...


AscendingOrder = SortOrder(0)
""" The items are sorted ascending e.g. starts with 'AAA' ends with 'ZZZ' in Latin-1 locales
"""
DescendingOrder = SortOrder(1)
""" The items are sorted descending e.g. starts with 'ZZZ' ends with 'AAA' in Latin-1 locales
"""


class TextElideMode(QtEnumeration):
    """ This enum specifies where the ellipsis should appear when displaying texts that don't fit:

    """
    ...


ElideLeft = TextElideMode(0)
""" The ellipsis should appear at the beginning of the text.
"""
ElideRight = TextElideMode(1)
""" The ellipsis should appear at the end of the text.
"""
ElideMiddle = TextElideMode(2)
""" The ellipsis should appear in the middle of the text.
"""
ElideNone = TextElideMode(3)
""" Ellipsis should NOT appear in the text.
"""


class TextFlag(QtEnumeration):
    """ This enum type is used to define some modifier flags. Some of these flags only make sense in the context of printing:

    """
    ...


TextSingleLine = TextFlag(0x0100)
""" Treats all whitespace as spaces and prints just one line.
"""
TextDontClip = TextFlag(0x0200)
""" If it's impossible to stay within the given bounds, it prints outside.
"""
TextExpandTabs = TextFlag(0x0400)
""" Makes the U+0009 (ASCII tab) character move to the next tab stop.
"""
TextShowMnemonic = TextFlag(0x0800)
""" 
"""
TextWordWrap = TextFlag(0x1000)
""" Breaks lines at appropriate points, e.g. at word boundaries.
"""
TextWrapAnywhere = TextFlag(0x2000)
""" Breaks lines anywhere, even within words.
"""
TextHideMnemonic = TextFlag(0x8000)
""" Same as Qt.TextShowMnemonic but doesn't draw the underlines.
"""
TextDontPrint = TextFlag(0x4000)
""" Treat this text as "hidden" and don't print it.
"""
IncludeTrailingSpaces = TextFlag(0x08000000)
""" 
"""
TextIncludeTrailingSpaces = IncludeTrailingSpaces
""" Same as IncludeTrailingSpaces
"""
TextJustificationForced = TextFlag(0x10000)
""" Ensures that text lines are justified.
"""


class TextFormat(QtEnumeration):
    """
    """
    ...


PlainText = TextFormat(0)
""" The text string is interpreted as a plain text string.
"""
RichText = TextFormat(1)
""" The text string is interpreted as a rich text string.
"""
AutoText = TextFormat(2)
""" The text string is interpreted as for Qt.RichText if Qt.mightBeRichText() returns true, otherwise as Qt.PlainText.
"""
LogText = TextFormat(3)
""" 
"""


class TextInteractionFlag(QtEnumeration):
    """ This enum specifies how a text displaying widget reacts to user input.

    """
    ...


NoTextInteraction = TextInteractionFlag(0)
""" No interaction with the text is possible.
"""
TextSelectableByMouse = TextInteractionFlag(1)
""" Text can be selected with the mouse and copied to the clipboard using a context menu or standard keyboard shortcuts.
"""
TextSelectableByKeyboard = TextInteractionFlag(2)
""" Text can be selected with the cursor keys on the keyboard. A text cursor is shown.
"""
LinksAccessibleByMouse = TextInteractionFlag(4)
""" Links can be highlighted and activated with the mouse.
"""
LinksAccessibleByKeyboard = TextInteractionFlag(8)
""" Links can be focused using tab and activated with enter.
"""
TextEditable = TextInteractionFlag(16)
""" The text is fully editable.
"""
TextEditorInteraction = TextInteractionFlag(TextSelectableByMouse | TextSelectableByKeyboard | TextEditable)
""" The default for a text editor.
"""
TextBrowserInteraction = TextInteractionFlag(TextSelectableByMouse | LinksAccessibleByMouse | LinksAccessibleByKeyboard)
""" 
"""


class TileRule(QtEnumeration):
    """ This enum describes how to repeat or stretch the parts of an image when drawing.

    """
    ...


StretchTile = TileRule(0)
""" Scale the image to fit to the available area.
"""
RepeatTile = TileRule(1)
""" Repeat the image until there is no more space. May crop the last image.
"""
RoundTile = TileRule(2)
""" Similar to Repeat, but scales the image down to ensure that the last tile is not cropped.
"""


class TimeSpec(QtEnumeration):
    """
    """
    ...


LocalTime = TimeSpec(0)
""" Locale dependent time (Timezones and Daylight Savings Time).
"""
UTC = TimeSpec(1)
""" Coordinated Universal Time, replaces Greenwich Mean Time.
"""
OffsetFromUTC = TimeSpec(2)
""" An offset in seconds from Coordinated Universal Time.
"""


class ToolBarArea(QtEnumeration):
    """
    """
    ...


LeftToolBarArea = ToolBarArea(0x1)
""" 
"""
RightToolBarArea = ToolBarArea(0x2)
""" 
"""
TopToolBarArea = ToolBarArea(0x4)
""" 
"""
BottomToolBarArea = ToolBarArea(0x8)
""" 
"""
AllToolBarAreas = ToolBarArea("ToolBarArea_Mask")
""" 
"""
NoToolBarArea = ToolBarArea(0)
""" 
"""


class ToolButtonStyle(QtEnumeration):
    """ The style of the tool button, describing how the button's text and icon should be displayed.

    """
    ...


ToolButtonIconOnly = ToolButtonStyle(0)
""" Only display the icon.
"""
ToolButtonTextOnly = ToolButtonStyle(1)
""" Only display the text.
"""
ToolButtonTextBesideIcon = ToolButtonStyle(2)
""" The text appears beside the icon.
"""
ToolButtonTextUnderIcon = ToolButtonStyle(3)
""" The text appears under the icon.
"""
ToolButtonFollowStyle = ToolButtonStyle(4)
""" 
"""


class TouchPointState(QtEnumeration):
    """
    """
    ...


TouchPointPressed = TouchPointState(0x01)
""" The touch point is now pressed.
"""
TouchPointMoved = TouchPointState(0x02)
""" The touch point moved.
"""
TouchPointStationary = TouchPointState(0x04)
""" The touch point did not move.
"""
TouchPointReleased = TouchPointState(0x08)
""" The touch point was released.
"""


class TransformationMode(QtEnumeration):
    """ This enum type defines whether image transformations (e.g., scaling) should be smooth or not.

    """
    ...


FastTransformation = TransformationMode(0)
""" The transformation is performed quickly, with no smoothing.
"""
SmoothTransformation = TransformationMode(1)
""" The resulting image is transformed using bilinear filtering.
"""


class UIEffect(QtEnumeration):
    """ This enum describes the available UI effects.
Note that all effects are disabled on screens running at less than 16-bit color depth.

    """
    ...


UI_AnimateMenu = UIEffect(1)
""" Show animated menus.
"""
UI_FadeMenu = UIEffect(2)
""" Show faded menus.
"""
UI_AnimateCombo = UIEffect(3)
""" Show animated comboboxes.
"""
UI_AnimateTooltip = UIEffect(4)
""" Show tooltip animations.
"""
UI_FadeTooltip = UIEffect(5)
""" Show tooltip fading effects.
"""
UI_AnimateToolBox = UIEffect(6)
""" Reserved
"""


class WhiteSpaceMode(QtEnumeration):
    """
    """
    ...


WhiteSpaceNormal = WhiteSpaceMode(0)
""" The whitespace mode used to display normal word wrapped text in paragraphs.
"""
WhiteSpacePre = WhiteSpaceMode(1)
""" A preformatted text mode in which whitespace is reproduced exactly.
"""
WhiteSpaceNoWrap = WhiteSpaceMode(2)
"""  
"""


class WidgetAttribute(QtEnumeration):
    """
    """
    ...


WA_AcceptDrops = WidgetAttribute(78)
""" 
"""
WA_AlwaysShowToolTips = WidgetAttribute(84)
""" Enables tooltips for inactive windows.
"""
WA_ContentsPropagated = WidgetAttribute(3)
""" This flag is superfluous and obsolete; it no longer has any effect. Since Qt 4.1, all widgets that do not set WA_PaintOnScreen propagate their contents.
"""
WA_CustomWhatsThis = WidgetAttribute(47)
""" Indicates that the widget wants to continue operating normally in "What's This?" mode. This is set by the widget's author.
"""
WA_DeleteOnClose = WidgetAttribute(55)
""" 
"""
WA_Disabled = WidgetAttribute(0)
""" 
"""
WA_DontShowOnScreen = WidgetAttribute(103)
""" Indicates that the widget is hidden or is not a part of the viewable Desktop.
"""
WA_ForceDisabled = WidgetAttribute(32)
""" 
"""
WA_ForceUpdatesDisabled = WidgetAttribute(59)
""" 
"""
WA_GroupLeader = WidgetAttribute(72)
""" 
"""
WA_Hover = WidgetAttribute(74)
""" 
"""
WA_InputMethodEnabled = WidgetAttribute(14)
""" 
"""
WA_KeyboardFocusChange = WidgetAttribute(77)
""" Set on a toplevel window when the users changes focus with the keyboard (tab, backtab, or shortcut).
"""
WA_KeyCompression = WidgetAttribute(33)
""" 
"""
WA_LayoutOnEntireRect = WidgetAttribute(48)
""" 
"""
WA_LayoutUsesWidgetRect = WidgetAttribute(92)
""" 
"""
WA_MacNoClickThrough = WidgetAttribute(12)
""" When a widget that has this attribute set is clicked, and its window is inactive, the click will make the window active but won't be seen by the widget. Typical use of this attribute is on widgets with "destructive" actions, such as a "Delete" button. WA_MacNoClickThrough also applies to all child widgets of the widget that has it set.
"""
WA_MacOpaqueSizeGrip = WidgetAttribute(85)
""" Indicates that the native Carbon size grip should be opaque instead of transparent (the default). This attribute is only applicable to Mac OS X and is set by the widget's author.
"""
WA_MacShowFocusRect = WidgetAttribute(88)
""" 
"""
WA_MacNormalSize = WidgetAttribute(89)
""" Indicates the widget should have the normal size for widgets in Mac OS X. This attribute is only applicable to Mac OS X.
"""
WA_MacSmallSize = WidgetAttribute(90)
""" Indicates the widget should have the small size for widgets in Mac OS X. This attribute is only applicable to Mac OS X.
"""
WA_MacMiniSize = WidgetAttribute(91)
""" Indicates the widget should have the mini size for widgets in Mac OS X. This attribute is only applicable to Mac OS X.
"""
WA_MacVariableSize = WidgetAttribute(102)
""" Indicates the widget can choose between alternative sizes for widgets to avoid clipping. This attribute is only applicable to Mac OS X.
"""
WA_MacBrushedMetal = WidgetAttribute(46)
""" Indicates the widget should be drawn in the brushed metal style as supported by the windowing system. This attribute is only applicable to Mac OS X.
"""
WA_Mapped = WidgetAttribute(11)
""" Indicates that the widget is mapped on screen. This is set/cleared by the Qt kernel.
"""
WA_MouseNoMask = WidgetAttribute(71)
""" 
"""
WA_MouseTracking = WidgetAttribute(2)
""" 
"""
WA_Moved = WidgetAttribute(43)
""" 
"""
WA_MSWindowsUseDirect3D = WidgetAttribute(94)
""" This value is obsolete and has no effect.
"""
WA_NoChildEventsForParent = WidgetAttribute(58)
""" Indicates that the widget does not want ChildAdded or ChildRemoved events sent to its parent. This is rarely necessary but can help to avoid automatic insertion widgets like splitters and layouts. This is set by a widget's author.
"""
WA_NoChildEventsFromChildren = WidgetAttribute(39)
""" Indicates that the widget does not want to receive ChildAdded or ChildRemoved events sent from its children. This is set by a widget's author.
"""
WA_NoMouseReplay = WidgetAttribute(54)
""" Used for pop-up widgets. Indicates that the most recent mouse press event should not be replayed when the pop-up widget closes. The flag is set by the widget's author and cleared by the Qt kernel every time the widget receives a new mouse event.
"""
WA_NoMousePropagation = WidgetAttribute(73)
""" Prohibits mouse events from being propagated to the widget's parent. This attribute is disabled by default.
"""
WA_TransparentForMouseEvents = WidgetAttribute(51)
""" When enabled, this attribute disables the delivery of mouse events to the widget and its children. Mouse events are delivered to other widgets as if the widget and its children were not present in the widget hierarchy; mouse clicks and other events effectively "pass through" them. This attribute is disabled by default.
"""
WA_NoSystemBackground = WidgetAttribute(9)
""" Indicates that the widget has no background, i.e. when the widget receives paint events, the background is not automatically repainted.
"""
WA_OpaquePaintEvent = WidgetAttribute(4)
""" Indicates that the widget paints all its pixels when it receives a paint event. Thus, it is not required for operations like updating, resizing, scrolling and focus changes to erase the widget before generating paint events. The use of WA_OpaquePaintEvent provides a small optimization by helping to reduce flicker on systems that do not support double buffering and avoiding computational cycles necessary to erase the background prior to painting.
"""
WA_NoBackground = WA_OpaquePaintEvent
""" This value is obsolete. Use WA_OpaquePaintEvent instead.
"""
WA_OutsideWSRange = WidgetAttribute(49)
""" Indicates that the widget is outside the valid range of the window system's coordinate system. A widget outside the valid range cannot be mapped on screen. This is set/cleared by the Qt kernel.
"""
WA_PaintOnScreen = WidgetAttribute(8)
""" Indicates that the widget wants to draw directly onto the screen. Widgets with this attribute set do not participate in composition management, i.e. they cannot be semi-transparent or shine through semi-transparent overlapping widgets.
"""
WA_PaintOutsidePaintEvent = WidgetAttribute(13)
""" 
"""
WA_PaintUnclipped = WidgetAttribute(52)
""" Makes all painters operating on this widget unclipped. Children of this widget or other widgets in front of it do not clip the area the painter can paint on. This flag is only supported for widgets with the WA_PaintOnScreen flag set. The preferred way to do this in a cross platform way is to create a transparent widget that lies in front of the other widgets.
"""
WA_PendingMoveEvent = WidgetAttribute(34)
""" Indicates that a move event is pending, e.g., when a hidden widget was moved. This flag is set or cleared by the Qt kernel.
"""
WA_PendingResizeEvent = WidgetAttribute(35)
""" Indicates that a resize event is pending, e.g., when a hidden widget was resized. This flag is set or cleared by the Qt kernel.
"""
WA_QuitOnClose = WidgetAttribute(76)
""" 
"""
WA_Resized = WidgetAttribute(42)
""" 
"""
WA_RightToLeft = WidgetAttribute(56)
""" Indicates that the layout direction for the widget is right to left.
"""
WA_SetCursor = WidgetAttribute(38)
""" 
"""
WA_SetFont = WidgetAttribute(37)
""" 
"""
WA_SetPalette = WidgetAttribute(36)
""" 
"""
WA_SetStyle = WidgetAttribute(86)
""" 
"""
WA_ShowModal = WidgetAttribute(70)
""" 
"""
WA_StaticContents = WidgetAttribute(5)
""" Indicates that the widget contents are north-west aligned and static. On resize, such a widget will receive paint events only for parts of itself that are newly visible. This flag is set or cleared by the widget's author.
"""
WA_StyleSheet = WidgetAttribute(97)
""" 
"""
WA_TranslucentBackground = WidgetAttribute(120)
""" 
"""
WA_UnderMouse = WidgetAttribute(1)
""" 
"""
WA_UpdatesDisabled = WidgetAttribute(10)
""" Indicates that updates are blocked (including the system background). This flag is set or cleared by the Qt kernel.
"""
WA_WindowModified = WidgetAttribute(41)
""" 
"""
WA_WindowPropagation = WidgetAttribute(80)
""" Makes a toplevel window inherit font and palette from its parent.
"""
WA_MacAlwaysShowToolWindow = WidgetAttribute(96)
""" On Mac OS X, show the tool window even when the application is not active. By default, all tool windows are hidden when the application is inactive.
"""
WA_SetLocale = WidgetAttribute(87)
""" Indicates the locale should be taken into consideration in the widget.
"""
WA_StyledBackground = WidgetAttribute(93)
""" Indicates the widget should be drawn using a styled background.
"""
WA_ShowWithoutActivating = WidgetAttribute(98)
""" Show the widget without making it active.
"""
WA_NativeWindow = WidgetAttribute(100)
""" Indicates that a native window is created for the widget. Enabling this flag will also force a native window for the widget's ancestors unless Qt.WA_DontCreateNativeAncestors is set.
"""
WA_DontCreateNativeAncestors = WidgetAttribute(101)
""" Indicates that the widget's ancestors are kept non-native even though the widget itself is native.
"""
WA_X11NetWmWindowTypeDesktop = WidgetAttribute(104)
""" Adds _NET_WM_WINDOW_TYPE_DESKTOP to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeDock = WidgetAttribute(105)
""" Adds _NET_WM_WINDOW_TYPE_DOCK to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeToolBar = WidgetAttribute(106)
""" Adds _NET_WM_WINDOW_TYPE_TOOLBAR to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeMenu = WidgetAttribute(107)
""" Adds _NET_WM_WINDOW_TYPE_MENU to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeUtility = WidgetAttribute(108)
""" Adds _NET_WM_WINDOW_TYPE_UTILITY to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeSplash = WidgetAttribute(109)
""" Adds _NET_WM_WINDOW_TYPE_SPLASH to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeDialog = WidgetAttribute(110)
""" Adds _NET_WM_WINDOW_TYPE_DIALOG to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeDropDownMenu = WidgetAttribute(111)
""" Adds _NET_WM_WINDOW_TYPE_DROPDOWN_MENU to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypePopupMenu = WidgetAttribute(112)
""" Adds _NET_WM_WINDOW_TYPE_POPUP_MENU to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeToolTip = WidgetAttribute(113)
""" Adds _NET_WM_WINDOW_TYPE_TOOLTIP to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeNotification = WidgetAttribute(114)
""" Adds _NET_WM_WINDOW_TYPE_NOTIFICATION to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeCombo = WidgetAttribute(115)
""" Adds _NET_WM_WINDOW_TYPE_COMBO to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_X11NetWmWindowTypeDND = WidgetAttribute(116)
""" Adds _NET_WM_WINDOW_TYPE_DND to the window's _NET_WM_WINDOW_TYPE X11 window property. See http://standards.freedesktop.org/wm-spec/ for more details. This attribute has no effect on non-X11 platforms.
"""
WA_MacFrameworkScaled = WidgetAttribute(117)
""" Enables resolution independence aware mode on Mac when using Carbon. This attribute has no effect on Cocoa. The attribute is off by default and can be enabled on a per-window basis.
"""
WA_AcceptTouchEvents = WidgetAttribute(121)
""" 
"""
WA_TouchPadAcceptSingleTouchEvents = WidgetAttribute(123)
""" Allows touchpad single touch events to be sent to the widget.
"""
WA_MergeSoftkeys = WidgetAttribute(124)
""" Allows widget to merge softkeys with parent widget, i.e. widget can set only one softkeys and request softkey implementation to take rest of the softkeys from the parent. Note parents are traversed until WA_MergeSoftkeys is not set. See also Qt.WA_MergeSoftkeysRecursively This attribute currently has effect only on Symbian platforms
"""
WA_MergeSoftkeysRecursively = WidgetAttribute(125)
""" Allows widget to merge softkeys recursively with all parents. If this attribute is set, the widget parents are traversed until window boundary (widget without parent or dialog) is found. This attribute currently has effect only on Symbian platforms
"""
WA_X11DoNotAcceptFocus = WidgetAttribute(132)
""" Asks the window manager to not give focus to this top level window. This attribute has no effect on non-X11 platforms.
"""
WA_LockPortraitOrientation = WidgetAttribute(128)
""" Locks the widget to a portrait orientation, ignoring changes to the display's orientation with respect to the user.
"""
WA_LockLandscapeOrientation = WidgetAttribute(129)
""" Locks the widget to a landscape orientation, ignoring changes to the display's orientation with respect to the user.
"""
WA_AutoOrientation = WidgetAttribute(130)
""" Causes the widget to change orientation whenever the display changes orientation with respect to the user.
"""
WA_MacNoShadow = WidgetAttribute(134)
""" Since Qt 4.8, this attribute disables drop shadows for this top level window. Only affects Cocoa builds of Qt for Mac OS X.
"""


class WindowFrameSection(QtEnumeration):
    """
    """
    ...


NoSection = WindowFrameSection(0)
""" 
"""
LeftSection = WindowFrameSection(1)
""" 
"""
TopLeftSection = WindowFrameSection(2)
""" 
"""
TopSection = WindowFrameSection(3)
""" 
"""
TopRightSection = WindowFrameSection(4)
""" 
"""
RightSection = WindowFrameSection(5)
""" 
"""
BottomRightSection = WindowFrameSection(6)
""" 
"""
BottomSection = WindowFrameSection(7)
""" 
"""
BottomLeftSection = WindowFrameSection(8)
""" 
"""
TitleBarArea = WindowFrameSection(9)
""" 
"""


class WindowModality(QtEnumeration):
    """ This enum specifies the behavior of a modal window. A modal window is one that blocks input to other windows. Note that windows that are children of a modal window are not blocked.
The values are:

    """
    ...


NonModal = WindowModality(0)
""" The window is not modal and does not block input to other windows.
"""
WindowModal = WindowModality(1)
""" The window is modal to a single window hierarchy and blocks input to its parent window, all grandparent windows, and all siblings of its parent and grandparent windows.
"""
ApplicationModal = WindowModality(2)
""" The window is modal to the application and blocks input to all windows.
"""


class WindowState(QtEnumeration):
    """ This enum type is used to specify the current state of a top-level window.
The states are

    """
    ...


WindowNoState = WindowState(0x00000000)
""" The window has no state set (in normal state).
"""
WindowMinimized = WindowState(0x00000001)
""" The window is minimized (i.e. iconified).
"""
WindowMaximized = WindowState(0x00000002)
""" The window is maximized with a frame around it.
"""
WindowFullScreen = WindowState(0x00000004)
""" The window fills the entire screen without any frame around it.
"""
WindowActive = WindowState(0x00000008)
""" The window is the active window, i.e. it has keyboard focus.
"""


class WindowType(QtEnumeration):
    """ This enum type is used to specify various window-system properties for the widget. They are fairly unusual but necessary in a few cases. Some of these flags depend on whether the underlying window manager supports them.
The main types are
There are also a number of flags which you can use to customize the appearance of top-level windows. These have no effect on other windows:
Obsolete flags:

    """
    ...


Widget = WindowType(0x00000000)
""" 
"""
Window = WindowType(0x00000001)
""" Indicates that the widget is a window, usually with a window system frame and a title bar, irrespective of whether the widget has a parent or not. Note that it is not possible to unset this flag if the widget does not have a parent.
"""
Dialog = WindowType(0x00000002 | Window)
""" 
"""
Sheet = WindowType(0x00000004 | Window)
""" 
"""
Drawer = WindowType(0x00000006 | Window)
""" Indicates that the widget is a Macintosh drawer.
"""
Popup = WindowType(0x00000008 | Window)
""" Indicates that the widget is a pop-up top-level window, i.e. that it is modal, but has a window system frame appropriate for pop-up menus.
"""
Tool = WindowType(0x0000000a | Window)
""" 
"""
ToolTip = WindowType(0x0000000c | Window)
""" 
"""
SplashScreen = WindowType(0x0000000e | Window)
""" 
"""
Desktop = WindowType(0x00000010 | Window)
""" 
"""
SubWindow = WindowType(0x00000012)
""" 
"""
MSWindowsFixedSizeDialogHint = WindowType(0x00000100)
""" Gives the window a thin dialog border on Windows. This style is traditionally used for fixed-size dialogs.
"""
MSWindowsOwnDC = WindowType(0x00000200)
""" Gives the window its own display context on Windows.
"""
X11BypassWindowManagerHint = WindowType(0x00000400)
""" 
"""
FramelessWindowHint = WindowType(0x00000800)
""" Produces a borderless window. The user cannot move or resize a borderless window via the window system. On X11, the result of the flag is dependent on the window manager and its ability to understand Motif and/or NETWM hints. Most existing modern window managers can handle this.
"""
CustomizeWindowHint = WindowType(0x02000000)
""" Turns off the default window title hints.
"""
WindowTitleHint = WindowType(0x00001000)
""" Gives the window a title bar.
"""
WindowSystemMenuHint = WindowType(0x00002000)
""" 
"""
WindowMinimizeButtonHint = WindowType(0x00004000)
""" Adds a minimize button. On some platforms this implies Qt.WindowSystemMenuHint for it to work.
"""
WindowMaximizeButtonHint = WindowType(0x00008000)
""" Adds a maximize button. On some platforms this implies Qt.WindowSystemMenuHint for it to work.
"""
WindowMinMaxButtonsHint = WindowType(WindowMinimizeButtonHint | WindowMaximizeButtonHint)
""" Adds a minimize and a maximize button. On some platforms this implies Qt.WindowSystemMenuHint for it to work.
"""
WindowCloseButtonHint = WindowType(0x08000000)
""" Adds a close button. On some platforms this implies Qt.WindowSystemMenuHint for it to work.
"""
WindowContextHelpButtonHint = WindowType(0x00010000)
""" Adds a context help button to dialogs. On some platforms this implies Qt.WindowSystemMenuHint for it to work.
"""
MacWindowToolBarButtonHint = WindowType(0x10000000)
""" On Mac OS X adds a tool bar button (i.e., the oblong button that is on the top right of windows that have toolbars).
"""
BypassGraphicsProxyWidget = WindowType(0x20000000)
""" 
"""
WindowShadeButtonHint = WindowType(0x00020000)
"""  
"""
WindowStaysOnTopHint = WindowType(0x00040000)
""" Informs the window system that the window should stay on top of all other windows. Note that on some window managers on X11 you also have to pass Qt.X11BypassWindowManagerHint for this flag to work correctly.
"""
WindowStaysOnBottomHint = WindowType(0x04000000)
""" Informs the window system that the window should stay on bottom of all other windows. Note that on X11 this hint will work only in window managers that support _NET_WM_STATE_BELOW atom. If a window always on the bottom has a parent, the parent will also be left on the bottom. This window hint is currently not implemented for Mac OS X.
"""
WindowOkButtonHint = WindowType(0x00080000)
""" Adds an OK button to the window decoration of a dialog. Only supported for Windows CE.
"""
WindowCancelButtonHint = WindowType(0x00100000)
""" Adds a Cancel button to the window decoration of a dialog. Only supported for Windows CE.
"""
WindowSoftkeysVisibleHint = WindowType(0x40000000)
""" Makes softkeys visible when widget is fullscreen. Only supported for Symbian.
"""
WindowSoftkeysRespondHint = WindowType(0x80000000)
""" 
"""
WindowType_Mask = WindowType(0x000000ff)
""" A mask for extracting the window type part of the window flags.
"""
WMouseNoMask = WindowType(0x00080000)
""" 
"""
WDestructiveClose = WindowType(0x00100000)
""" 
"""
WStaticContents = WindowType(0x00200000)
""" 
"""
WGroupLeader = WindowType(0x00400000)
""" No longer needed.
"""
WShowModal = WindowType(0x00800000)
""" 
"""
WNoMousePropagation = WindowType(0x01000000)
""" 
"""
WType_TopLevel = Window
""" Use Qt.Window instead.
"""
WType_Dialog = Dialog
""" Use Qt.Dialog instead.
"""
WType_Popup = Popup
""" Use Qt.Popup instead.
"""
WType_Desktop = Desktop
""" Use Qt.Desktop instead.
"""
WType_Mask = WindowType_Mask
""" Use Qt.WindowType_Mask instead.
"""
WStyle_Customize = WindowType(0)
""" No longer needed.
"""
WStyle_NormalBorder = WindowType(0)
""" No longer needed.
"""
WStyle_DialogBorder = MSWindowsFixedSizeDialogHint
""" Use Qt.MSWindowsFixedSizeDialogHint instead.
"""
WStyle_NoBorder = FramelessWindowHint
""" Use Qt.FramelessWindowHint instead.
"""
WStyle_Title = WindowTitleHint
""" Use Qt.WindowTitleHint instead.
"""
WStyle_SysMenu = WindowSystemMenuHint
""" Use Qt.WindowSystemMenuHint instead.
"""
WStyle_Minimize = WindowMinimizeButtonHint
""" Use Qt.WindowMinimizeButtonHint instead.
"""
WStyle_Maximize = WindowMaximizeButtonHint
""" Use Qt.WindowMaximizeButtonHint instead.
"""
WStyle_MinMax = WindowType(WStyle_Minimize | WStyle_Maximize)
""" Use Qt.WindowMinMaxButtonsHint instead.
"""
WStyle_Tool = Tool
""" Use Qt.Tool instead.
"""
WStyle_StaysOnTop = WindowStaysOnTopHint
""" Use Qt.WindowStaysOnTopHint instead.
"""
WStyle_ContextHelp = WindowContextHelpButtonHint
""" Use Qt.WindowContextHelpButtonHint instead.
"""
WPaintDesktop = WindowType(0)
""" No longer needed.
"""
WPaintClever = WindowType(0)
""" No longer needed.
"""
WX11BypassWM = X11BypassWindowManagerHint
""" Use Qt.X11BypassWindowManagerHint instead.
"""
WWinOwnDC = MSWindowsOwnDC
""" Use Qt.MSWindowsOwnDC instead.
"""
WMacSheet = Sheet
""" Use Qt.Sheet instead.
"""
WMacDrawer = Drawer
""" Use Qt.Drawer instead.
"""
WStyle_Splash = SplashScreen
""" Use Qt.SplashScreen instead.
"""
WNoAutoErase = WindowType(0)
""" No longer needed.
"""
WRepaintNoErase = WindowType(0)
""" No longer needed.
"""
WNorthWestGravity = WStaticContents
""" 
"""
WType_Modal = WindowType(Dialog | WShowModal)
""" 
"""
WStyle_Dialog = Dialog
""" Use Qt.Dialog instead.
"""
WStyle_NoBorderEx = FramelessWindowHint
""" Use Qt.FramelessWindowHint instead.
"""
WResizeNoErase = WindowType(0)
""" No longer needed.
"""
WMacNoSheet = WindowType(0)
""" No longer needed.
"""
