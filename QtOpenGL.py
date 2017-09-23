# encoding: utf-8
# module PyQt4.QtOpenGL
# from C:\Python27\lib\site-packages\PyQt4\QtOpenGL.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QGL(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def setPreferredPaintEngine(self, QPaintEngine_Type): # real signature unknown; restored from __doc__
        """ QGL.setPreferredPaintEngine(QPaintEngine.Type) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccumBuffer = 16
    AlphaChannel = 8
    ColorIndex = 262144
    DeprecatedFunctions = 1024
    DepthBuffer = 2
    DirectRendering = 128
    DoubleBuffer = 1
    HasOverlay = 256
    IndirectRendering = 8388608
    NoAccumBuffer = 1048576
    NoAlphaChannel = 524288
    NoDeprecatedFunctions = 67108864
    NoDepthBuffer = 131072
    NoOverlay = 16777216
    NoSampleBuffers = 33554432
    NoStencilBuffer = 2097152
    NoStereoBuffers = 4194304
    Rgba = 4
    SampleBuffers = 512
    SingleBuffer = 65536
    StencilBuffer = 32
    StereoBuffers = 64


class QGLBuffer(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QGLBuffer()
    QGLBuffer(QGLBuffer.Type)
    QGLBuffer(QGLBuffer)
    """
    def allocate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLBuffer.allocate(sip.voidptr, int)
        QGLBuffer.allocate(int)
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.bind() -> bool """
        return False

    def bufferId(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.bufferId() -> int """
        return 0

    def create(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.create() -> bool """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.destroy() """
        pass

    def isCreated(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.isCreated() -> bool """
        return False

    def map(self, QGLBuffer_Access): # real signature unknown; restored from __doc__
        """ QGLBuffer.map(QGLBuffer.Access) -> sip.voidptr """
        pass

    def read(self, p_int, sip_voidptr, p_int_1): # real signature unknown; restored from __doc__
        """ QGLBuffer.read(int, sip.voidptr, int) -> bool """
        return False

    def release(self, QGLBuffer_Type=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLBuffer.release()
        QGLBuffer.release(QGLBuffer.Type)
        """
        pass

    def setUsagePattern(self, QGLBuffer_UsagePattern): # real signature unknown; restored from __doc__
        """ QGLBuffer.setUsagePattern(QGLBuffer.UsagePattern) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.size() -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.type() -> QGLBuffer.Type """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.unmap() -> bool """
        return False

    def usagePattern(self): # real signature unknown; restored from __doc__
        """ QGLBuffer.usagePattern() -> QGLBuffer.UsagePattern """
        pass

    def write(self, p_int, sip_voidptr, p_int_1): # real signature unknown; restored from __doc__
        """ QGLBuffer.write(int, sip.voidptr, int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DynamicCopy = 35050
    DynamicDraw = 35048
    DynamicRead = 35049
    IndexBuffer = 34963
    PixelPackBuffer = 35051
    PixelUnpackBuffer = 35052
    ReadOnly = 35000
    ReadWrite = 35002
    StaticCopy = 35046
    StaticDraw = 35044
    StaticRead = 35045
    StreamCopy = 35042
    StreamDraw = 35040
    StreamRead = 35041
    VertexBuffer = 34962
    WriteOnly = 35001


class QGLColormap(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QGLColormap()
    QGLColormap(QGLColormap)
    """
    def detach(self): # real signature unknown; restored from __doc__
        """ QGLColormap.detach() """
        pass

    def entryColor(self, p_int): # real signature unknown; restored from __doc__
        """ QGLColormap.entryColor(int) -> QColor """
        pass

    def entryRgb(self, p_int): # real signature unknown; restored from __doc__
        """ QGLColormap.entryRgb(int) -> int """
        return 0

    def find(self, p_int): # real signature unknown; restored from __doc__
        """ QGLColormap.find(int) -> int """
        return 0

    def findNearest(self, p_int): # real signature unknown; restored from __doc__
        """ QGLColormap.findNearest(int) -> int """
        return 0

    def handle(self): # real signature unknown; restored from __doc__
        """ QGLColormap.handle() -> sip.voidptr """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QGLColormap.isEmpty() -> bool """
        return False

    def setEntries(self, list_of_int, int_base=0): # real signature unknown; restored from __doc__
        """ QGLColormap.setEntries(list-of-int, int base=0) """
        pass

    def setEntry(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLColormap.setEntry(int, int)
        QGLColormap.setEntry(int, QColor)
        """
        pass

    def setHandle(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QGLColormap.setHandle(sip.voidptr) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QGLColormap.size() -> int """
        return 0

    def __init__(self, QGLColormap=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QGLContext(): # skipped bases: <type 'sip.wrapper'>
    """ QGLContext(QGLFormat, QPaintDevice) """
    def areSharing(self, QGLContext, QGLContext_1): # real signature unknown; restored from __doc__
        """ QGLContext.areSharing(QGLContext, QGLContext) -> bool """
        return False

    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLContext.bindTexture(QImage, int target=GL_TEXTURE_2D, int format=GL_RGBA) -> int
        QGLContext.bindTexture(QPixmap, int target=GL_TEXTURE_2D, int format=GL_RGBA) -> int
        QGLContext.bindTexture(QString) -> int
        QGLContext.bindTexture(QImage, int, int, QGLContext.BindOptions) -> int
        QGLContext.bindTexture(QPixmap, int, int, QGLContext.BindOptions) -> int
        """
        return 0

    def chooseContext(self, QGLContext_shareContext=None): # real signature unknown; restored from __doc__
        """ QGLContext.chooseContext(QGLContext shareContext=None) -> bool """
        return False

    def create(self, QGLContext_shareContext=None): # real signature unknown; restored from __doc__
        """ QGLContext.create(QGLContext shareContext=None) -> bool """
        return False

    def currentContext(self): # real signature unknown; restored from __doc__
        """ QGLContext.currentContext() -> QGLContext """
        return QGLContext

    def deleteTexture(self, p_int): # real signature unknown; restored from __doc__
        """ QGLContext.deleteTexture(int) """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ QGLContext.device() -> QPaintDevice """
        pass

    def deviceIsPixmap(self): # real signature unknown; restored from __doc__
        """ QGLContext.deviceIsPixmap() -> bool """
        return False

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ QGLContext.doneCurrent() """
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLContext.drawTexture(QRectF, int, int textureTarget=GL_TEXTURE_2D)
        QGLContext.drawTexture(QPointF, int, int textureTarget=GL_TEXTURE_2D)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QGLContext.format() -> QGLFormat """
        return QGLFormat

    def generateFontDisplayLists(self, QFont, p_int): # real signature unknown; restored from __doc__
        """ QGLContext.generateFontDisplayLists(QFont, int) """
        pass

    def getProcAddress(self, QString): # real signature unknown; restored from __doc__
        """ QGLContext.getProcAddress(QString) -> sip.voidptr """
        pass

    def initialized(self): # real signature unknown; restored from __doc__
        """ QGLContext.initialized() -> bool """
        return False

    def isSharing(self): # real signature unknown; restored from __doc__
        """ QGLContext.isSharing() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QGLContext.isValid() -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ QGLContext.makeCurrent() """
        pass

    def overlayTransparentColor(self): # real signature unknown; restored from __doc__
        """ QGLContext.overlayTransparentColor() -> QColor """
        pass

    def requestedFormat(self): # real signature unknown; restored from __doc__
        """ QGLContext.requestedFormat() -> QGLFormat """
        return QGLFormat

    def reset(self): # real signature unknown; restored from __doc__
        """ QGLContext.reset() """
        pass

    def setFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ QGLContext.setFormat(QGLFormat) """
        pass

    def setInitialized(self, bool): # real signature unknown; restored from __doc__
        """ QGLContext.setInitialized(bool) """
        pass

    def setTextureCacheLimit(self, p_int): # real signature unknown; restored from __doc__
        """ QGLContext.setTextureCacheLimit(int) """
        pass

    def setWindowCreated(self, bool): # real signature unknown; restored from __doc__
        """ QGLContext.setWindowCreated(bool) """
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ QGLContext.swapBuffers() """
        pass

    def textureCacheLimit(self): # real signature unknown; restored from __doc__
        """ QGLContext.textureCacheLimit() -> int """
        return 0

    def windowCreated(self): # real signature unknown; restored from __doc__
        """ QGLContext.windowCreated() -> bool """
        return False

    def __init__(self, QGLFormat, QPaintDevice): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DefaultBindOption = 11
    InvertedYBindOption = 1
    LinearFilteringBindOption = 8
    MipmapBindOption = 2
    NoBindOption = 0
    PremultipliedAlphaBindOption = 4


class QGLFormat(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QGLFormat()
    QGLFormat(QGL.FormatOptions, int plane=0)
    QGLFormat(QGLFormat)
    """
    def accum(self): # real signature unknown; restored from __doc__
        """ QGLFormat.accum() -> bool """
        return False

    def accumBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.accumBufferSize() -> int """
        return 0

    def alpha(self): # real signature unknown; restored from __doc__
        """ QGLFormat.alpha() -> bool """
        return False

    def alphaBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.alphaBufferSize() -> int """
        return 0

    def blueBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.blueBufferSize() -> int """
        return 0

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ QGLFormat.defaultFormat() -> QGLFormat """
        return QGLFormat

    def defaultOverlayFormat(self): # real signature unknown; restored from __doc__
        """ QGLFormat.defaultOverlayFormat() -> QGLFormat """
        return QGLFormat

    def depth(self): # real signature unknown; restored from __doc__
        """ QGLFormat.depth() -> bool """
        return False

    def depthBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.depthBufferSize() -> int """
        return 0

    def directRendering(self): # real signature unknown; restored from __doc__
        """ QGLFormat.directRendering() -> bool """
        return False

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ QGLFormat.doubleBuffer() -> bool """
        return False

    def greenBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.greenBufferSize() -> int """
        return 0

    def hasOpenGL(self): # real signature unknown; restored from __doc__
        """ QGLFormat.hasOpenGL() -> bool """
        return False

    def hasOpenGLOverlays(self): # real signature unknown; restored from __doc__
        """ QGLFormat.hasOpenGLOverlays() -> bool """
        return False

    def hasOverlay(self): # real signature unknown; restored from __doc__
        """ QGLFormat.hasOverlay() -> bool """
        return False

    def majorVersion(self): # real signature unknown; restored from __doc__
        """ QGLFormat.majorVersion() -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ QGLFormat.minorVersion() -> int """
        return 0

    def openGLVersionFlags(self): # real signature unknown; restored from __doc__
        """ QGLFormat.openGLVersionFlags() -> QGLFormat.OpenGLVersionFlags """
        pass

    def plane(self): # real signature unknown; restored from __doc__
        """ QGLFormat.plane() -> int """
        return 0

    def profile(self): # real signature unknown; restored from __doc__
        """ QGLFormat.profile() -> QGLFormat.OpenGLContextProfile """
        pass

    def redBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.redBufferSize() -> int """
        return 0

    def rgba(self): # real signature unknown; restored from __doc__
        """ QGLFormat.rgba() -> bool """
        return False

    def sampleBuffers(self): # real signature unknown; restored from __doc__
        """ QGLFormat.sampleBuffers() -> bool """
        return False

    def samples(self): # real signature unknown; restored from __doc__
        """ QGLFormat.samples() -> int """
        return 0

    def setAccum(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setAccum(bool) """
        pass

    def setAccumBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setAccumBufferSize(int) """
        pass

    def setAlpha(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setAlpha(bool) """
        pass

    def setAlphaBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setAlphaBufferSize(int) """
        pass

    def setBlueBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setBlueBufferSize(int) """
        pass

    def setDefaultFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ QGLFormat.setDefaultFormat(QGLFormat) """
        pass

    def setDefaultOverlayFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ QGLFormat.setDefaultOverlayFormat(QGLFormat) """
        pass

    def setDepth(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setDepth(bool) """
        pass

    def setDepthBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setDepthBufferSize(int) """
        pass

    def setDirectRendering(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setDirectRendering(bool) """
        pass

    def setDoubleBuffer(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setDoubleBuffer(bool) """
        pass

    def setGreenBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setGreenBufferSize(int) """
        pass

    def setOption(self, QGL_FormatOptions): # real signature unknown; restored from __doc__
        """ QGLFormat.setOption(QGL.FormatOptions) """
        pass

    def setOverlay(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setOverlay(bool) """
        pass

    def setPlane(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setPlane(int) """
        pass

    def setProfile(self, QGLFormat_OpenGLContextProfile): # real signature unknown; restored from __doc__
        """ QGLFormat.setProfile(QGLFormat.OpenGLContextProfile) """
        pass

    def setRedBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setRedBufferSize(int) """
        pass

    def setRgba(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setRgba(bool) """
        pass

    def setSampleBuffers(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setSampleBuffers(bool) """
        pass

    def setSamples(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setSamples(int) """
        pass

    def setStencil(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setStencil(bool) """
        pass

    def setStencilBufferSize(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setStencilBufferSize(int) """
        pass

    def setStereo(self, bool): # real signature unknown; restored from __doc__
        """ QGLFormat.setStereo(bool) """
        pass

    def setSwapInterval(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFormat.setSwapInterval(int) """
        pass

    def setVersion(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGLFormat.setVersion(int, int) """
        pass

    def stencil(self): # real signature unknown; restored from __doc__
        """ QGLFormat.stencil() -> bool """
        return False

    def stencilBufferSize(self): # real signature unknown; restored from __doc__
        """ QGLFormat.stencilBufferSize() -> int """
        return 0

    def stereo(self): # real signature unknown; restored from __doc__
        """ QGLFormat.stereo() -> bool """
        return False

    def swapInterval(self): # real signature unknown; restored from __doc__
        """ QGLFormat.swapInterval() -> int """
        return 0

    def testOption(self, QGL_FormatOptions): # real signature unknown; restored from __doc__
        """ QGLFormat.testOption(QGL.FormatOptions) -> bool """
        return False

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


    CompatibilityProfile = 2
    CoreProfile = 1
    NoProfile = 0
    OpenGL_ES_CommonLite_Version_1_0 = 256
    OpenGL_ES_CommonLite_Version_1_1 = 1024
    OpenGL_ES_Common_Version_1_0 = 128
    OpenGL_ES_Common_Version_1_1 = 512
    OpenGL_ES_Version_2_0 = 2048
    OpenGL_Version_1_1 = 1
    OpenGL_Version_1_2 = 2
    OpenGL_Version_1_3 = 4
    OpenGL_Version_1_4 = 8
    OpenGL_Version_1_5 = 16
    OpenGL_Version_2_0 = 32
    OpenGL_Version_2_1 = 64
    OpenGL_Version_3_0 = 4096
    OpenGL_Version_3_1 = 8192
    OpenGL_Version_3_2 = 16384
    OpenGL_Version_3_3 = 32768
    OpenGL_Version_4_0 = 65536
    OpenGL_Version_None = 0


class QGLFramebufferObject(__PyQt4_QtGui.QPaintDevice):
    """
    QGLFramebufferObject(QSize, int target=GL_TEXTURE_2D)
    QGLFramebufferObject(int, int, int target=GL_TEXTURE_2D)
    QGLFramebufferObject(QSize, QGLFramebufferObject.Attachment, int target=GL_TEXTURE_2D, int internalFormat=GL_RGBA8)
    QGLFramebufferObject(int, int, QGLFramebufferObject.Attachment, int target=GL_TEXTURE_2D, int internalFormat=GL_RGBA8)
    QGLFramebufferObject(QSize, QGLFramebufferObjectFormat)
    QGLFramebufferObject(int, int, QGLFramebufferObjectFormat)
    """
    def attachment(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.attachment() -> QGLFramebufferObject.Attachment """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.bind() -> bool """
        return False

    def blitFramebuffer(self, QGLFramebufferObject, QRect, QGLFramebufferObject_1, QRect_1, int_buffers=None, int_filter=None): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.blitFramebuffer(QGLFramebufferObject, QRect, QGLFramebufferObject, QRect, int buffers=GL_COLOR_BUFFER_BIT, int filter=GL_NEAREST) """
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLFramebufferObject.drawTexture(QRectF, int, int textureTarget=GL_TEXTURE_2D)
        QGLFramebufferObject.drawTexture(QPointF, int, int textureTarget=GL_TEXTURE_2D)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.format() -> QGLFramebufferObjectFormat """
        return QGLFramebufferObjectFormat

    def handle(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.handle() -> int """
        return 0

    def hasOpenGLFramebufferBlit(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.hasOpenGLFramebufferBlit() -> bool """
        return False

    def hasOpenGLFramebufferObjects(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.hasOpenGLFramebufferObjects() -> bool """
        return False

    def isBound(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.isBound() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.isValid() -> bool """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.paintEngine() -> QPaintEngine """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.release() -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.size() -> QSize """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.texture() -> int """
        return 0

    def toImage(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObject.toImage() -> QImage """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CombinedDepthStencil = 1
    Depth = 2
    NoAttachment = 0


class QGLFramebufferObjectFormat(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QGLFramebufferObjectFormat()
    QGLFramebufferObjectFormat(QGLFramebufferObjectFormat)
    """
    def attachment(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.attachment() -> QGLFramebufferObject.Attachment """
        pass

    def internalTextureFormat(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.internalTextureFormat() -> int """
        return 0

    def mipmap(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.mipmap() -> bool """
        return False

    def samples(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.samples() -> int """
        return 0

    def setAttachment(self, QGLFramebufferObject_Attachment): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.setAttachment(QGLFramebufferObject.Attachment) """
        pass

    def setInternalTextureFormat(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.setInternalTextureFormat(int) """
        pass

    def setMipmap(self, bool): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.setMipmap(bool) """
        pass

    def setSamples(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.setSamples(int) """
        pass

    def setTextureTarget(self, p_int): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.setTextureTarget(int) """
        pass

    def textureTarget(self): # real signature unknown; restored from __doc__
        """ QGLFramebufferObjectFormat.textureTarget() -> int """
        return 0

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, QGLFramebufferObjectFormat=None): # real signature unknown; restored from __doc__ with multiple overloads
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



class QGLPixelBuffer(__PyQt4_QtGui.QPaintDevice):
    """
    QGLPixelBuffer(QSize, QGLFormat format=QGLFormat.defaultFormat(), QGLWidget shareWidget=None)
    QGLPixelBuffer(int, int, QGLFormat format=QGLFormat.defaultFormat(), QGLWidget shareWidget=None)
    """
    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLPixelBuffer.bindTexture(QImage, int target=GL_TEXTURE_2D) -> int
        QGLPixelBuffer.bindTexture(QPixmap, int target=GL_TEXTURE_2D) -> int
        QGLPixelBuffer.bindTexture(QString) -> int
        """
        return 0

    def bindToDynamicTexture(self, p_int): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.bindToDynamicTexture(int) -> bool """
        return False

    def deleteTexture(self, p_int): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.deleteTexture(int) """
        pass

    def devType(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.devType() -> int """
        return 0

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.doneCurrent() -> bool """
        return False

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLPixelBuffer.drawTexture(QRectF, int, int textureTarget=GL_TEXTURE_2D)
        QGLPixelBuffer.drawTexture(QPointF, int, int textureTarget=GL_TEXTURE_2D)
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.format() -> QGLFormat """
        return QGLFormat

    def generateDynamicTexture(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.generateDynamicTexture() -> int """
        return 0

    def handle(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.handle() -> sip.voidptr """
        pass

    def hasOpenGLPbuffers(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.hasOpenGLPbuffers() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.isValid() -> bool """
        return False

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.makeCurrent() -> bool """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.metric(QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.paintEngine() -> QPaintEngine """
        pass

    def releaseFromDynamicTexture(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.releaseFromDynamicTexture() """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.size() -> QSize """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.toImage() -> QImage """
        pass

    def updateDynamicTexture(self, p_int): # real signature unknown; restored from __doc__
        """ QGLPixelBuffer.updateDynamicTexture(int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QGLShader(__PyQt4_QtCore.QObject):
    """
    QGLShader(QGLShader.ShaderType, QObject parent=None)
    QGLShader(QGLShader.ShaderType, QGLContext, QObject parent=None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def compileSourceCode(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShader.compileSourceCode(QByteArray) -> bool
        QGLShader.compileSourceCode(QString) -> bool
        """
        return False

    def compileSourceFile(self, QString): # real signature unknown; restored from __doc__
        """ QGLShader.compileSourceFile(QString) -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaders(self, QGLShader_ShaderType, QGLContext_context=None): # real signature unknown; restored from __doc__
        """ QGLShader.hasOpenGLShaders(QGLShader.ShaderType, QGLContext context=None) -> bool """
        return False

    def isCompiled(self): # real signature unknown; restored from __doc__
        """ QGLShader.isCompiled() -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ QGLShader.log() -> QString """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def shaderId(self): # real signature unknown; restored from __doc__
        """ QGLShader.shaderId() -> int """
        return 0

    def shaderType(self): # real signature unknown; restored from __doc__
        """ QGLShader.shaderType() -> QGLShader.ShaderType """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ QGLShader.sourceCode() -> QByteArray """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QGLShader_ShaderType, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Fragment = 2
    Geometry = 4
    Vertex = 1


class QGLShaderProgram(__PyQt4_QtCore.QObject):
    """
    QGLShaderProgram(QObject parent=None)
    QGLShaderProgram(QGLContext, QObject parent=None)
    """
    def addShader(self, QGLShader): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.addShader(QGLShader) -> bool """
        return False

    def addShaderFromSourceCode(self, QGLShader_ShaderType, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.addShaderFromSourceCode(QGLShader.ShaderType, QByteArray) -> bool
        QGLShaderProgram.addShaderFromSourceCode(QGLShader.ShaderType, QString) -> bool
        """
        return False

    def addShaderFromSourceFile(self, QGLShader_ShaderType, QString): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.addShaderFromSourceFile(QGLShader.ShaderType, QString) -> bool """
        return False

    def attributeLocation(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.attributeLocation(QByteArray) -> int
        QGLShaderProgram.attributeLocation(QString) -> int
        """
        return 0

    def bind(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.bind() -> bool """
        return False

    def bindAttributeLocation(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.bindAttributeLocation(QByteArray, int)
        QGLShaderProgram.bindAttributeLocation(QString, int)
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disableAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.disableAttributeArray(int)
        QGLShaderProgram.disableAttributeArray(str)
        """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def enableAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.enableAttributeArray(int)
        QGLShaderProgram.enableAttributeArray(str)
        """
        pass

    def geometryInputType(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.geometryInputType() -> int """
        return 0

    def geometryOutputType(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.geometryOutputType() -> int """
        return 0

    def geometryOutputVertexCount(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.geometryOutputVertexCount() -> int """
        return 0

    def hasOpenGLShaderPrograms(self, QGLContext_context=None): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.hasOpenGLShaderPrograms(QGLContext context=None) -> bool """
        return False

    def isLinked(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.isLinked() -> bool """
        return False

    def link(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.link() -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.log() -> QString """
        pass

    def programId(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.programId() -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def release(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.release() """
        pass

    def removeAllShaders(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.removeAllShaders() """
        pass

    def removeShader(self, QGLShader): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.removeShader(QGLShader) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.setAttributeArray(int, sequence)
        QGLShaderProgram.setAttributeArray(str, sequence)
        """
        pass

    def setAttributeBuffer(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.setAttributeBuffer(int, int, int, int, int stride=0)
        QGLShaderProgram.setAttributeBuffer(str, int, int, int, int stride=0)
        """
        pass

    def setAttributeValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.setAttributeValue(int, float)
        QGLShaderProgram.setAttributeValue(int, float, float)
        QGLShaderProgram.setAttributeValue(int, float, float, float)
        QGLShaderProgram.setAttributeValue(int, float, float, float, float)
        QGLShaderProgram.setAttributeValue(int, QVector2D)
        QGLShaderProgram.setAttributeValue(int, QVector3D)
        QGLShaderProgram.setAttributeValue(int, QVector4D)
        QGLShaderProgram.setAttributeValue(int, QColor)
        QGLShaderProgram.setAttributeValue(str, float)
        QGLShaderProgram.setAttributeValue(str, float, float)
        QGLShaderProgram.setAttributeValue(str, float, float, float)
        QGLShaderProgram.setAttributeValue(str, float, float, float, float)
        QGLShaderProgram.setAttributeValue(str, QVector2D)
        QGLShaderProgram.setAttributeValue(str, QVector3D)
        QGLShaderProgram.setAttributeValue(str, QVector4D)
        QGLShaderProgram.setAttributeValue(str, QColor)
        """
        pass

    def setGeometryInputType(self, p_int): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.setGeometryInputType(int) """
        pass

    def setGeometryOutputType(self, p_int): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.setGeometryOutputType(int) """
        pass

    def setGeometryOutputVertexCount(self, p_int): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.setGeometryOutputVertexCount(int) """
        pass

    def setUniformValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.setUniformValue(int, int)
        QGLShaderProgram.setUniformValue(int, float)
        QGLShaderProgram.setUniformValue(int, float, float)
        QGLShaderProgram.setUniformValue(int, float, float, float)
        QGLShaderProgram.setUniformValue(int, float, float, float, float)
        QGLShaderProgram.setUniformValue(int, QVector2D)
        QGLShaderProgram.setUniformValue(int, QVector3D)
        QGLShaderProgram.setUniformValue(int, QVector4D)
        QGLShaderProgram.setUniformValue(int, QColor)
        QGLShaderProgram.setUniformValue(int, QPoint)
        QGLShaderProgram.setUniformValue(int, QPointF)
        QGLShaderProgram.setUniformValue(int, QSize)
        QGLShaderProgram.setUniformValue(int, QSizeF)
        QGLShaderProgram.setUniformValue(int, QMatrix2x2)
        QGLShaderProgram.setUniformValue(int, QMatrix2x3)
        QGLShaderProgram.setUniformValue(int, QMatrix2x4)
        QGLShaderProgram.setUniformValue(int, QMatrix3x2)
        QGLShaderProgram.setUniformValue(int, QMatrix3x3)
        QGLShaderProgram.setUniformValue(int, QMatrix3x4)
        QGLShaderProgram.setUniformValue(int, QMatrix4x2)
        QGLShaderProgram.setUniformValue(int, QMatrix4x3)
        QGLShaderProgram.setUniformValue(int, QMatrix4x4)
        QGLShaderProgram.setUniformValue(int, QTransform)
        QGLShaderProgram.setUniformValue(str, int)
        QGLShaderProgram.setUniformValue(str, float)
        QGLShaderProgram.setUniformValue(str, float, float)
        QGLShaderProgram.setUniformValue(str, float, float, float)
        QGLShaderProgram.setUniformValue(str, float, float, float, float)
        QGLShaderProgram.setUniformValue(str, QVector2D)
        QGLShaderProgram.setUniformValue(str, QVector3D)
        QGLShaderProgram.setUniformValue(str, QVector4D)
        QGLShaderProgram.setUniformValue(str, QColor)
        QGLShaderProgram.setUniformValue(str, QPoint)
        QGLShaderProgram.setUniformValue(str, QPointF)
        QGLShaderProgram.setUniformValue(str, QSize)
        QGLShaderProgram.setUniformValue(str, QSizeF)
        QGLShaderProgram.setUniformValue(str, QMatrix2x2)
        QGLShaderProgram.setUniformValue(str, QMatrix2x3)
        QGLShaderProgram.setUniformValue(str, QMatrix2x4)
        QGLShaderProgram.setUniformValue(str, QMatrix3x2)
        QGLShaderProgram.setUniformValue(str, QMatrix3x3)
        QGLShaderProgram.setUniformValue(str, QMatrix3x4)
        QGLShaderProgram.setUniformValue(str, QMatrix4x2)
        QGLShaderProgram.setUniformValue(str, QMatrix4x3)
        QGLShaderProgram.setUniformValue(str, QMatrix4x4)
        QGLShaderProgram.setUniformValue(str, QTransform)
        """
        pass

    def setUniformValueArray(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.setUniformValueArray(int, sequence)
        QGLShaderProgram.setUniformValueArray(str, sequence)
        """
        pass

    def shaders(self): # real signature unknown; restored from __doc__
        """ QGLShaderProgram.shaders() -> list-of-QGLShader """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uniformLocation(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLShaderProgram.uniformLocation(QByteArray) -> int
        QGLShaderProgram.uniformLocation(QString) -> int
        """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QGLWidget(__PyQt4_QtGui.QWidget):
    """
    QGLWidget(QWidget parent=None, QGLWidget shareWidget=None, Qt.WindowFlags flags=0)
    QGLWidget(QGLContext, QWidget parent=None, QGLWidget shareWidget=None, Qt.WindowFlags flags=0)
    QGLWidget(QGLFormat, QWidget parent=None, QGLWidget shareWidget=None, Qt.WindowFlags flags=0)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def autoBufferSwap(self): # real signature unknown; restored from __doc__
        """ QGLWidget.autoBufferSwap() -> bool """
        return False

    def bindTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLWidget.bindTexture(QImage, int target=GL_TEXTURE_2D, int format=GL_RGBA) -> int
        QGLWidget.bindTexture(QPixmap, int target=GL_TEXTURE_2D, int format=GL_RGBA) -> int
        QGLWidget.bindTexture(QString) -> int
        QGLWidget.bindTexture(QImage, int, int, QGLContext.BindOptions) -> int
        QGLWidget.bindTexture(QPixmap, int, int, QGLContext.BindOptions) -> int
        """
        return 0

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def colormap(self): # real signature unknown; restored from __doc__
        """ QGLWidget.colormap() -> QGLColormap """
        return QGLColormap

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ QGLWidget.context() -> QGLContext """
        return QGLContext

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def convertToGLFormat(self, QImage): # real signature unknown; restored from __doc__
        """ QGLWidget.convertToGLFormat(QImage) -> QImage """
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, p_int): # real signature unknown; restored from __doc__
        """ QGLWidget.deleteTexture(int) """
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self): # real signature unknown; restored from __doc__
        """ QGLWidget.doneCurrent() """
        pass

    def doubleBuffer(self): # real signature unknown; restored from __doc__
        """ QGLWidget.doubleBuffer() -> bool """
        return False

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLWidget.drawTexture(QRectF, int, int textureTarget=GL_TEXTURE_2D)
        QGLWidget.drawTexture(QPointF, int, int textureTarget=GL_TEXTURE_2D)
        """
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QGLWidget.event(QEvent) -> bool """
        return False

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

    def fontDisplayListBase(self, QFont, int_listBase=2000): # real signature unknown; restored from __doc__
        """ QGLWidget.fontDisplayListBase(QFont, int listBase=2000) -> int """
        return 0

    def format(self): # real signature unknown; restored from __doc__
        """ QGLWidget.format() -> QGLFormat """
        return QGLFormat

    def glDraw(self): # real signature unknown; restored from __doc__
        """ QGLWidget.glDraw() """
        pass

    def glInit(self): # real signature unknown; restored from __doc__
        """ QGLWidget.glInit() """
        pass

    def grabFrameBuffer(self, bool_withAlpha=False): # real signature unknown; restored from __doc__
        """ QGLWidget.grabFrameBuffer(bool withAlpha=False) -> QImage """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self): # real signature unknown; restored from __doc__
        """ QGLWidget.initializeGL() """
        pass

    def initializeOverlayGL(self): # real signature unknown; restored from __doc__
        """ QGLWidget.initializeOverlayGL() """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self): # real signature unknown; restored from __doc__
        """ QGLWidget.isSharing() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QGLWidget.isValid() -> bool """
        return False

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self): # real signature unknown; restored from __doc__
        """ QGLWidget.makeCurrent() """
        pass

    def makeOverlayCurrent(self): # real signature unknown; restored from __doc__
        """ QGLWidget.makeOverlayCurrent() """
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

    def overlayContext(self): # real signature unknown; restored from __doc__
        """ QGLWidget.overlayContext() -> QGLContext """
        return QGLContext

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ QGLWidget.paintEngine() -> QPaintEngine """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QGLWidget.paintEvent(QPaintEvent) """
        pass

    def paintGL(self): # real signature unknown; restored from __doc__
        """ QGLWidget.paintGL() """
        pass

    def paintOverlayGL(self): # real signature unknown; restored from __doc__
        """ QGLWidget.paintOverlayGL() """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def qglClearColor(self, QColor): # real signature unknown; restored from __doc__
        """ QGLWidget.qglClearColor(QColor) """
        pass

    def qglColor(self, QColor): # real signature unknown; restored from __doc__
        """ QGLWidget.qglColor(QColor) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def renderPixmap(self, int_width=0, int_height=0, bool_useContext=False): # real signature unknown; restored from __doc__
        """ QGLWidget.renderPixmap(int width=0, int height=0, bool useContext=False) -> QPixmap """
        pass

    def renderText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QGLWidget.renderText(int, int, QString, QFont font=QFont(), int listBase=2000)
        QGLWidget.renderText(float, float, float, QString, QFont font=QFont(), int listBase=2000)
        """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QGLWidget.resizeEvent(QResizeEvent) """
        pass

    def resizeGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGLWidget.resizeGL(int, int) """
        pass

    def resizeOverlayGL(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QGLWidget.resizeOverlayGL(int, int) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoBufferSwap(self, bool): # real signature unknown; restored from __doc__
        """ QGLWidget.setAutoBufferSwap(bool) """
        pass

    def setColormap(self, QGLColormap): # real signature unknown; restored from __doc__
        """ QGLWidget.setColormap(QGLColormap) """
        pass

    def setContext(self, QGLContext, QGLContext_shareContext=None, bool_deleteOldContext=True): # real signature unknown; restored from __doc__
        """ QGLWidget.setContext(QGLContext, QGLContext shareContext=None, bool deleteOldContext=True) """
        pass

    def setFormat(self, QGLFormat): # real signature unknown; restored from __doc__
        """ QGLWidget.setFormat(QGLFormat) """
        pass

    def setMouseTracking(self, bool): # real signature unknown; restored from __doc__
        """ QGLWidget.setMouseTracking(bool) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self): # real signature unknown; restored from __doc__
        """ QGLWidget.swapBuffers() """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateGL(self): # real signature unknown; restored from __doc__
        """ QGLWidget.updateGL() """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updateOverlayGL(self): # real signature unknown; restored from __doc__
        """ QGLWidget.updateOverlayGL() """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


