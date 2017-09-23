# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QMessageBox(QDialog):
    """
    QMessageBox(QWidget parent=None)
    QMessageBox(QMessageBox.Icon, QString, QString, QMessageBox.StandardButtons buttons=QMessageBox.NoButton, QWidget parent=None, Qt.WindowFlags flags=Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
    QMessageBox(QString, QString, QMessageBox.Icon, int, int, int, QWidget parent=None, Qt.WindowFlags flags=Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
    """
    def about(self, QWidget, QString, QString_1): # real signature unknown; restored from __doc__
        """ QMessageBox.about(QWidget, QString, QString) """
        pass

    def aboutQt(self, QWidget, QString_title=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QMessageBox.aboutQt(QWidget, QString title=QString()) """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.addButton(QAbstractButton, QMessageBox.ButtonRole)
        QMessageBox.addButton(QString, QMessageBox.ButtonRole) -> QPushButton
        QMessageBox.addButton(QMessageBox.StandardButton) -> QPushButton
        """
        return QPushButton

    def button(self, QMessageBox_StandardButton): # real signature unknown; restored from __doc__
        """ QMessageBox.button(QMessageBox.StandardButton) -> QAbstractButton """
        return QAbstractButton

    def buttonClicked(self, *args, **kwargs): # real signature unknown
        """ QMessageBox.buttonClicked[QAbstractButton] [signal] """
        pass

    def buttonRole(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QMessageBox.buttonRole(QAbstractButton) -> QMessageBox.ButtonRole """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ QMessageBox.buttons() -> list-of-QAbstractButton """
        pass

    def buttonText(self, p_int): # real signature unknown; restored from __doc__
        """ QMessageBox.buttonText(int) -> QString """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.changeEvent(QEvent) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clickedButton(self): # real signature unknown; restored from __doc__
        """ QMessageBox.clickedButton() -> QAbstractButton """
        return QAbstractButton

    def closeEvent(self, QCloseEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.closeEvent(QCloseEvent) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def critical(self, QWidget, QString, QString_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.critical(QWidget, QString, QString, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.critical(QWidget, QString, QString, int, int, int button2=0) -> int
        QMessageBox.critical(QWidget, QString, QString, QString, QString button1Text=QString(), QString button2Text=QString(), int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultButton(self): # real signature unknown; restored from __doc__
        """ QMessageBox.defaultButton() -> QPushButton """
        return QPushButton

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def detailedText(self): # real signature unknown; restored from __doc__
        """ QMessageBox.detailedText() -> QString """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def escapeButton(self): # real signature unknown; restored from __doc__
        """ QMessageBox.escapeButton() -> QAbstractButton """
        return QAbstractButton

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.event(QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QMessageBox.icon() -> QMessageBox.Icon """
        pass

    def iconPixmap(self): # real signature unknown; restored from __doc__
        """ QMessageBox.iconPixmap() -> QPixmap """
        return QPixmap

    def information(self, QWidget, QString, QString_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.information(QWidget, QString, QString, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.information(QWidget, QString, QString, int, int button1=0, int button2=0) -> int
        QMessageBox.information(QWidget, QString, QString, QString, QString button1Text=QString(), QString button2Text=QString(), int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def informativeText(self): # real signature unknown; restored from __doc__
        """ QMessageBox.informativeText() -> QString """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.open()
        QMessageBox.open(QObject, SLOT())
        QMessageBox.open(callable)
        """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def question(self, QWidget, QString, QString_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.question(QWidget, QString, QString, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.question(QWidget, QString, QString, int, int button1=0, int button2=0) -> int
        QMessageBox.question(QWidget, QString, QString, QString, QString button1Text=QString(), QString button2Text=QString(), int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QMessageBox.removeButton(QAbstractButton) """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.resizeEvent(QResizeEvent) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButtonText(self, p_int, QString): # real signature unknown; restored from __doc__
        """ QMessageBox.setButtonText(int, QString) """
        pass

    def setDefaultButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.setDefaultButton(QPushButton)
        QMessageBox.setDefaultButton(QMessageBox.StandardButton)
        """
        pass

    def setDetailedText(self, QString): # real signature unknown; restored from __doc__
        """ QMessageBox.setDetailedText(QString) """
        pass

    def setEscapeButton(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.setEscapeButton(QAbstractButton)
        QMessageBox.setEscapeButton(QMessageBox.StandardButton)
        """
        pass

    def setIcon(self, QMessageBox_Icon): # real signature unknown; restored from __doc__
        """ QMessageBox.setIcon(QMessageBox.Icon) """
        pass

    def setIconPixmap(self, QPixmap): # real signature unknown; restored from __doc__
        """ QMessageBox.setIconPixmap(QPixmap) """
        pass

    def setInformativeText(self, QString): # real signature unknown; restored from __doc__
        """ QMessageBox.setInformativeText(QString) """
        pass

    def setStandardButtons(self, QMessageBox_StandardButtons): # real signature unknown; restored from __doc__
        """ QMessageBox.setStandardButtons(QMessageBox.StandardButtons) """
        pass

    def setText(self, QString): # real signature unknown; restored from __doc__
        """ QMessageBox.setText(QString) """
        pass

    def setTextFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ QMessageBox.setTextFormat(Qt.TextFormat) """
        pass

    def setWindowModality(self, Qt_WindowModality): # real signature unknown; restored from __doc__
        """ QMessageBox.setWindowModality(Qt.WindowModality) """
        pass

    def setWindowTitle(self, QString): # real signature unknown; restored from __doc__
        """ QMessageBox.setWindowTitle(QString) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QMessageBox.showEvent(QShowEvent) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QMessageBox.sizeHint() -> QSize """
        pass

    def standardButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QMessageBox.standardButton(QAbstractButton) -> QMessageBox.StandardButton """
        pass

    def standardButtons(self): # real signature unknown; restored from __doc__
        """ QMessageBox.standardButtons() -> QMessageBox.StandardButtons """
        pass

    def standardIcon(self, QMessageBox_Icon): # real signature unknown; restored from __doc__
        """ QMessageBox.standardIcon(QMessageBox.Icon) -> QPixmap """
        return QPixmap

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QMessageBox.text() -> QString """
        pass

    def textFormat(self): # real signature unknown; restored from __doc__
        """ QMessageBox.textFormat() -> Qt.TextFormat """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def warning(self, QWidget, QString, QString_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMessageBox.warning(QWidget, QString, QString, QMessageBox.StandardButtons buttons=QMessageBox.Ok, QMessageBox.StandardButton defaultButton=QMessageBox.NoButton) -> QMessageBox.StandardButton
        QMessageBox.warning(QWidget, QString, QString, int, int, int button2=0) -> int
        QMessageBox.warning(QWidget, QString, QString, QString, QString button1Text=QString(), QString button2Text=QString(), int defaultButtonNumber=0, int escapeButtonNumber=-1) -> int
        """
        return 0

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Abort = 262144
    AcceptRole = 0
    ActionRole = 3
    Apply = 33554432
    ApplyRole = 8
    ButtonMask = -769
    Cancel = 4194304
    Close = 2097152
    Critical = 3
    Default = 256
    DestructiveRole = 2
    Discard = 8388608
    Escape = 512
    FirstButton = 1024
    FlagMask = 768
    Help = 16777216
    HelpRole = 4
    Ignore = 1048576
    Information = 1
    InvalidRole = -1
    LastButton = 134217728
    No = 65536
    NoAll = 131072
    NoButton = 0
    NoIcon = 0
    NoRole = 6
    NoToAll = 131072
    Ok = 1024
    Open = 8192
    Question = 4
    RejectRole = 1
    Reset = 67108864
    ResetRole = 7
    RestoreDefaults = 134217728
    Retry = 524288
    Save = 2048
    SaveAll = 4096
    Warning = 2
    Yes = 16384
    YesAll = 32768
    YesRole = 5
    YesToAll = 32768


