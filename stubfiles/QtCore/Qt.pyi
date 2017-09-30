

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


