# encoding: utf-8
# module PyQt4.QtSql
# from C:\Python27\lib\site-packages\PyQt4\QtSql.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QSql(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AfterLastRow = -2
    AllTables = 255
    BeforeFirstRow = -1
    Binary = 4
    HighPrecision = 0
    In = 1
    InOut = 3
    LowPrecisionDouble = 4
    LowPrecisionInt32 = 1
    LowPrecisionInt64 = 2
    Out = 2
    SystemTables = 2
    Tables = 1
    Views = 4


class QSqlDatabase(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSqlDatabase()
    QSqlDatabase(QSqlDatabase)
    QSqlDatabase(QString)
    QSqlDatabase(QSqlDriver)
    """
    def addDatabase(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlDatabase.addDatabase(QString, QString connectionName=QLatin1String(QSqlDatabase.defaultConnection)) -> QSqlDatabase
        QSqlDatabase.addDatabase(QSqlDriver, QString connectionName=QLatin1String(QSqlDatabase.defaultConnection)) -> QSqlDatabase
        """
        pass

    def cloneDatabase(self, QSqlDatabase, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.cloneDatabase(QSqlDatabase, QString) -> QSqlDatabase """
        return QSqlDatabase

    def close(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.close() """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.commit() -> bool """
        return False

    def connectionName(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.connectionName() -> QString """
        pass

    def connectionNames(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.connectionNames() -> QStringList """
        pass

    def connectOptions(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.connectOptions() -> QString """
        pass

    def contains(self, QString_connectionName=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlDatabase.contains(QString connectionName=QLatin1String(QSqlDatabase.defaultConnection)) -> bool """
        pass

    def database(self, QString_connectionName=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlDatabase.database(QString connectionName=QLatin1String(QSqlDatabase.defaultConnection), bool open=True) -> QSqlDatabase """
        pass

    def databaseName(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.databaseName() -> QString """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.driver() -> QSqlDriver """
        return QSqlDriver

    def driverName(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.driverName() -> QString """
        pass

    def drivers(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.drivers() -> QStringList """
        pass

    def exec_(self, QString_query=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlDatabase.exec_(QString query=QString()) -> QSqlQuery """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.hostName() -> QString """
        pass

    def isDriverAvailable(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.isDriverAvailable(QString) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.isOpen() -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.isOpenError() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.isValid() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.lastError() -> QSqlError """
        return QSqlError

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.numericalPrecisionPolicy() -> QSql.NumericalPrecisionPolicy """
        pass

    def open(self, QString=None, QString_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlDatabase.open() -> bool
        QSqlDatabase.open(QString, QString) -> bool
        """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.password() -> QString """
        pass

    def port(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.port() -> int """
        return 0

    def primaryIndex(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.primaryIndex(QString) -> QSqlIndex """
        return QSqlIndex

    def record(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.record(QString) -> QSqlRecord """
        return QSqlRecord

    def registerSqlDriver(self, QString, QSqlDriverCreatorBase): # real signature unknown; restored from __doc__
        """ QSqlDatabase.registerSqlDriver(QString, QSqlDriverCreatorBase) """
        pass

    def removeDatabase(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.removeDatabase(QString) """
        pass

    def rollback(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.rollback() -> bool """
        return False

    def setConnectOptions(self, QString_options=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlDatabase.setConnectOptions(QString options=QString()) """
        pass

    def setDatabaseName(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.setDatabaseName(QString) """
        pass

    def setHostName(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.setHostName(QString) """
        pass

    def setNumericalPrecisionPolicy(self, QSql_NumericalPrecisionPolicy): # real signature unknown; restored from __doc__
        """ QSqlDatabase.setNumericalPrecisionPolicy(QSql.NumericalPrecisionPolicy) """
        pass

    def setPassword(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.setPassword(QString) """
        pass

    def setPort(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlDatabase.setPort(int) """
        pass

    def setUserName(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDatabase.setUserName(QString) """
        pass

    def tables(self, QSql_TableType_type=None): # real signature unknown; restored from __doc__
        """ QSqlDatabase.tables(QSql.TableType type=QSql.Tables) -> QStringList """
        pass

    def transaction(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.transaction() -> bool """
        return False

    def userName(self): # real signature unknown; restored from __doc__
        """ QSqlDatabase.userName() -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlDriver(__PyQt4_QtCore.QObject):
    """ QSqlDriver(QObject parent=None) """
    def beginTransaction(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.beginTransaction() -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.close() """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.commitTransaction() -> bool """
        return False

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createResult(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.createResult() -> QSqlResult """
        return QSqlResult

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def escapeIdentifier(self, QString, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ QSqlDriver.escapeIdentifier(QString, QSqlDriver.IdentifierType) -> QString """
        pass

    def formatValue(self, QSqlField, bool_trimStrings=False): # real signature unknown; restored from __doc__
        """ QSqlDriver.formatValue(QSqlField, bool trimStrings=False) -> QString """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.handle() -> QVariant """
        pass

    def hasFeature(self, QSqlDriver_DriverFeature): # real signature unknown; restored from __doc__
        """ QSqlDriver.hasFeature(QSqlDriver.DriverFeature) -> bool """
        return False

    def isIdentifierEscaped(self, QString, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ QSqlDriver.isIdentifierEscaped(QString, QSqlDriver.IdentifierType) -> bool """
        return False

    def isIdentifierEscapedImplementation(self, QString, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ QSqlDriver.isIdentifierEscapedImplementation(QString, QSqlDriver.IdentifierType) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.isOpen() -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.isOpenError() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.lastError() -> QSqlError """
        return QSqlError

    def notification(self, *args, **kwargs): # real signature unknown
        """ QSqlDriver.notification[QString] [signal] """
        pass

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.numericalPrecisionPolicy() -> QSql.NumericalPrecisionPolicy """
        pass

    def open(self, QString, QString_user=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlDriver.open(QString, QString user=QString(), QString password=QString(), QString host=QString(), int port=-1, QString options=QString()) -> bool """
        pass

    def primaryIndex(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDriver.primaryIndex(QString) -> QSqlIndex """
        return QSqlIndex

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDriver.record(QString) -> QSqlRecord """
        return QSqlRecord

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.rollbackTransaction() -> bool """
        return False

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, QSqlError): # real signature unknown; restored from __doc__
        """ QSqlDriver.setLastError(QSqlError) """
        pass

    def setNumericalPrecisionPolicy(self, QSql_NumericalPrecisionPolicy): # real signature unknown; restored from __doc__
        """ QSqlDriver.setNumericalPrecisionPolicy(QSql.NumericalPrecisionPolicy) """
        pass

    def setOpen(self, bool): # real signature unknown; restored from __doc__
        """ QSqlDriver.setOpen(bool) """
        pass

    def setOpenError(self, bool): # real signature unknown; restored from __doc__
        """ QSqlDriver.setOpenError(bool) """
        pass

    def sqlStatement(self, QSqlDriver_StatementType, QString, QSqlRecord, bool): # real signature unknown; restored from __doc__
        """ QSqlDriver.sqlStatement(QSqlDriver.StatementType, QString, QSqlRecord, bool) -> QString """
        pass

    def stripDelimiters(self, QString, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ QSqlDriver.stripDelimiters(QString, QSqlDriver.IdentifierType) -> QString """
        pass

    def stripDelimitersImplementation(self, QString, QSqlDriver_IdentifierType): # real signature unknown; restored from __doc__
        """ QSqlDriver.stripDelimitersImplementation(QString, QSqlDriver.IdentifierType) -> QString """
        pass

    def subscribedToNotifications(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.subscribedToNotifications() -> QStringList """
        pass

    def subscribedToNotificationsImplementation(self): # real signature unknown; restored from __doc__
        """ QSqlDriver.subscribedToNotificationsImplementation() -> QStringList """
        pass

    def subscribeToNotification(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDriver.subscribeToNotification(QString) -> bool """
        return False

    def subscribeToNotificationImplementation(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDriver.subscribeToNotificationImplementation(QString) -> bool """
        return False

    def tables(self, QSql_TableType): # real signature unknown; restored from __doc__
        """ QSqlDriver.tables(QSql.TableType) -> QStringList """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotification(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDriver.unsubscribeFromNotification(QString) -> bool """
        return False

    def unsubscribeFromNotificationImplementation(self, QString): # real signature unknown; restored from __doc__
        """ QSqlDriver.unsubscribeFromNotificationImplementation(QString) -> bool """
        return False

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    BatchOperations = 8
    BLOB = 2
    DeleteStatement = 4
    EventNotifications = 11
    FieldName = 0
    FinishQuery = 12
    InsertStatement = 3
    LastInsertId = 7
    LowPrecisionNumbers = 10
    MultipleResultSets = 13
    NamedPlaceholders = 5
    PositionalPlaceholders = 6
    PreparedQueries = 4
    QuerySize = 1
    SelectStatement = 1
    SimpleLocking = 9
    TableName = 1
    Transactions = 0
    Unicode = 3
    UpdateStatement = 2
    WhereStatement = 0


class QSqlDriverCreatorBase(): # skipped bases: <type 'sip.wrapper'>
    """
    QSqlDriverCreatorBase()
    QSqlDriverCreatorBase(QSqlDriverCreatorBase)
    """
    def createObject(self): # real signature unknown; restored from __doc__
        """ QSqlDriverCreatorBase.createObject() -> QSqlDriver """
        return QSqlDriver

    def __init__(self, QSqlDriverCreatorBase=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlError(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSqlError(QString driverText=QString(), QString databaseText=QString(), QSqlError.ErrorType type=QSqlError.NoError, int number=-1)
    QSqlError(QSqlError)
    """
    def databaseText(self): # real signature unknown; restored from __doc__
        """ QSqlError.databaseText() -> QString """
        pass

    def driverText(self): # real signature unknown; restored from __doc__
        """ QSqlError.driverText() -> QString """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSqlError.isValid() -> bool """
        return False

    def number(self): # real signature unknown; restored from __doc__
        """ QSqlError.number() -> int """
        return 0

    def setDatabaseText(self, QString): # real signature unknown; restored from __doc__
        """ QSqlError.setDatabaseText(QString) """
        pass

    def setDriverText(self, QString): # real signature unknown; restored from __doc__
        """ QSqlError.setDriverText(QString) """
        pass

    def setNumber(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlError.setNumber(int) """
        pass

    def setType(self, QSqlError_ErrorType): # real signature unknown; restored from __doc__
        """ QSqlError.setType(QSqlError.ErrorType) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QSqlError.text() -> QString """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QSqlError.type() -> QSqlError.ErrorType """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConnectionError = 1
    NoError = 0
    StatementError = 2
    TransactionError = 3
    UnknownError = 4


class QSqlField(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSqlField(QString fieldName=QString(), Type type=QVariant.Invalid)
    QSqlField(QSqlField)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlField.clear() """
        pass

    def defaultValue(self): # real signature unknown; restored from __doc__
        """ QSqlField.defaultValue() -> QVariant """
        pass

    def isAutoValue(self): # real signature unknown; restored from __doc__
        """ QSqlField.isAutoValue() -> bool """
        return False

    def isGenerated(self): # real signature unknown; restored from __doc__
        """ QSqlField.isGenerated() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QSqlField.isNull() -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QSqlField.isReadOnly() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSqlField.isValid() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QSqlField.length() -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ QSqlField.name() -> QString """
        pass

    def precision(self): # real signature unknown; restored from __doc__
        """ QSqlField.precision() -> int """
        return 0

    def requiredStatus(self): # real signature unknown; restored from __doc__
        """ QSqlField.requiredStatus() -> QSqlField.RequiredStatus """
        pass

    def setAutoValue(self, bool): # real signature unknown; restored from __doc__
        """ QSqlField.setAutoValue(bool) """
        pass

    def setDefaultValue(self, QVariant): # real signature unknown; restored from __doc__
        """ QSqlField.setDefaultValue(QVariant) """
        pass

    def setGenerated(self, bool): # real signature unknown; restored from __doc__
        """ QSqlField.setGenerated(bool) """
        pass

    def setLength(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlField.setLength(int) """
        pass

    def setName(self, QString): # real signature unknown; restored from __doc__
        """ QSqlField.setName(QString) """
        pass

    def setPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlField.setPrecision(int) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QSqlField.setReadOnly(bool) """
        pass

    def setRequired(self, bool): # real signature unknown; restored from __doc__
        """ QSqlField.setRequired(bool) """
        pass

    def setRequiredStatus(self, QSqlField_RequiredStatus): # real signature unknown; restored from __doc__
        """ QSqlField.setRequiredStatus(QSqlField.RequiredStatus) """
        pass

    def setSqlType(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlField.setSqlType(int) """
        pass

    def setType(self, Type): # real signature unknown; restored from __doc__
        """ QSqlField.setType(Type) """
        pass

    def setValue(self, QVariant): # real signature unknown; restored from __doc__
        """ QSqlField.setValue(QVariant) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QSqlField.type() -> Type """
        pass

    def typeID(self): # real signature unknown; restored from __doc__
        """ QSqlField.typeID() -> int """
        return 0

    def value(self): # real signature unknown; restored from __doc__
        """ QSqlField.value() -> QVariant """
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


    Optional = 0
    Required = 1
    Unknown = -1


class QSqlRecord(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSqlRecord()
    QSqlRecord(QSqlRecord)
    """
    def append(self, QSqlField): # real signature unknown; restored from __doc__
        """ QSqlRecord.append(QSqlField) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlRecord.clear() """
        pass

    def clearValues(self): # real signature unknown; restored from __doc__
        """ QSqlRecord.clearValues() """
        pass

    def contains(self, QString): # real signature unknown; restored from __doc__
        """ QSqlRecord.contains(QString) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ QSqlRecord.count() -> int """
        return 0

    def field(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.field(int) -> QSqlField
        QSqlRecord.field(QString) -> QSqlField
        """
        return QSqlField

    def fieldName(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlRecord.fieldName(int) -> QString """
        pass

    def indexOf(self, QString): # real signature unknown; restored from __doc__
        """ QSqlRecord.indexOf(QString) -> int """
        return 0

    def insert(self, p_int, QSqlField): # real signature unknown; restored from __doc__
        """ QSqlRecord.insert(int, QSqlField) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QSqlRecord.isEmpty() -> bool """
        return False

    def isGenerated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.isGenerated(int) -> bool
        QSqlRecord.isGenerated(QString) -> bool
        """
        return False

    def isNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.isNull(int) -> bool
        QSqlRecord.isNull(QString) -> bool
        """
        return False

    def remove(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlRecord.remove(int) """
        pass

    def replace(self, p_int, QSqlField): # real signature unknown; restored from __doc__
        """ QSqlRecord.replace(int, QSqlField) """
        pass

    def setGenerated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.setGenerated(QString, bool)
        QSqlRecord.setGenerated(int, bool)
        """
        pass

    def setNull(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.setNull(int)
        QSqlRecord.setNull(QString)
        """
        pass

    def setValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.setValue(int, QVariant)
        QSqlRecord.setValue(QString, QVariant)
        """
        pass

    def value(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlRecord.value(int) -> QVariant
        QSqlRecord.value(QString) -> QVariant
        """
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

    def __init__(self, QSqlRecord=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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



class QSqlIndex(QSqlRecord):
    """
    QSqlIndex(QString cursorName=QString(), QString name=QString())
    QSqlIndex(QSqlIndex)
    """
    def append(self, QSqlField, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlIndex.append(QSqlField)
        QSqlIndex.append(QSqlField, bool)
        """
        pass

    def cursorName(self): # real signature unknown; restored from __doc__
        """ QSqlIndex.cursorName() -> QString """
        pass

    def isDescending(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlIndex.isDescending(int) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QSqlIndex.name() -> QString """
        pass

    def setCursorName(self, QString): # real signature unknown; restored from __doc__
        """ QSqlIndex.setCursorName(QString) """
        pass

    def setDescending(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QSqlIndex.setDescending(int, bool) """
        pass

    def setName(self, QString): # real signature unknown; restored from __doc__
        """ QSqlIndex.setName(QString) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QSqlQuery(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSqlQuery(QSqlResult)
    QSqlQuery(QString query=QString(), QSqlDatabase db=QSqlDatabase())
    QSqlQuery(QSqlDatabase)
    QSqlQuery(QSqlQuery)
    """
    def addBindValue(self, QVariant, QSql_ParamType_type=None): # real signature unknown; restored from __doc__
        """ QSqlQuery.addBindValue(QVariant, QSql.ParamType type=QSql.In) """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.at() -> int """
        return 0

    def bindValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlQuery.bindValue(QString, QVariant, QSql.ParamType type=QSql.In)
        QSqlQuery.bindValue(int, QVariant, QSql.ParamType type=QSql.In)
        """
        pass

    def boundValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlQuery.boundValue(QString) -> QVariant
        QSqlQuery.boundValue(int) -> QVariant
        """
        pass

    def boundValues(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.boundValues() -> dict-of-QString-QVariant """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.clear() """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.driver() -> QSqlDriver """
        return QSqlDriver

    def execBatch(self, QSqlQuery_BatchExecutionMode_mode=None): # real signature unknown; restored from __doc__
        """ QSqlQuery.execBatch(QSqlQuery.BatchExecutionMode mode=QSqlQuery.ValuesAsRows) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.executedQuery() -> QString """
        pass

    def exec_(self, QString=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlQuery.exec_(QString) -> bool
        QSqlQuery.exec_() -> bool
        """
        return False

    def finish(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.finish() """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.first() -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.isActive() -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.isForwardOnly() -> bool """
        return False

    def isNull(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlQuery.isNull(int) -> bool """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.isSelect() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.isValid() -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.last() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.lastError() -> QSqlError """
        return QSqlError

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.lastInsertId() -> QVariant """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.lastQuery() -> QString """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.next() -> bool """
        return False

    def nextResult(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.nextResult() -> bool """
        return False

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.numericalPrecisionPolicy() -> QSql.NumericalPrecisionPolicy """
        pass

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.numRowsAffected() -> int """
        return 0

    def prepare(self, QString): # real signature unknown; restored from __doc__
        """ QSqlQuery.prepare(QString) -> bool """
        return False

    def previous(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.previous() -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.record() -> QSqlRecord """
        return QSqlRecord

    def result(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.result() -> QSqlResult """
        return QSqlResult

    def seek(self, p_int, bool_relative=False): # real signature unknown; restored from __doc__
        """ QSqlQuery.seek(int, bool relative=False) -> bool """
        return False

    def setForwardOnly(self, bool): # real signature unknown; restored from __doc__
        """ QSqlQuery.setForwardOnly(bool) """
        pass

    def setNumericalPrecisionPolicy(self, QSql_NumericalPrecisionPolicy): # real signature unknown; restored from __doc__
        """ QSqlQuery.setNumericalPrecisionPolicy(QSql.NumericalPrecisionPolicy) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSqlQuery.size() -> int """
        return 0

    def value(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlQuery.value(int) -> QVariant """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ValuesAsColumns = 1
    ValuesAsRows = 0


class QSqlQueryModel(__PyQt4_QtCore.QAbstractTableModel):
    """ QSqlQueryModel(QObject parent=None) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def canFetchMore(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlQueryModel.canFetchMore(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.clear() """
        pass

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlQueryModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlQueryModel.fetchMore(QModelIndex parent=QModelIndex()) """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        pass

    def indexInQuery(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.indexInQuery(QModelIndex) -> QModelIndex """
        pass

    def insertColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlQueryModel.insertColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.lastError() -> QSqlError """
        return QSqlError

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.query() -> QSqlQuery """
        return QSqlQuery

    def queryChange(self): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.queryChange() """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlQueryModel.record(int) -> QSqlRecord
        QSqlQueryModel.record() -> QSqlRecord
        """
        return QSqlRecord

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlQueryModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlQueryModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setLastError(self, QSqlError): # real signature unknown; restored from __doc__
        """ QSqlQueryModel.setLastError(QSqlError) """
        pass

    def setQuery(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlQueryModel.setQuery(QSqlQuery)
        QSqlQueryModel.setQuery(QString, QSqlDatabase db=QSqlDatabase())
        """
        pass

    def setRoleNames(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QSqlRelation(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QSqlRelation()
    QSqlRelation(QString, QString, QString)
    QSqlRelation(QSqlRelation)
    """
    def displayColumn(self): # real signature unknown; restored from __doc__
        """ QSqlRelation.displayColumn() -> QString """
        pass

    def indexColumn(self): # real signature unknown; restored from __doc__
        """ QSqlRelation.indexColumn() -> QString """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSqlRelation.isValid() -> bool """
        return False

    def tableName(self): # real signature unknown; restored from __doc__
        """ QSqlRelation.tableName() -> QString """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlRelationalDelegate(__PyQt4_QtGui.QItemDelegate):
    """ QSqlRelationalDelegate(QObject parent=None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlRelationalDelegate.createEditor(QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, *args, **kwargs): # real signature unknown
        pass

    def drawCheck(self, *args, **kwargs): # real signature unknown
        pass

    def drawDecoration(self, *args, **kwargs): # real signature unknown
        pass

    def drawDisplay(self, *args, **kwargs): # real signature unknown
        pass

    def drawFocus(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlRelationalDelegate.setEditorData(QWidget, QModelIndex) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlRelationalDelegate.setModelData(QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QSqlTableModel(QSqlQueryModel):
    """ QSqlTableModel(QObject parent=None, QSqlDatabase db=QSqlDatabase()) """
    def beforeDelete(self, *args, **kwargs): # real signature unknown
        """ QSqlTableModel.beforeDelete[int] [signal] """
        pass

    def beforeInsert(self, *args, **kwargs): # real signature unknown
        """ QSqlTableModel.beforeInsert[QSqlRecord] [signal] """
        pass

    def beforeUpdate(self, *args, **kwargs): # real signature unknown
        """ QSqlTableModel.beforeUpdate[int, QSqlRecord] [signal] """
        pass

    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.clear() """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlTableModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def database(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.database() -> QSqlDatabase """
        return QSqlDatabase

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlTableModel.deleteRowFromTable(int) -> bool """
        return False

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def editStrategy(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.editStrategy() -> QSqlTableModel.EditStrategy """
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fieldIndex(self, QString): # real signature unknown; restored from __doc__
        """ QSqlTableModel.fieldIndex(QString) -> int """
        return 0

    def filter(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.filter() -> QString """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlTableModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlTableModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> QVariant """
        pass

    def indexInQuery(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlTableModel.indexInQuery(QModelIndex) -> QModelIndex """
        pass

    def insertRecord(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ QSqlTableModel.insertRecord(int, QSqlRecord) -> bool """
        return False

    def insertRowIntoTable(self, QSqlRecord): # real signature unknown; restored from __doc__
        """ QSqlTableModel.insertRowIntoTable(QSqlRecord) -> bool """
        return False

    def insertRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlTableModel.insertRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def isDirty(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QSqlTableModel.isDirty(QModelIndex) -> bool """
        return False

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.orderByClause() -> QString """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def primaryKey(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.primaryKey() -> QSqlIndex """
        return QSqlIndex

    def primeInsert(self, *args, **kwargs): # real signature unknown
        """ QSqlTableModel.primeInsert[int, QSqlRecord] [signal] """
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlTableModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def removeRows(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlTableModel.removeRows(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.revert() """
        pass

    def revertAll(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.revertAll() """
        pass

    def revertRow(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlTableModel.revertRow(int) """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlTableModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.select() -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.selectStatement() -> QString """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setEditStrategy(self, QSqlTableModel_EditStrategy): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setEditStrategy(QSqlTableModel.EditStrategy) """
        pass

    def setFilter(self, QString): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setFilter(QString) """
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, QSqlIndex): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setPrimaryKey(QSqlIndex) """
        pass

    def setQuery(self, QSqlQuery): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setQuery(QSqlQuery) """
        pass

    def setRecord(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setRecord(int, QSqlRecord) -> bool """
        return False

    def setRoleNames(self, *args, **kwargs): # real signature unknown
        pass

    def setSort(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setSort(int, Qt.SortOrder) """
        pass

    def setTable(self, QString): # real signature unknown; restored from __doc__
        """ QSqlTableModel.setTable(QString) """
        pass

    def sort(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ QSqlTableModel.sort(int, Qt.SortOrder) """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.submit() -> bool """
        return False

    def submitAll(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.submitAll() -> bool """
        return False

    def tableName(self): # real signature unknown; restored from __doc__
        """ QSqlTableModel.tableName() -> QString """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ QSqlTableModel.updateRowInTable(int, QSqlRecord) -> bool """
        return False

    def __init__(self, QObject_parent=None, QSqlDatabase_db=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    OnFieldChange = 0
    OnManualSubmit = 2
    OnRowChange = 1


class QSqlRelationalTableModel(QSqlTableModel):
    """ QSqlRelationalTableModel(QObject parent=None, QSqlDatabase db=QSqlDatabase()) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.clear() """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, QSqlRecord): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.insertRowIntoTable(QSqlRecord) -> bool """
        return False

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.orderByClause() -> QString """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def relation(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.relation(int) -> QSqlRelation """
        return QSqlRelation

    def relationModel(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.relationModel(int) -> QSqlTableModel """
        return QSqlTableModel

    def removeColumns(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QSqlRelationalTableModel.removeColumns(int, int, QModelIndex parent=QModelIndex()) -> bool """
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.revertRow(int) """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.select() -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.selectStatement() -> QString """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setJoinMode(self, QSqlRelationalTableModel_JoinMode): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.setJoinMode(QSqlRelationalTableModel.JoinMode) """
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRelation(self, p_int, QSqlRelation): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.setRelation(int, QSqlRelation) """
        pass

    def setRoleNames(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, QString): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.setTable(QString) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, p_int, QSqlRecord): # real signature unknown; restored from __doc__
        """ QSqlRelationalTableModel.updateRowInTable(int, QSqlRecord) -> bool """
        return False

    def __init__(self, QObject_parent=None, QSqlDatabase_db=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    InnerJoin = 0
    LeftJoin = 1


class QSqlResult(): # skipped bases: <type 'sip.wrapper'>
    """ QSqlResult(QSqlDriver) """
    def addBindValue(self, QVariant, QSql_ParamType): # real signature unknown; restored from __doc__
        """ QSqlResult.addBindValue(QVariant, QSql.ParamType) """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ QSqlResult.at() -> int """
        return 0

    def bindingSyntax(self): # real signature unknown; restored from __doc__
        """ QSqlResult.bindingSyntax() -> QSqlResult.BindingSyntax """
        pass

    def bindValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlResult.bindValue(int, QVariant, QSql.ParamType)
        QSqlResult.bindValue(QString, QVariant, QSql.ParamType)
        """
        pass

    def bindValueType(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlResult.bindValueType(QString) -> QSql.ParamType
        QSqlResult.bindValueType(int) -> QSql.ParamType
        """
        pass

    def boundValue(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSqlResult.boundValue(QString) -> QVariant
        QSqlResult.boundValue(int) -> QVariant
        """
        pass

    def boundValueCount(self): # real signature unknown; restored from __doc__
        """ QSqlResult.boundValueCount() -> int """
        return 0

    def boundValueName(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlResult.boundValueName(int) -> QString """
        pass

    def boundValues(self): # real signature unknown; restored from __doc__
        """ QSqlResult.boundValues() -> list-of-QVariant """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSqlResult.clear() """
        pass

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlResult.data(int) -> QVariant """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ QSqlResult.driver() -> QSqlDriver """
        return QSqlDriver

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ QSqlResult.executedQuery() -> QString """
        pass

    def exec_(self): # real signature unknown; restored from __doc__
        """ QSqlResult.exec_() -> bool """
        return False

    def fetch(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlResult.fetch(int) -> bool """
        return False

    def fetchFirst(self): # real signature unknown; restored from __doc__
        """ QSqlResult.fetchFirst() -> bool """
        return False

    def fetchLast(self): # real signature unknown; restored from __doc__
        """ QSqlResult.fetchLast() -> bool """
        return False

    def fetchNext(self): # real signature unknown; restored from __doc__
        """ QSqlResult.fetchNext() -> bool """
        return False

    def fetchPrevious(self): # real signature unknown; restored from __doc__
        """ QSqlResult.fetchPrevious() -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ QSqlResult.handle() -> QVariant """
        pass

    def hasOutValues(self): # real signature unknown; restored from __doc__
        """ QSqlResult.hasOutValues() -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ QSqlResult.isActive() -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ QSqlResult.isForwardOnly() -> bool """
        return False

    def isNull(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlResult.isNull(int) -> bool """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ QSqlResult.isSelect() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSqlResult.isValid() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QSqlResult.lastError() -> QSqlError """
        return QSqlError

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ QSqlResult.lastInsertId() -> QVariant """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ QSqlResult.lastQuery() -> QString """
        pass

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ QSqlResult.numRowsAffected() -> int """
        return 0

    def prepare(self, QString): # real signature unknown; restored from __doc__
        """ QSqlResult.prepare(QString) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ QSqlResult.record() -> QSqlRecord """
        return QSqlRecord

    def reset(self, QString): # real signature unknown; restored from __doc__
        """ QSqlResult.reset(QString) -> bool """
        return False

    def savePrepare(self, QString): # real signature unknown; restored from __doc__
        """ QSqlResult.savePrepare(QString) -> bool """
        return False

    def setActive(self, bool): # real signature unknown; restored from __doc__
        """ QSqlResult.setActive(bool) """
        pass

    def setAt(self, p_int): # real signature unknown; restored from __doc__
        """ QSqlResult.setAt(int) """
        pass

    def setForwardOnly(self, bool): # real signature unknown; restored from __doc__
        """ QSqlResult.setForwardOnly(bool) """
        pass

    def setLastError(self, QSqlError): # real signature unknown; restored from __doc__
        """ QSqlResult.setLastError(QSqlError) """
        pass

    def setQuery(self, QString): # real signature unknown; restored from __doc__
        """ QSqlResult.setQuery(QString) """
        pass

    def setSelect(self, bool): # real signature unknown; restored from __doc__
        """ QSqlResult.setSelect(bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSqlResult.size() -> int """
        return 0

    def __init__(self, QSqlDriver): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NamedBinding = 1
    PositionalBinding = 0


