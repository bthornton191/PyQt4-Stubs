

class QtEnumeration(object):
    def __init__(self, value):
        self.value = value

    def __or__(self, other):
        return self.value | other.value


class AlignmentFlag(QtEnumeration):
    """ This enum type is used to describe alignment. It contains horizontal and vertical flags that can be combined
        to produce the required effect.

        The TextElideMode enum can also be used in many situations to fine-tune the appearance of aligned text.
    """
    ...

AlignLeft = AlignmentFlag(0x0001)
""" Aligns with the left edge."""
AlignRight = AlignmentFlag(0x0002)
""" Aligns with the right edge."""
AlignHCenter = AlignmentFlag(0x0004)
""" Centers horizontally in the available space."""
AlignJustify = AlignmentFlag(0x0008)
""" Justifies the text in the available space."""
AlignTop = AlignmentFlag(0x0020)
""" Aligns with the top."""
AlignBottom = AlignmentFlag(0x0040)
""" Aligns with the bottom."""
AlignVCenter = AlignmentFlag(0x0080)
""" Centers vertically in the available space."""
AlignCenter = AlignHCenter | AlignVCenter
""" Centers in both dimensions."""
AlignAbsolute = AlignmentFlag(0x0010)
""" If the widget's layout direction is Qt::RightToLeft (instead of Qt::LeftToRight, the default), 
Qt::AlignLeft refers to the right edge and Qt::AlignRight to the left edge. This is normally the desired behavior. 
If you want Qt::AlignLeft to always mean "left" and Qt::AlignRight to always mean "right", 
combine the flag with Qt::AlignAbsolute."""
AlignLeading = AlignLeft
""" Synonym for Qt::AlignLeft."""
AlignTrailing = AlignRight
""" Synonym for Qt::AlignRight."""
AlignHorizontal_Mask = AlignLeft | AlignRight | AlignHCenter | AlignJustify | AlignAbsolute
AlignVertical_Mask = AlignTop | AlignBottom | AlignVCenter

class AnchorAttribute(QtEnumeration):
    """ An anchor has one or more of the following attributes:
        AnchorName
        AnchorHref
    """
    ...

AnchorName = AnchorAttribute(0)
AnchorHref = AnchorAttribute(1)

class AnchorPoint(QtEnumeration):
    """ Specifies a side of a layout item that can be anchored. This is used by QGraphicsAnchorLayout.
    """
    ...


AnchorLeft = AnchorPoint(0)
""" The left side of a layout item."""
AnchorHorizontalCenter = AnchorPoint(1)
""" A "virtual" side that is centered between the left and the right side of a layout item."""
AnchorRight = AnchorPoint(2)
""" The right side of a layout item."""
AnchorTop = AnchorPoint(3)
""" The top side of a layout item."""
AnchorVerticalCenter = AnchorPoint(4)
""" A "virtual" side that is centered between the top and the bottom side of a layout item."""
AnchorBottom = AnchorPoint(5)
""" The bottom side of a layout item."""


class ApplicationAttribute(QtEnumeration):
    """ This enum describes attributes that change the behavior of application-wide features.
        These are enabled and disabled using QCoreApplication::setAttribute(),
        and can be tested for with QCoreApplication::testAttribute().
    """
    ...


AA_ImmediateWidgetCreation = ApplicationAttribute(0)
""" Ensures that widgets are created as soon as they are constructed. By default, 
    resources for widgets are allocated on demand to improve efficiency and minimize resource usage. 
    Setting or clearing this attribute affects widgets constructed after the change. 
    Setting it tells Qt to create toplevel windows immediately. 
    Therefore, if it is important to minimize resource consumption, do not set this attribute."""
AA_MSWindowsUseDirect3DByDefault = ApplicationAttribute(1)
""" This value is obsolete and has no effect."""
AA_DontShowIconsInMenus = ApplicationAttribute(2)
""" Actions with the Icon property won't be shown in any menus unless specifically set by the 
    QAction::iconVisibleInMenu property. Menus that are currently open or menus already created 
    in the native Mac OS X menubar may not pick up a change in this attribute. 
    Changes in the QAction::iconVisibleInMenu property will always be picked up."""
AA_NativeWindows = ApplicationAttribute(3)
""" Ensures that widgets have native windows."""
AA_DontCreateNativeWidgetSiblings = ApplicationAttribute(4)
""" Ensures that siblings of native widgets stay non-native unless specifically set by the 
    Qt::WA_NativeWindow attribute."""
AA_MacPluginApplication = ApplicationAttribute(5)
""" Stops the Qt mac application from doing specific initializations that do not necessarily make sense 
    when using Qt to author a plugin. This includes avoiding loading our nib for the main menu and not taking 
    possession of the native menu bar. When setting this attribute to true will also set the 
    AA_DontUseNativeMenuBar attribute to true."""
AA_DontUseNativeMenuBar = ApplicationAttribute(6)
""" All menubars created while this attribute is set to true won't be used as a native menubar 
    (e.g, the menubar at the top of the main screen on Mac OS X or at the bottom in Windows CE)."""
AA_MacDontSwapCtrlAndMeta = ApplicationAttribute(7)
""" On Mac OS X by default, Qt swaps the Control and Meta (Command) keys 
    (i.e., whenever Control is pressed, Qt sends Meta, and whenever Meta is pressed Control is sent). 
    When this attribute is true, Qt will not do the flip. QKeySequence::StandardShortcuts will also flip accordingly 
    (i.e., QKeySequence::Copy will be Command+C on the keyboard regardless of the value set, 
    though what is output for QKeySequence::toString(QKeySequence::PortableText) will be different)."""
AA_S60DontConstructApplicationPanes = ApplicationAttribute(8)
""" Stops Qt from initializing the S60 status pane and softkey pane on Symbian. 
    This is useful to save memory and reduce startup time for applications that will run in fullscreen mode 
    during their whole lifetime. This attribute must be set before QApplication is constructed."""
AA_S60DisablePartialScreenInputMode = ApplicationAttribute(9)
""" By default in Symbian^3, a separate editing window is opened on top of an application. 
    This is exactly like editing on previous versions of Symbian behave. When this attribute is false, 
    a non-fullscreen virtual keyboard window is shown on top of application and it is ensured that the 
    focused text input widget is visible. The auto-translation of input widget is only supported for 
    applications based on QGraphicsView, but the non-fullscreen virtual keyboard will work for any kind 
    of application (i.e. QWidgets-based). By default this attribute is true. This attribute must be set 
    after QApplication is constructed. This is only supported in Symbian^3 and later Symbian releases."""
AA_X11InitThreads = ApplicationAttribute(10)
""" Calls XInitThreads() as part of the QApplication construction in order to make Xlib calls thread-safe. 
    This attribute must be set before QApplication is constructed."""
AA_CaptureMultimediaKeys = ApplicationAttribute(11)
""" Enables application to receive multimedia key events (play, next, previous etc). 
    This includes also external sources such as headsets. Application can not use Remote Control framework 
    on Symbian if this attribute is set. On Symbian, multimedia key event routing may vary between different devices. 
    For example, application on background may receive multimedia key events only if it has active audio stream 
    i.e. it is playing music or video. This attribute must be set before QApplication is constructed. 
    This attribute is only supported in Symbian platform."""


class ArrowType(QtEnumeration): ...


NoArrow = ArrowType(0)
UpArrow = ArrowType(1)
DownArrow = ArrowType(2)
LeftArrow = ArrowType(3)
RightArrow = ArrowType(4)


class AspectRatioMode(QtEnumeration):
    """ This enum type defines what happens to the aspect ratio when scaling an rectangle.
    """
    ...


IgnoreAspectRatio = AspectRatioMode(0)
""" The size is scaled freely. The aspect ratio is not preserved."""
KeepAspectRatio = AspectRatioMode(1)
""" The size is scaled to a rectangle as large as possible inside a given rectangle, preserving the aspect ratio."""
KeepAspectRatioByExpanding = AspectRatioMode(2)
""" The size is scaled to a rectangle as small as possible outside a given rectangle, preserving the aspect ratio."""


class Axis(QtEnumeration):
    """ This enum type defines three values to represent the three axes in the cartesian coordinate system.
    """
    ...


XAxis = Axis(0)
YAxis = Axis(1)
ZAxis = Axis(2)


class BGMode(QtEnumeration):
    """ Background mode.
    """
    ...


TransparentMode = BGMode(0)
OpaqueMode = BGMode(1)


class BrushStyle(QtEnumeration):
    """ This enum type defines the brush styles supported by Qt, i.e. the fill pattern of shapes drawn using QPainter.
    """
    ...


NoBrush = BrushStyle(0)
""" No brush pattern."""
SolidPattern = BrushStyle(1)
""" Uniform color."""
Dense1Pattern = BrushStyle(2)
""" Extremely dense brush pattern."""
Dense2Pattern = BrushStyle(3)
""" Very dense brush pattern."""
Dense3Pattern = BrushStyle(4)
""" Somewhat dense brush pattern."""
Dense4Pattern = BrushStyle(5)
""" Half dense brush pattern."""
Dense5Pattern = BrushStyle(6)
""" Somewhat sparse brush pattern."""
Dense6Pattern = BrushStyle(7)
""" Very sparse brush pattern."""
Dense7Pattern = BrushStyle(8)
""" Extremely sparse brush pattern."""
HorPattern = BrushStyle(9)
""" Horizontal lines."""
VerPattern = BrushStyle(10)
""" Vertical lines."""
CrossPattern = BrushStyle(11)
""" Crossing horizontal and vertical lines."""
BDiagPattern = BrushStyle(12)
""" Backward diagonal lines."""
FDiagPattern = BrushStyle(13)
""" Forward diagonal lines."""
DiagCrossPattern = BrushStyle(14)
""" Crossing diagonal lines."""
LinearGradientPattern = BrushStyle(15)
""" Linear gradient (set using a dedicated QBrush constructor)."""
ConicalGradientPattern = BrushStyle(17)
""" Conical gradient (set using a dedicated QBrush constructor)."""
RadialGradientPattern = BrushStyle(16)
""" Radial gradient (set using a dedicated QBrush constructor)."""
TexturePattern = BrushStyle(24)
""" Custom pattern (see QBrush::setTexture())."""


class CaseSensitivity(QtEnumeration): ...


CaseInsensitive = CaseSensitivity(0)
CaseSensitive = CaseSensitivity(1)


class CheckState(QtEnumeration):
    """ This enum describes the state of checkable items, controls, and widgets.
    """
    ...


Unchecked = CheckState(0)
""" The item is unchecked."""
PartiallyChecked = CheckState(1)
""" The item is partially checked. Items in hierarchical models may be partially checked if some, but not all, 
    of their children are checked."""
Checked = CheckState(2)
""" The item is checked."""


class ClipOperation(QtEnumeration): ...


NoClip = ClipOperation(0)
""" This operation turns clipping off."""
ReplaceClip = ClipOperation(1)
""" Replaces the current clip path/rect/region with the one supplied in the function call."""
IntersectClip = ClipOperation(2)
""" Intersects the current clip path/rect/region with the one supplied in the function call."""
UniteClip = ClipOperation(3)
""" Unites the current clip path/rect/region with the one supplied in the function call."""


class ConnectionType(QtEnumeration):
    """ This enum describes the types of connection that can be used between signals and slots. In particular,
        it determines whether a particular signal is delivered to a slot immediately or queued for delivery
        at a later time.

        With queued connections, the parameters must be of types that are known to Qt's meta-object system,
        because Qt needs to copy the arguments to store them in an event behind the scenes.
        If you try to use a queued connection and get the error message:
            QObject::connect: Cannot queue arguments of type 'MyType'

        Call qRegisterMetaType() to register the data type before you establish the connection.

        When using signals and slots with multiple threads, see Signals and Slots Across Threads.
    """
    ...


AutoConnection = ConnectionType(0)
""" default) If the signal is emitted from a different thread than the receiving object, the signal is queued, 
    behaving as Qt::QueuedConnection. Otherwise, the slot is invoked directly, behaving as Qt::DirectConnection. 
    The type of connection is determined when the signal is emitted."""
DirectConnection = ConnectionType(1)
""" The slot is invoked immediately, when the signal is emitted."""
QueuedConnection = ConnectionType(2)
""" The slot is invoked when control returns to the event loop of the receiver's thread. 
    The slot is executed in the receiver's thread."""
BlockingQueuedConnection = ConnectionType(4)
""" Same as QueuedConnection, except the current thread blocks until the slot returns. 
    This connection type should only be used where the emitter and receiver are in different threads."""
UniqueConnection = ConnectionType(0x80)
""" Same as AutoConnection, but the connection is made only if it does not duplicate an existing connection. 
    i.e., if the same signal is already connected to the same slot for the same pair of objects, 
    then the connection will fail. This connection type was introduced in Qt 4.6."""
AutoCompatConnection = ConnectionType(3)
""" The default type when Qt 3 support is enabled. Same as AutoConnection but will also cause warnings 
    to be output in certain situations. See Compatibility Signals and Slots for further information."""


class ContextMenuPolicy(QtEnumeration):
    """ This enum type defines the various policies a widget can have with respect to showing a context menu.
    """
    ...


NoContextMenu = ContextMenuPolicy(0)
""" the widget does not feature a context menu, context menu handling is deferred to the widget's parent."""
PreventContextMenu = ContextMenuPolicy(4)
""" the widget does not feature a context menu, and in contrast to NoContextMenu, 
    the handling is not deferred to the widget's parent. This means that all right mouse button events are 
    guaranteed to be delivered to the widget itself through mousePressEvent(), and mouseReleaseEvent()."""
DefaultContextMenu = ContextMenuPolicy(1)
""" the widget's QWidget::contextMenuEvent() handler is called."""
ActionsContextMenu = ContextMenuPolicy(2)
""" the widget displays its QWidget::actions() as context menu."""
CustomContextMenu = ContextMenuPolicy(3)
""" the widget emits the QWidget::customContextMenuRequested() signal."""


class CoordinateSystem(QtEnumeration):
    """ This enum specifies the coordinate system.
    """
    ...


DeviceCoordinates = CoordinateSystem(0)
""" Coordinates are relative to the upper-left corner of the object's paint device."""
LogicalCoordinates = CoordinateSystem(1)
""" Coordinates are relative to the upper-left corner of the object."""


class Corner(QtEnumeration):
    """ This enum type specifies a corner in a rectangle.
    """
    ...


TopLeftCorner = Corner(0x00000)
""" The top-left corner of the rectangle."""
TopRightCorner = Corner(0x00001)
""" The top-right corner of the rectangle."""
BottomLeftCorner = Corner(0x00002)
""" The bottom-left corner of the rectangle."""
BottomRightCorner = Corner(0x00003)
""" The bottom-right corner of the rectangle."""


class CursorMoveStyle(QtEnumeration):
    """ This enum describes the movement style available to text cursors.
    """
    ...


LogicalMoveStyle = CursorMoveStyle(0)
VisualMoveStyle = CursorMoveStyle(1)


class CursorShape(QtEnumeration):
    """ This enum type defines the various cursors that can be used.

        The standard arrow cursor is the default for widgets in a normal state.
    """
    ...


ArrowCursor = CursorShape(0)
""" The standard arrow cursor."""
UpArrowCursor = CursorShape(1)
""" An arrow pointing upwards toward the top of the screen."""
CrossCursor = CursorShape(2)
""" A crosshair cursor, typically used to help the user accurately select a point on the screen."""
WaitCursor = CursorShape(3)
""" An hourglass or watch cursor, usually shown during operations that prevent the user from interacting 
    with the application."""
IBeamCursor = CursorShape(4)
""" A caret or ibeam cursor, indicating that a widget can accept and display text input."""
SizeVerCursor = CursorShape(5)
""" A cursor used for elements that are used to vertically resize top-level windows."""
SizeHorCursor = CursorShape(6)
""" A cursor used for elements that are used to horizontally resize top-level windows."""
SizeBDiagCursor = CursorShape(7)
""" A cursor used for elements that are used to diagonally resize top-level windows at their 
    top-right and bottom-left corners."""
SizeFDiagCursor = CursorShape(8)
""" A cursor used for elements that are used to diagonally resize top-level windows at their 
    top-left and bottom-right corners."""
SizeAllCursor = CursorShape(9)
""" A cursor used for elements that are used to resize top-level windows in any direction."""
BlankCursor = CursorShape(10)
""" A blank/invisible cursor, typically used when the cursor shape needs to be hidden."""
SplitVCursor = CursorShape(11)
""" A cursor used for vertical splitters, indicating that a handle can be dragged horizontally 
    to adjust the use of available space."""
SplitHCursor = CursorShape(12)
""" A cursor used for horizontal splitters, indicating that a handle can be dragged vertically 
    to adjust the use of available space."""
PointingHandCursor = CursorShape(13)
""" A pointing hand cursor that is typically used for clickable elements such as hyperlinks."""
ForbiddenCursor = CursorShape(14)
""" A slashed circle cursor, typically used during drag and drop operations to indicate that dragged content 
    cannot be dropped on particular widgets or inside certain regions."""
OpenHandCursor = CursorShape(17)
""" A cursor representing an open hand, typically used to indicate that the area under the cursor is the visible part 
    of a canvas that the user can click and drag in order to scroll around."""
ClosedHandCursor = CursorShape(18)
""" A cursor representing a closed hand, typically used to indicate that a dragging operation is in 
    progress that involves scrolling."""
WhatsThisCursor = CursorShape(15)
""" An arrow with a question mark, typically used to indicate the presence of What's This? help for a widget."""
BusyCursor = CursorShape(16)
""" An hourglass or watch cursor, usually shown during operations that allow the user to interact with the 
    application while they are performed in the background."""
DragMoveCursor = CursorShape(20)
""" A cursor that is usually used when dragging an item."""
DragCopyCursor = CursorShape(19)
""" A cursor that is usually used when dragging an item to copy it."""
DragLinkCursor = CursorShape(21)
""" A cursor that is usually used when dragging an item to make a link to it."""
BitmapCursor = CursorShape(24)


class DateFormat(QtEnumeration): ...


TextDate = DateFormat(0)
""" The default Qt format, which includes the day and month name, the day number in the month, and the year in full. 
    The day and month names will be short, localized names. This is basically equivalent to using the date format 
    string, "ddd MMM d yyyy". See QDate::toString() for more information."""
ISODate = DateFormat(1)
""" ISO 8601 extended format: either YYYY-MM-DD for dates or YYYY-MM-DDTHH:mm:ss, YYYY-MM-DDTHH:mm:ssTZD 
    (e.g., 1997-07-16T19:20:30+01:00) for combined dates and times."""
SystemLocalShortDate = DateFormat("?")
""" The short format used by the operating system."""
SystemLocalLongDate = DateFormat("?")
""" The long format used by the operating system."""
DefaultLocalShortDate = DateFormat("?")
""" The short format specified by the application's locale."""
DefaultLocalLongDate = DateFormat("?")
""" The long format used by the application's locale."""
SystemLocaleDate = DateFormat(2)
""" This enum value is deprecated. Use Qt::SystemLocaleShortDate instead 
    (or Qt::SystemLocaleLongDate if you want long dates)."""
LocaleDate = DateFormat("?")
""" This enum value is deprecated. Use Qt::DefaultLocaleShortDate instead 
    (or Qt::DefaultLocaleLongDate if you want long dates)."""
LocalDate = SystemLocaleDate
""" This enum value is deprecated. Use Qt::SystemLocaleShortDate instead 
    (or Qt::SystemLocaleLongDate if you want long dates)."""


class DayOfWeek(QtEnumeration): ...


Monday = DayOfWeek(1)
Tuesday = DayOfWeek(2)
Wednesday = DayOfWeek(3)
Thursday = DayOfWeek(4)
Friday = DayOfWeek(5)
Saturday = DayOfWeek(6)
Sunday = DayOfWeek(7)


class DockWidgetArea(QtEnumeration):
    """ The DockWidgetAreas type is a typedef for QFlags<DockWidgetArea>. It stores an OR combination of
        DockWidgetArea values.
    """
    ...


LeftDockWidgetArea = DockWidgetArea(0x1)
RightDockWidgetArea = DockWidgetArea(0x2)
TopDockWidgetArea = DockWidgetArea(0x4)
BottomDockWidgetArea = DockWidgetArea(0x8)
AllDockWidgetAreas = LeftDockWidgetArea | RightDockWidgetArea | TopDockWidgetArea | BottomDockWidgetArea
NoDockWidgetArea = DockWidgetArea(0)


class DropAction(QtEnumeration):
    """ The DropActions type is a typedef for QFlags<DropAction>. It stores an OR combination of DropAction values.
    """
    ...


CopyAction = DropAction(0x1)
""" Copy the data to the target."""
MoveAction = DropAction(0x2)
""" Move the data from the source to the target."""
LinkAction = DropAction(0x4)
""" Create a link from the source to the target."""
ActionMask = DropAction(0xff)
IgnoreAction = DropAction(0x0)
""" Ignore the action (do nothing with the data)."""
TargetMoveAction = DropAction(0x8002)
""" On Windows, this value is used when the ownership of the D&D data should be taken over by the target application, 
    i.e., the source application should not delete the data. On X11 this value is used to do a move. 
    TargetMoveAction is not used on the Mac."""


class EventPriority(QtEnumeration):
    """ This enum can be used to specify event priorities.
        Note that these values are provided purely for convenience,
        since event priorities can be any value between INT_MAX and INT_MIN, inclusive.
    """
    ...


HighEventPriority = EventPriority(1)
NormalEventPriority = EventPriority(0)
LowEventPriority = EventPriority(-1)


class FillRule(QtEnumeration):
    """ Specifies which method should be used to fill the paths and polygons.
    """
    ...


OddEvenFill = FillRule(0)
""" Specifies that the region is filled using the odd even fill rule. With this rule, 
    we determine whether a point is inside the shape by using the following method. 
    Draw a horizontal line from the point to a location outside the shape, and count the number of intersections. 
    If the number of intersections is an odd number, the point is inside the shape. This mode is the default."""
WindingFill = FillRule(1)
""" Specifies that the region is filled using the non zero winding rule. With this rule, we determine whether a point 
    is inside the shape by using the following method. Draw a horizontal line from the point to a location 
    outside the shape. Determine whether the direction of the line at each intersection point is up or down. 
    The winding number is determined by summing the direction of each intersection. If the number is non zero, 
    the point is inside the shape. This fill mode can also in most cases be considered as the intersection of 
    closed shapes."""


class FocusPolicy(QtEnumeration):
    """ This enum type defines the various policies a widget can have with respect to acquiring keyboard focus.
    """
    ...


TabFocus = FocusPolicy(0x1)
""" the widget accepts focus by tabbing."""
ClickFocus = FocusPolicy(0x2)
""" the widget accepts focus by clicking."""
StrongFocus = TabFocus | ClickFocus | FocusPolicy(0x8)
""" the widget accepts focus by both tabbing and clicking. On Mac OS X this will also be indicate that the 
    widget accepts tab focus when in 'Text/List focus mode'."""
WheelFocus = StrongFocus | FocusPolicy(0x4)
""" like Qt::StrongFocus plus the widget accepts focus by using the mouse wheel."""
NoFocus = FocusPolicy(0)
""" the widget does not accept focus."""


class FocusReason(QtEnumeration):
    """ This enum specifies why the focus changed. It will be passed through QWidget::setFocus and
        can be retrieved in the QFocusEvent sent to the widget upon focus change.
    """
    ...


MouseFocusReason = FocusReason(0)
""" A mouse action occurred."""
TabFocusReason = FocusReason(1)
""" The Tab key was pressed."""
BacktabFocusReason = FocusReason(2)
""" A Backtab occurred. The input for this may include the Shift or Control keys; e.g. Shift+Tab."""
ActiveWindowFocusReason = FocusReason(3)
""" The window system made this window either active or inactive."""
PopupFocusReason = FocusReason(4)
""" The application opened/closed a pop-up that grabbed/released the keyboard focus."""
ShortcutFocusReason = FocusReason(5)
""" The user typed a label's buddy shortcut"""
MenuBarFocusReason = FocusReason(6)
""" The menu bar took focus."""
OtherFocusReason = FocusReason(7)
""" Another reason, usually application-specific."""


class GestureFlag(QtEnumeration):
    """ This enum type describes additional flags that can be used when subscribing to a gesture.

        This enum was introduced or modified in Qt 4.6.

        The GestureFlags type is a typedef for QFlags<GestureFlag>. It stores an OR combination of GestureFlag values.
    """
    ...


DontStartGestureOnChildren = GestureFlag(0x01)
""" By default gestures can start on the widget or over any of its children. Use this flag to 
    disable this and allow a gesture to start on the widget only."""
ReceivePartialGestures = GestureFlag(0x02)
""" Allows any ignored gesture events to be propagated to parent widgets which have specified this hint. 
    By default only gestures that are in the Qt::GestureStarted state are propagated and the widget always
    gets the full gesture sequence starting with a gesture in the Qt::GestureStarted state and ending with 
    a gesture in the Qt::GestureFinished or Qt::GestureCanceled states."""
IgnoredGesturesPropagateToParent = GestureFlag(0x04)
""" Since Qt 4.7, this flag allows you to fine-tune gesture event propagation. By setting the flag when grabbing 
    a gesture all ignored partial gestures will propagate to their parent items."""


class GestureState(QtEnumeration):
    """ This enum type describes the state of a gesture.

        This enum was introduced or modified in Qt 4.6.
    """
    ...


GestureStarted = GestureState(1)
""" A continuous gesture has started."""
GestureUpdated = GestureState(2)
""" A gesture continues."""
GestureFinished = GestureState(3)
""" A gesture has finished."""
GestureCanceled = GestureState(4)
""" A gesture was canceled."""


class GestureType(QtEnumeration):
    """ This enum type describes the standard gestures.

        User-defined gestures are registered with the QGestureRecognizer::registerRecognizer() function which
        generates a custom gesture ID with the Qt::CustomGesture flag set.

        This enum was introduced or modified in Qt 4.6.
    """
    ...


TapGesture = GestureType(1)
""" A Tap gesture."""
TapAndHoldGesture = GestureType(2)
""" A Tap-And-Hold (Long-Tap) gesture."""
PanGesture = GestureType(3)
""" A Pan gesture."""
PinchGesture = GestureType(4)
""" A Pinch gesture."""
SwipeGesture = GestureType(5)
""" A Swipe gesture."""
CustomGesture = GestureType(0x0100)
""" A flag that can be used to test if the gesture is a user-defined gesture ID."""


class GlobalColor(QtEnumeration):
    """ Qt's predefined QColor objects
    """
    ...


white = GlobalColor(3)
""" White (#ffffff)"""
black = GlobalColor(2)
""" Black (#000000)"""
red = GlobalColor(7)
""" Red (#ff0000)"""
darkRed = GlobalColor(13)
""" Dark red (#800000)"""
green = GlobalColor(8)
""" Green (#00ff00)"""
darkGreen = GlobalColor(14)
""" Dark green (#008000)"""
blue = GlobalColor(9)
""" Blue (#0000ff)"""
darkBlue = GlobalColor(15)
""" Dark blue (#000080)"""
cyan = GlobalColor(10)
""" Cyan (#00ffff)"""
darkCyan = GlobalColor(16)
""" Dark cyan (#008080)"""
magenta = GlobalColor(11)
""" Magenta (#ff00ff)"""
darkMagenta = GlobalColor(17)
""" Dark magenta (#800080)"""
yellow = GlobalColor(12)
""" Yellow (#ffff00)"""
darkYellow = GlobalColor(18)
""" Dark yellow (#808000)"""
gray = GlobalColor(5)
""" Gray (#a0a0a4)"""
darkGray = GlobalColor(4)
""" Dark gray (#808080)"""
lightGray = GlobalColor(6)
""" Light gray (#c0c0c0)"""
transparent = GlobalColor(19)
""" a transparent black value (i.e., QColor(0, 0, 0, 0))"""
color0 = GlobalColor(0)
""" 0 pixel value (for bitmaps)"""
color1 = GlobalColor(1)
""" 1 pixel value (for bitmaps)"""


class HANDLE(QtEnumeration):
    """ Platform-specific handle type for system objects. This is equivalent to void * on Mac OS X and embedded Linux,
        and to unsigned long on X11. On Windows it is the DWORD returned by the Win32 function getCurrentThreadId().

        Warning: Using this type is not portable.
    """
    ...


class HitTestAccuracy(QtEnumeration):
    """ This enum contains the types of accuracy that can be used by the QTextDocument class when testing for mouse clicks on text documents.
    """
    ...


ExactHit = HitTestAccuracy(0)
""" The point at which input occurred must coincide exactly with input-sensitive parts of the document."""
FuzzyHit = HitTestAccuracy(1)
""" The point at which input occurred can lie close to input-sensitive parts of the document."""


class ImageConversionFlag(QtEnumeration):
    """ The options marked "(default)" are set if no other values from the list are included (since the defaults are zero).

        Don't do any format conversions on the image. Can be useful when converting a QImage to a QPixmap for a one-time rendering operation for example.

        The ImageConversionFlags type is a typedef for QFlags<ImageConversionFlag>. It stores an OR combination of ImageConversionFlag values.
    """
    ...

# Color/Mono Preference:
AutoColor = ImageConversionFlag(0x00000000)
""" (default) - If the image has depth 1 and contains only black and white pixels, the pixmap becomes monochrome."""
ColorOnly = ImageConversionFlag(0x00000003)
""" The pixmap is dithered/converted to the native display depth."""
MonoOnly = ImageConversionFlag(0x00000002)
""" The pixmap becomes monochrome. If necessary, it is dithered using the chosen dithering algorithm."""

# Dithering mode preference for RGB channels:
DiffuseDither = ImageConversionFlag(0x00000000)
""" (default) - A high-quality dither."""
OrderedDither = ImageConversionFlag(0x00000010)
""" A faster, more ordered dither."""
ThresholdDither = ImageConversionFlag(0x00000020)
""" No dithering; closest color is used."""

# Dithering mode preference for alpha channel:
ThresholdAlphaDither = ImageConversionFlag(0x00000000)
""" (default) - No dithering."""
OrderedAlphaDither = ImageConversionFlag(0x00000004)
""" A faster, more ordered dither."""
DiffuseAlphaDither = ImageConversionFlag(0x00000008)
""" A high-quality dither."""

# Color matching versus dithering preference:
PreferDither = ImageConversionFlag(0x00000040)
""" (default when converting to a pixmap) - Always dither 32-bit images when the image is converted to 8 bits."""
AvoidDither = ImageConversionFlag(0x00000080)
""" (default when converting for the purpose of saving to file) - Dither 32-bit images only if the image has more than 256 colors and it is being converted to 8 bits."""
NoOpaqueDetection = ImageConversionFlag(0x00000100)
""" Do not check whether the image contains non-opaque pixels. Use this if you know that the image is semi-transparent and you want to avoid the overhead of 
    checking the pixels in the image until a non-opaque pixel is found, or if you want the pixmap to retain an alpha channel for some other reason. 
    If the image has no alpha channel this flag has no effect.
"""


class InputMethodHint(QtEnumeration):
    """
        Note: If several exclusive flags are ORed together, the resulting character set will consist of the union of the specified sets.
        For instance specifying ImhNumbersOnly and ImhUppercaseOnly would yield a set consisting of numbers and uppercase letters.

        The InputMethodHints type is a typedef for QFlags<InputMethodHint>. It stores an OR combination of InputMethodHint values.
    """
    ...


ImhNone = InputMethodHint(0x0)
""" No hints."""
ImhHiddenText = InputMethodHint(0x1)
""" Characters should be hidden, as is typically used when entering passwords. This is automatically set when setting QLineEdit::echoMode to Password."""
ImhNoAutoUppercase = InputMethodHint(0x2)
""" The input method should not try to automatically switch to upper case when a sentence ends."""
ImhPreferNumbers = InputMethodHint(0x4)
""" Numbers are preferred (but not required)."""
ImhPreferUppercase = InputMethodHint(0x8)
""" Upper case letters are preferred (but not required)."""
ImhPreferLowercase = InputMethodHint(0x10)
""" Lower case letters are preferred (but not required)."""
ImhNoPredictiveText = InputMethodHint(0x20)
""" Do not use predictive text (i.e. dictionary lookup) while typing."""
ImhDigitsOnly = InputMethodHint(0x10000)
""" Only digits are allowed."""
ImhFormattedNumbersOnly = InputMethodHint(0x20000)
""" Only number input is allowed. This includes decimal point and minus sign."""
ImhUppercaseOnly = InputMethodHint(0x40000)
""" Only upper case letter input is allowed."""
ImhLowercaseOnly = InputMethodHint(0x80000)
""" Only lower case letter input is allowed."""
ImhDialableCharactersOnly = InputMethodHint(0x100000)
""" Only characters suitable for phone dialling are allowed."""
ImhEmailCharactersOnly = InputMethodHint(0x200000)
""" Only characters suitable for email addresses are allowed."""
ImhUrlCharactersOnly = InputMethodHint(0x400000)
""" Only characters suitable for URLs are allowed."""
ImhExclusiveInputMask = InputMethodHint(0xffff0000)
""" This mask yields nonzero if any of the exclusive flags are used."""


class InputMethodQuery(QtEnumeration): ...


ImMicroFocus = InputMethodQuery(0)
""" The rectangle covering the area of the input cursor in widget coordinates."""
ImFont = InputMethodQuery(1)
""" The currently used font for text input."""
ImCursorPosition = InputMethodQuery(2)
""" The logical position of the cursor within the text surrounding the input area (see ImSurroundingText)."""
ImSurroundingText = InputMethodQuery(3)
""" The plain text around the input area, for example the current paragraph."""
ImCurrentSelection = InputMethodQuery(4)
""" The currently selected text."""
ImMaximumTextLength = InputMethodQuery(5)
""" The maximum number of characters that the widget can hold. If there is no limit, QVariant() is returned."""
ImAnchorPosition = InputMethodQuery(6)
""" The position of the selection anchor. This may be less or greater than ImCursorPosition, depending on which side of selection the cursor is. 
    If there is no selection, it returns the same as ImCursorPosition.
"""


class ItemDataRole(QtEnumeration):
    """ Each item in the model has a set of data elements associated with it, each with its own role. The roles are used by the view to indicate to the model
        which type of data it needs. Custom models should return data in these types.
    """
    ...


DisplayRole = ItemDataRole(0)
""" The key data to be rendered in the form of text. (QString)"""
DecorationRole = ItemDataRole(1)
""" The data to be rendered as a decoration in the form of an icon. (QColor, QIcon or QPixmap)"""
EditRole = ItemDataRole(2)
""" The data in a form suitable for editing in an editor. (QString)"""
ToolTipRole = ItemDataRole(3)
""" The data displayed in the item's tooltip. (QString)"""
StatusTipRole = ItemDataRole(4)
""" The data displayed in the status bar. (QString)"""
WhatsThisRole = ItemDataRole(5)
""" The data displayed for the item in "What's This?" mode. (QString)"""
SizeHintRole = ItemDataRole(13)
""" The size hint for the item that will be supplied to views. (QSize)"""
FontRole = ItemDataRole(6)
""" The font used for items rendered with the default delegate. (QFont)"""
TextAlignmentRole = ItemDataRole(7)
""" The alignment of the text for items rendered with the default delegate. (Qt::AlignmentFlag)"""
BackgroundRole = ItemDataRole(8)
""" The background brush used for items rendered with the default delegate. (QBrush)"""
BackgroundColorRole = ItemDataRole(8)
""" This role is obsolete. Use BackgroundRole instead."""
ForegroundRole = ItemDataRole(9)
""" The foreground brush (text color, typically) used for items rendered with the default delegate. (QBrush)"""
TextColorRole = ItemDataRole(9)
""" This role is obsolete. Use ForegroundRole instead."""
CheckStateRole = ItemDataRole(10)
""" This role is used to obtain the checked state of an item. (Qt::CheckState)"""
InitialSortOrderRole = ItemDataRole(14)
""" This role is used to obtain the initial sort order of a header view section. (Qt::SortOrder). This role was introduced in Qt 4.8."""
AccessibleTextRole = ItemDataRole(11)
""" The text to be used by accessibility extensions and plugins, such as screen readers. (QString)"""
AccessibleDescriptionRole = ItemDataRole(12)
""" A description of the item for accessibility purposes. (QString)"""
UserRole = ItemDataRole(32)
""" The first role that can be used for application-specific purposes."""


class ItemFlag(QtEnumeration):
    """ This enum describes the properties of an item.

        Note that checkable items need to be given both a suitable set of flags and an initial state, indicating whether the item is checked or not. T
        his is handled automatically for model/view components, but needs to be explicitly set for instances of QListWidgetItem, QTableWidgetItem, and QTreeWidgetItem.

        The ItemFlags type is a typedef for QFlags<ItemFlag>. It stores an OR combination of ItemFlag values.
    """
    ...


NoItemFlags = ItemFlag(0)
""" It does not have any properties set."""
ItemIsSelectable = ItemFlag(1)
""" It can be selected."""
ItemIsEditable = ItemFlag(2)
""" It can be edited."""
ItemIsDragEnabled = ItemFlag(4)
""" It can be dragged."""
ItemIsDropEnabled = ItemFlag(8)
""" It can be used as a drop target."""
ItemIsUserCheckable = ItemFlag(16)
""" It can be checked or unchecked by the user."""
ItemIsEnabled = ItemFlag(32)
""" The user can interact with the item."""
ItemIsTristate = ItemFlag(64)
""" The item is checkable with three separate states."""


class ItemSelectionMode(QtEnumeration):
    """ This enum is used in QGraphicsItem, QGraphicsScene and QGraphicsView to specify how items are selected, or how to determine if a shapes and items collide.
    """
    ...


ContainsItemShape = ItemSelectionMode(0x0)
""" The output list contains only items whose shape is fully contained inside the selection area. Items that intersect with the area's outline are not included."""
IntersectsItemShape = ItemSelectionMode(0x1)
""" The output list contains both items whose shape is fully contained inside the selection area, and items that intersect with the area's outline. 
    This is a common mode for rubber band selection.
"""
ContainsItemBoundingRect = ItemSelectionMode(0x2)
""" The output list contains only items whose bounding rectangle is fully contained inside the selection area. 
    Items that intersect with the area's outline are not included.
"""
IntersectsItemBoundingRect = ItemSelectionMode(0x3)
""" The output list contains both items whose bounding rectangle is fully contained inside the selection area, and items that intersect with the area's outline. 
    This method is commonly used for determining areas that need redrawing.
"""


class Key(QtEnumeration):
    """ The key names used by Qt.
    """
    ...


Key_Escape = Key(0x01000000)
Key_Tab = Key(0x01000001)
Key_Backtab = Key(0x01000002)
Key_Backspace = Key(0x01000003)
Key_Return = Key(0x01000004)
Key_Enter = Key(0x01000005)

Key_Insert = Key(0x01000006)
Key_Delete = Key(0x01000007)
Key_Pause = Key(0x01000008)
Key_Print = Key(0x01000009)
Key_SysReq = Key(0x0100000a)

Key_Clear = Key(0x0100000b)
Key_ = Key(0x0100000c)
Key_ = Key(0x0100000d)
Key_ = Key(0x0100000e)
Key_ = Key(0x0100000f)

Key_ = Key(0x01000010)
Key_ = Key(0x01000011)
Key_ = Key(0x01000012)
Key_ = Key(0x01000013)
Key_ = Key(0x01000014)

Key_ = Key(0x01000015)
Key_ = Key(0x01000016)
Key_ = Key(0x01000017)
Key_ = Key(0x01000020)
Key_ = Key(0x01000021)

Key_ = Key(0x01000022)
Key_ = Key(0x01001103)
Key_ = Key(0x01000024)
Key_ = Key(0x01000025)
Key_ = Key(0x01000026)

Key_ = Key(0x01000030)
Key_ = Key(0x01000031)
Key_ = Key(0x01000032)
Key_ = Key(0x01000033)
Key_ = Key(0x01000034)

Key_ = Key(0x01000035)
Key_ = Key(0x01000036)
Key_ = Key(0x01000037)
Key_ = Key(0x01000038)
Key_ = Key(0x01000039)

Key_ = Key(0x0100003a)
Key_ = Key(0x0100003b)
Key_ = Key(0x0100003c)
Key_ = Key(0x0100003d)
Key_ = Key(0x0100003e)

Key_ = Key(0x0100003f)
Key_ = Key(0x01000040)
Key_ = Key(0x01000041)
Key_ = Key(0x01000042)
Key_ = Key(0x01000043)

Key_ = Key(0x01000044)
Key_ = Key(0x01000045)
Key_ = Key(0x01000046)
Key_ = Key(0x01000047)
Key_ = Key(0x01000048)

Key_ = Key(0x01000049)
Key_ = Key(0x0100004a)
Key_ = Key(0x0100004b)
Key_ = Key(0x0100004c)
Key_ = Key(0x0100004d)

Key_ = Key(0x0100004e)
Key_ = Key(0x0100004f)
Key_ = Key(0x01000050)
Key_ = Key(0x01000051)
Key_ = Key(0x01000052)

Key_ = Key(0x01000053)
Key_ = Key(0x01000054)
Key_ = Key(0x01000055)
Key_ = Key(0x01000056)
Key_ = Key(0x01000057)

Key_ = Key(0x01000058)
Key_ = Key(0x01000059)
Key_ = Key(0x01000060)
Key_Space = Key(0x20)
Key_Any = Key_Space

Key_ = Key(0x21)
Key_ = Key(0x22)
Key_ = Key(0x23)
Key_ = Key(0x24)
Key_ = Key(0x25)

Key_ = Key(0x26)
Key_ = Key(0x27)
Key_ = Key(0x28)
Key_ = Key(0x29)
Key_ = Key(0x2a)

Key_ = Key(0x2b)
Key_ = Key(0x2c)
Key_ = Key(0x2d)
Key_ = Key(0x2e)
Key_ = Key(0x2f)

Key_ = Key(0x30)
Key_ = Key(0x31)
Key_ = Key(0x32)
Key_ = Key(0x33)
Key_ = Key(0x34)

Key_ = Key(0x35)
Key_ = Key(0x36)
Key_ = Key(0x37)
Key_ = Key(0x38)
Key_ = Key(0x39)

Key_ = Key(0x3a)
Key_ = Key(0x3b)
Key_ = Key(0x3c)
Key_ = Key(0x3d)
Key_ = Key(0x3e)

Key_ = Key(0x3f)
Key_ = Key(0x40)
Key_ = Key(0x41)
Key_ = Key(0x42)
Key_ = Key(0x43)

Key_ = Key(0x44)
Key_ = Key(0x45)
Key_ = Key(0x46)
Key_ = Key(0x47)
Key_ = Key(0x48)

Key_ = Key(0x49)
Key_ = Key(0x4a)
Key_ = Key(0x4b)
Key_ = Key(0x4c)
Key_ = Key(0x4d)

Key_ = Key(0x4e)
Key_ = Key(0x4f)
Key_ = Key(0x50)
Key_ = Key(0x51)
Key_ = Key(0x52)

Key_ = Key(0x53)
Key_ = Key(0x54)
Key_ = Key(0x55)
Key_ = Key(0x56)
Key_ = Key(0x57)

Key_ = Key(0x58)
Key_ = Key(0x59)
Key_ = Key(0x5a)
Key_ = Key(0x5b)
Key_ = Key(0x5c)

Key_ = Key(0x5d)
Key_ = Key(0x5e)
Key_ = Key(0x5f)
Key_ = Key(0x60)
Key_ = Key(0x7b)

Key_ = Key(0x7c)
Key_ = Key(0x7d)
Key_ = Key(0x7e)
Key_ = Key(0x0a0)
Key_ = Key(0x0a1)

Key_ = Key(0x0a2)
Key_ = Key(0x0a3)
Key_ = Key(0x0a4)
Key_ = Key(0x0a5)
Key_ = Key(0x0a6)

Key_ = Key(0x0a7)
Key_ = Key(0x0a8)
Key_ = Key(0x0a9)
Key_ = Key(0x0aa)
Key_ = Key(0x0ab)

Key_ = Key(0x0ac)
Key_ = Key(0x0ad)
Key_ = Key(0x0ae)
Key_ = Key(0x0af)
Key_ = Key(0x0b0)

Key_ = Key(0x0b1)
Key_ = Key(0x0b2)
Key_ = Key(0x0b3)
Key_ = Key(0x0b4)
Key_ = Key(0x0b5)

Key_ = Key(0x0b6)
Key_ = Key(0x0b7)
Key_ = Key(0x0b8)
Key_ = Key(0x0b9)
Key_ = Key(0x0ba)

Key_ = Key(0x0bb)
Key_ = Key(0x0bc)
Key_ = Key(0x0bd)
Key_ = Key(0x0be)
Key_ = Key(0x0bf)

Key_ = Key(0x0c0)
Key_ = Key(0x0c1)
Key_ = Key(0x0c2)
Key_ = Key(0x0c3)
Key_ = Key(0x0c4)

Key_ = Key(0x0c5)
Key_ = Key(0x0c6)
Key_ = Key(0x0c7)
Key_ = Key(0x0c8)
Key_ = Key(0x0c9)

Key_ = Key(0x0ca)
Key_ = Key(0x0cb)
Key_ = Key(0x0cc)
Key_ = Key(0x0cd)
Key_ = Key(0x0ce)

Key_ = Key(0x0cf)
Key_ = Key(0x0d0)
Key_ = Key(0x0d1)
Key_ = Key(0x0d2)
Key_ = Key(0x0d3)

Key_ = Key(0x0d4)
Key_ = Key(0x0d5)
Key_ = Key(0x0d6)
Key_ = Key(0x0d7)
Key_ = Key(0x0d8)

Key_ = Key(0x0d9)
Key_ = Key(0x0da)
Key_ = Key(0x0db)
Key_ = Key(0x0dc)
Key_ = Key(0x0dd)

Key_ = Key(0x0de)
Key_ = Key(0x0df)
Key_ = Key(0x0f7)
Key_ = Key(0x0ff)
Key_ = Key(0x01001120)

Key_ = Key(0x01001120)
Key_ = Key(0x01001137)
Key_ = Key(0x0100113c)
Key_ = Key(0x0100113d)
Key_ = Key(0x0100113e)

Key_ = Key(0x0100117e)
Key_ = Key(0x01001121)
Key_ = Key(0x01001122)
Key_ = Key(0x01001123)
Key_ = Key(0x01001124)

Key_ = Key(0x01001125)
Key_ = Key(0x01001126)
Key_ = Key(0x01001127)
Key_ = Key(0x01001128)
Key_ = Key(0x01001129)

Key_ = Key(0x0100112a)
Key_ = Key(0x0100112b)
Key_ = Key(0x0100112c)
Key_ = Key(0x0100112d)
Key_ = Key(0x0100112e)

Key_ = Key(0x0100112f)
Key_ = Key(0x01001130)
Key_ = Key(0x01001131)
Key_ = Key(0x01001132)
Key_ = Key(0x01001133)

Key_ = Key(0x01001134)
Key_ = Key(0x01001135)
Key_ = Key(0x01001136)
Key_ = Key(0x01001137)
Key_ = Key(0x01001138)

Key_ = Key(0x0100113a)
Key_ = Key(0x0100113b)
Key_ = Key(0x0100113c)
Key_ = Key(0x0100113d)
Key_ = Key(0x0100113e)

Key_ = Key(0x01001250)
Key_ = Key(0x01001251)
Key_ = Key(0x01001252)
Key_ = Key(0x01001253)
Key_ = Key(0x01001254)

Key_ = Key(0x01001255)
Key_ = Key(0x01001256)
Key_ = Key(0x01001257)
Key_ = Key(0x01001258)
Key_ = Key(0x01001259)

Key_ = Key(0x0100125a)
Key_ = Key(0x0100125b)
Key_ = Key(0x0100125c)
Key_ = Key(0x0100125d)
Key_ = Key(0x0100125e)

Key_ = Key(0x0100125f)
Key_ = Key(0x01001260)
Key_ = Key(0x01001261)
Key_ = Key(0x01001262)
Key_ = Key(0x01000061)

Key_ = Key(0x01000062)
Key_ = Key(0x01000063)
Key_ = Key(0x01000064)
Key_ = Key(0x01000070)
Key_ = Key(0x01000071)

Key_ = Key(0x01000072)
Key_ = Key(0x01000074)
Key_ = Key(0x01000075)
Key_ = Key(0x01000076)
Key_ = Key(0x01000077)

Key_ = Key(0x01000080)
Key_ = Key(0x01000081)
Key_ = Key(0x01000082)
Key_ = Key(0x01000083)
Key_ = Key(0x01000084)

Key_ = Key(0x1000085)
Key_ = Key(0x1000086)
Key_ = Key(0x01000090)
Key_ = Key(0x01000091)
Key_ = Key(0x01000092)

Key_ = Key(0x01000094)
Key_ = Key(0x010000a0)
Key_ = Key(0x010000a1)
Key_ = Key(0x010000a2)
Key_ = Key(0x010000a3)

Key_ = Key(0x01000094)
Key_ = Key(0x010000a0)
Key_ = Key(0x010000a1)
Key_ = Key(0x010000a2)
Key_ = Key(0x010000a3)

Key_ = Key(0x010000a4)
Key_ = Key(0x010000a5)
Key_ = Key(0x010000a6)
Key_ = Key(0x010000a7)
Key_ = Key(0x010000a8)

Key_ = Key(0x010000a9)
Key_ = Key(0x010000aa)
Key_ = Key(0x010000ab)
Key_ = Key(0x010000ac)
Key_ = Key(0x010000ad)

Key_ = Key(0x010000ae)
Key_ = Key(0x010000af)
Key_ = Key(0x010000b0)
Key_ = Key(0x010000b1)
Key_ = Key(0x0100000e)

Key_ = Key(0x0100000f)
Key_ = Key(0x010000b2)
Key_ = Key(0x010000b3)
Key_ = Key(0x010000b4)
Key_ = Key(0x010000b5)

Key_ = Key(0x010000b6)
Key_ = Key(0x010000b7)
Key_ = Key(0x010000b8)
Key_ = Key(0x010000b9)
Key_ = Key(0x010000ba)

Key_ = Key(0x010000bb)
Key_ = Key(0x010000bc)
Key_ = Key(0x010000bd)
Key_ = Key(0x010000be)
Key_ = Key(0x010000bf)

Key_ = Key(0x010000c0)
Key_ = Key(0x010000c1)
Key_ = Key(0x010000c2)
Key_ = Key(0x010000c3)
Key_ = Key(0x010000c4)

Key_ = Key(0x010000c5)
Key_ = Key(0x010000c6)
Key_ = Key(0x010000c7)
Key_ = Key(0x010000c8)
Key_ = Key(0x010000c9)

Key_ = Key(0x010000ca)
Key_ = Key(0x010000cb)
Key_ = Key(0x010000cc)
Key_ = Key(0x010000cd)
Key_ = Key(0x010000ce)

Key_ = Key(0x010000cf)
Key_ = Key(0x010000d0)
Key_ = Key(0x010000d1)
Key_ = Key(0x010000d2)
Key_ = Key(0x010000d3)

Key_ = Key(0x010000d4)
Key_ = Key(0x010000d5)
Key_ = Key(0x010000d6)
Key_ = Key(0x010000d7)
Key_ = Key(0x010000d8)

Key_ = Key(0x010000d9)
Key_ = Key(0x010000da)
Key_ = Key(0x010000db)
Key_ = Key(0x010000dc)
Key_ = Key(0x010000dd)

Key_ = Key(0x010000de)
Key_ = Key(0x010000df)
Key_ = Key(0x010000e0)
Key_ = Key(0x010000e1)
Key_ = Key(0x010000e2)

Key_ = Key(0x010000e3)
Key_ = Key(0x010000e4)
Key_ = Key(0x010000e5)
Key_ = Key(0x010000e6)
Key_ = Key(0x010000e7)

Key_ = Key(0x010000e8)
Key_ = Key(0x010000e9)
Key_ = Key(0x010000ea)
Key_ = Key(0x010000eb)
Key_ = Key(0x010000ec)

Key_ = Key(0x010000ed)
Key_ = Key(0x010000ee)
Key_ = Key(0x010000ef)
Key_ = Key(0x010000f0)
Key_ = Key(0x010000f1)

Key_ = Key(0x010000f2)
Key_ = Key(0x010000f3)
Key_ = Key(0x010000f4)
Key_ = Key(0x010000f5)
Key_ = Key(0x010000f6)

Key_ = Key(0x010000f7)
Key_ = Key(0x010000f8)
Key_ = Key(0x010000f9)
Key_ = Key(0x010000fa)
Key_ = Key(0x010000fb)

Key_ = Key(0x010000fc)
Key_ = Key(0x010000fd)
Key_ = Key(0x010000fe)
Key_ = Key(0x010000ff)
Key_ = Key(0x01000100)

Key_ = Key(0x01000101)
Key_ = Key(0x01000102)
Key_ = Key(0x01000103)
Key_ = Key(0x01000104)
Key_ = Key(0x01000105)

Key_ = Key(0x01000106)
Key_ = Key(0x01000107)
Key_ = Key(0x01000108)
Key_ = Key(0x01000109)
Key_ = Key(0x0100010a)

Key_ = Key(0x0100010b)
Key_ = Key(0x0100010c)
Key_ = Key(0x0100010d)
Key_ = Key(0x0100ffff)
Key_ = Key(0x01ffffff)

Key_ = Key(0x01100004)
Key_ = Key(0x01100020)
Key_ = Key(0x01100021)
Key_ = Key(0x01100000)
Key_ = Key(0x01100001)

Key_ = Key(0x01100002)
Key_ = Key(0x01100003)
Key_ = Key(0x01100004)
Key_ = Key(0x01100005)
Key_ = Key(0x01010002)

Key_ = Key(0x01010000)
Key_ = Key(0x01010001)
Key_ = Key(0x01100007)
Key_ = Key(0x01100008)
Key_ = Key(0x01100009)

Key_ = Key(0x01020003)
Key_ = Key(0x01020002)
Key_ = Key(0x01020005)
Key_ = Key(0x01020004)
Key_ = Key(0x01020006)

Key_ = Key(0x01020001)