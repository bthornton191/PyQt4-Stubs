# encoding: utf-8
# module PyQt4.QtMultimedia
# from C:\Python27\lib\site-packages\PyQt4\QtMultimedia.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QAbstractVideoBuffer(): # skipped bases: <type 'sip.simplewrapper'>
    """ QAbstractVideoBuffer(QAbstractVideoBuffer.HandleType) """
    def handle(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoBuffer.handle() -> QVariant """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoBuffer.handleType() -> QAbstractVideoBuffer.HandleType """
        pass

    def map(self, QAbstractVideoBuffer_MapMode): # real signature unknown; restored from __doc__
        """ QAbstractVideoBuffer.map(QAbstractVideoBuffer.MapMode) -> (sip.voidptr, int, int) """
        pass

    def mapMode(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoBuffer.mapMode() -> QAbstractVideoBuffer.MapMode """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoBuffer.unmap() """
        pass

    def __init__(self, QAbstractVideoBuffer_HandleType): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CoreImageHandle = 3
    GLTextureHandle = 1
    NoHandle = 0
    NotMapped = 0
    QPixmapHandle = 4
    ReadOnly = 1
    ReadWrite = 3
    UserHandle = 1000
    WriteOnly = 2
    XvShmImageHandle = 2


class QAbstractVideoSurface(__PyQt4_QtCore.QObject):
    """ QAbstractVideoSurface(QObject parent=None) """
    def activeChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractVideoSurface.activeChanged[bool] [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.error() -> QAbstractVideoSurface.Error """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.isActive() -> bool """
        return False

    def isFormatSupported(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.isFormatSupported(QVideoSurfaceFormat) -> bool """
        return False

    def nearestFormat(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.nearestFormat(QVideoSurfaceFormat) -> QVideoSurfaceFormat """
        return QVideoSurfaceFormat

    def present(self, QVideoFrame): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.present(QVideoFrame) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, QAbstractVideoSurface_Error): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.setError(QAbstractVideoSurface.Error) """
        pass

    def start(self, QVideoSurfaceFormat): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.start(QVideoSurfaceFormat) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.stop() """
        pass

    def supportedFormatsChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractVideoSurface.supportedFormatsChanged [signal] """
        pass

    def supportedPixelFormats(self, QAbstractVideoBuffer_HandleType_type=None): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.supportedPixelFormats(QAbstractVideoBuffer.HandleType type=QAbstractVideoBuffer.NoHandle) -> list-of-QVideoFrame.PixelFormat """
        pass

    def surfaceFormat(self): # real signature unknown; restored from __doc__
        """ QAbstractVideoSurface.surfaceFormat() -> QVideoSurfaceFormat """
        return QVideoSurfaceFormat

    def surfaceFormatChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractVideoSurface.surfaceFormatChanged[QVideoSurfaceFormat] [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    IncorrectFormatError = 2
    NoError = 0
    ResourceError = 4
    StoppedError = 3
    UnsupportedFormatError = 1


class QAudio(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ActiveState = 0
    AudioInput = 0
    AudioOutput = 1
    FatalError = 4
    IdleState = 3
    IOError = 2
    NoError = 0
    OpenError = 1
    StoppedState = 2
    SuspendedState = 1
    UnderrunError = 3


class QAudioDeviceInfo(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QAudioDeviceInfo()
    QAudioDeviceInfo(QAudioDeviceInfo)
    """
    def availableDevices(self, QAudio_Mode): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.availableDevices(QAudio.Mode) -> list-of-QAudioDeviceInfo """
        pass

    def defaultInputDevice(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.defaultInputDevice() -> QAudioDeviceInfo """
        return QAudioDeviceInfo

    def defaultOutputDevice(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.defaultOutputDevice() -> QAudioDeviceInfo """
        return QAudioDeviceInfo

    def deviceName(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.deviceName() -> QString """
        pass

    def isFormatSupported(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.isFormatSupported(QAudioFormat) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.isNull() -> bool """
        return False

    def nearestFormat(self, QAudioFormat): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.nearestFormat(QAudioFormat) -> QAudioFormat """
        return QAudioFormat

    def preferredFormat(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.preferredFormat() -> QAudioFormat """
        return QAudioFormat

    def supportedByteOrders(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedByteOrders() -> list-of-QAudioFormat.Endian """
        pass

    def supportedChannelCounts(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedChannelCounts() -> list-of-int """
        pass

    def supportedChannels(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedChannels() -> list-of-int """
        pass

    def supportedCodecs(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedCodecs() -> QStringList """
        pass

    def supportedFrequencies(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedFrequencies() -> list-of-int """
        pass

    def supportedSampleRates(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedSampleRates() -> list-of-int """
        pass

    def supportedSampleSizes(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedSampleSizes() -> list-of-int """
        pass

    def supportedSampleTypes(self): # real signature unknown; restored from __doc__
        """ QAudioDeviceInfo.supportedSampleTypes() -> list-of-QAudioFormat.SampleType """
        pass

    def __init__(self, QAudioDeviceInfo=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QAudioFormat(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QAudioFormat()
    QAudioFormat(QAudioFormat)
    """
    def byteOrder(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.byteOrder() -> QAudioFormat.Endian """
        pass

    def channelCount(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.channelCount() -> int """
        return 0

    def channels(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.channels() -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.codec() -> QString """
        pass

    def frequency(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.frequency() -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.isValid() -> bool """
        return False

    def sampleRate(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.sampleRate() -> int """
        return 0

    def sampleSize(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.sampleSize() -> int """
        return 0

    def sampleType(self): # real signature unknown; restored from __doc__
        """ QAudioFormat.sampleType() -> QAudioFormat.SampleType """
        pass

    def setByteOrder(self, QAudioFormat_Endian): # real signature unknown; restored from __doc__
        """ QAudioFormat.setByteOrder(QAudioFormat.Endian) """
        pass

    def setChannelCount(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioFormat.setChannelCount(int) """
        pass

    def setChannels(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioFormat.setChannels(int) """
        pass

    def setCodec(self, QString): # real signature unknown; restored from __doc__
        """ QAudioFormat.setCodec(QString) """
        pass

    def setFrequency(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioFormat.setFrequency(int) """
        pass

    def setSampleRate(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioFormat.setSampleRate(int) """
        pass

    def setSampleSize(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioFormat.setSampleSize(int) """
        pass

    def setSampleType(self, QAudioFormat_SampleType): # real signature unknown; restored from __doc__
        """ QAudioFormat.setSampleType(QAudioFormat.SampleType) """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, QAudioFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BigEndian = 0
    Float = 3
    LittleEndian = 1
    SignedInt = 1
    Unknown = 0
    UnSignedInt = 2


class QAudioInput(__PyQt4_QtCore.QObject):
    """
    QAudioInput(QAudioFormat format=QAudioFormat(), QObject parent=None)
    QAudioInput(QAudioDeviceInfo, QAudioFormat format=QAudioFormat(), QObject parent=None)
    """
    def bufferSize(self): # real signature unknown; restored from __doc__
        """ QAudioInput.bufferSize() -> int """
        return 0

    def bytesReady(self): # real signature unknown; restored from __doc__
        """ QAudioInput.bytesReady() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self): # real signature unknown; restored from __doc__
        """ QAudioInput.elapsedUSecs() -> int """
        return 0

    def error(self): # real signature unknown; restored from __doc__
        """ QAudioInput.error() -> QAudio.Error """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QAudioInput.format() -> QAudioFormat """
        return QAudioFormat

    def notify(self, *args, **kwargs): # real signature unknown
        """ QAudioInput.notify [signal] """
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ QAudioInput.notifyInterval() -> int """
        return 0

    def periodSize(self): # real signature unknown; restored from __doc__
        """ QAudioInput.periodSize() -> int """
        return 0

    def processedUSecs(self): # real signature unknown; restored from __doc__
        """ QAudioInput.processedUSecs() -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QAudioInput.reset() """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ QAudioInput.resume() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioInput.setBufferSize(int) """
        pass

    def setNotifyInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioInput.setNotifyInterval(int) """
        pass

    def start(self, QIODevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAudioInput.start(QIODevice)
        QAudioInput.start() -> QIODevice
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QAudioInput.state() -> QAudio.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QAudioInput.stateChanged[QAudio.State] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QAudioInput.stop() """
        pass

    def suspend(self): # real signature unknown; restored from __doc__
        """ QAudioInput.suspend() """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QAudioOutput(__PyQt4_QtCore.QObject):
    """
    QAudioOutput(QAudioFormat format=QAudioFormat(), QObject parent=None)
    QAudioOutput(QAudioDeviceInfo, QAudioFormat format=QAudioFormat(), QObject parent=None)
    """
    def bufferSize(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.bufferSize() -> int """
        return 0

    def bytesFree(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.bytesFree() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def elapsedUSecs(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.elapsedUSecs() -> int """
        return 0

    def error(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.error() -> QAudio.Error """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.format() -> QAudioFormat """
        return QAudioFormat

    def notify(self, *args, **kwargs): # real signature unknown
        """ QAudioOutput.notify [signal] """
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.notifyInterval() -> int """
        return 0

    def periodSize(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.periodSize() -> int """
        return 0

    def processedUSecs(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.processedUSecs() -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.reset() """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.resume() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioOutput.setBufferSize(int) """
        pass

    def setNotifyInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QAudioOutput.setNotifyInterval(int) """
        pass

    def start(self, QIODevice=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QAudioOutput.start(QIODevice)
        QAudioOutput.start() -> QIODevice
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.state() -> QAudio.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QAudioOutput.stateChanged[QAudio.State] [signal] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.stop() """
        pass

    def suspend(self): # real signature unknown; restored from __doc__
        """ QAudioOutput.suspend() """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QVideoFrame(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QVideoFrame()
    QVideoFrame(QAbstractVideoBuffer, QSize, QVideoFrame.PixelFormat)
    QVideoFrame(int, QSize, int, QVideoFrame.PixelFormat)
    QVideoFrame(QImage)
    QVideoFrame(QVideoFrame)
    """
    def bits(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.bits() -> sip.voidptr """
        pass

    def bytesPerLine(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.bytesPerLine() -> int """
        return 0

    def endTime(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.endTime() -> int """
        return 0

    def fieldType(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.fieldType() -> QVideoFrame.FieldType """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.handle() -> QVariant """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.handleType() -> QAbstractVideoBuffer.HandleType """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.height() -> int """
        return 0

    def imageFormatFromPixelFormat(self, QVideoFrame_PixelFormat): # real signature unknown; restored from __doc__
        """ QVideoFrame.imageFormatFromPixelFormat(QVideoFrame.PixelFormat) -> QImage.Format """
        pass

    def isMapped(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.isMapped() -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.isReadable() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.isValid() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.isWritable() -> bool """
        return False

    def map(self, QAbstractVideoBuffer_MapMode): # real signature unknown; restored from __doc__
        """ QVideoFrame.map(QAbstractVideoBuffer.MapMode) -> bool """
        return False

    def mapMode(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.mapMode() -> QAbstractVideoBuffer.MapMode """
        pass

    def mappedBytes(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.mappedBytes() -> int """
        return 0

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.pixelFormat() -> QVideoFrame.PixelFormat """
        pass

    def pixelFormatFromImageFormat(self, QImage_Format): # real signature unknown; restored from __doc__
        """ QVideoFrame.pixelFormatFromImageFormat(QImage.Format) -> QVideoFrame.PixelFormat """
        pass

    def setEndTime(self, p_int): # real signature unknown; restored from __doc__
        """ QVideoFrame.setEndTime(int) """
        pass

    def setFieldType(self, QVideoFrame_FieldType): # real signature unknown; restored from __doc__
        """ QVideoFrame.setFieldType(QVideoFrame.FieldType) """
        pass

    def setStartTime(self, p_int): # real signature unknown; restored from __doc__
        """ QVideoFrame.setStartTime(int) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.size() -> QSize """
        pass

    def startTime(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.startTime() -> int """
        return 0

    def unmap(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.unmap() """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ QVideoFrame.width() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BottomField = 2
    Format_ARGB32 = 1
    Format_ARGB32_Premultiplied = 2
    Format_ARGB8565_Premultiplied = 7
    Format_AYUV444 = 15
    Format_AYUV444_Premultiplied = 16
    Format_BGR24 = 11
    Format_BGR32 = 10
    Format_BGR555 = 13
    Format_BGR565 = 12
    Format_BGRA32 = 8
    Format_BGRA32_Premultiplied = 9
    Format_BGRA5658_Premultiplied = 14
    Format_IMC1 = 24
    Format_IMC2 = 25
    Format_IMC3 = 26
    Format_IMC4 = 27
    Format_Invalid = 0
    Format_NV12 = 22
    Format_NV21 = 23
    Format_RGB24 = 4
    Format_RGB32 = 3
    Format_RGB555 = 6
    Format_RGB565 = 5
    Format_User = 1000
    Format_UYVY = 20
    Format_Y16 = 29
    Format_Y8 = 28
    Format_YUV420P = 18
    Format_YUV444 = 17
    Format_YUYV = 21
    Format_YV12 = 19
    InterlacedFrame = 3
    ProgressiveFrame = 0
    TopField = 1


class QVideoSurfaceFormat(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QVideoSurfaceFormat()
    QVideoSurfaceFormat(QSize, QVideoFrame.PixelFormat, QAbstractVideoBuffer.HandleType type=QAbstractVideoBuffer.NoHandle)
    QVideoSurfaceFormat(QVideoSurfaceFormat)
    """
    def frameHeight(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.frameHeight() -> int """
        return 0

    def frameRate(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.frameRate() -> float """
        return 0.0

    def frameSize(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.frameSize() -> QSize """
        pass

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.frameWidth() -> int """
        return 0

    def handleType(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.handleType() -> QAbstractVideoBuffer.HandleType """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.isValid() -> bool """
        return False

    def pixelAspectRatio(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.pixelAspectRatio() -> QSize """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.pixelFormat() -> QVideoFrame.PixelFormat """
        pass

    def property(self, p_str): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.property(str) -> QVariant """
        pass

    def propertyNames(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.propertyNames() -> list-of-QByteArray """
        pass

    def scanLineDirection(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.scanLineDirection() -> QVideoSurfaceFormat.Direction """
        pass

    def setFrameRate(self, p_float): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.setFrameRate(float) """
        pass

    def setFrameSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QVideoSurfaceFormat.setFrameSize(QSize)
        QVideoSurfaceFormat.setFrameSize(int, int)
        """
        pass

    def setPixelAspectRatio(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QVideoSurfaceFormat.setPixelAspectRatio(QSize)
        QVideoSurfaceFormat.setPixelAspectRatio(int, int)
        """
        pass

    def setProperty(self, p_str, QVariant): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.setProperty(str, QVariant) """
        pass

    def setScanLineDirection(self, QVideoSurfaceFormat_Direction): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.setScanLineDirection(QVideoSurfaceFormat.Direction) """
        pass

    def setViewport(self, QRect): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.setViewport(QRect) """
        pass

    def setYCbCrColorSpace(self, QVideoSurfaceFormat_YCbCrColorSpace): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.setYCbCrColorSpace(QVideoSurfaceFormat.YCbCrColorSpace) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.sizeHint() -> QSize """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.viewport() -> QRect """
        pass

    def yCbCrColorSpace(self): # real signature unknown; restored from __doc__
        """ QVideoSurfaceFormat.yCbCrColorSpace() -> QVideoSurfaceFormat.YCbCrColorSpace """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BottomToTop = 1
    TopToBottom = 0
    YCbCr_BT601 = 1
    YCbCr_BT709 = 2
    YCbCr_JPEG = 5
    YCbCr_Undefined = 0
    YCbCr_xvYCC601 = 3
    YCbCr_xvYCC709 = 4


