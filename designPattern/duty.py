from abc import ABCMeta,abstractmethod
class Request:
    #request contents
    def __init__(self,name,dayoff,reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None
    def getName(self):
        return self.__name
    def getDayOff(self):
        return self.__dayoff
    def getReason(self):
        return self.__reason

class Responsible(metaclass = ABCMeta):
    #responsible abstract
    def __init__(self,name,title):
        self.__name = name
        self.__title = title
        self._nextHandler = None
    def getName(self):
        return self.__name
    def getTitle(self):
        return self.__title
    def setNextHandler(self,nextHandler):
        self._nextHandler = nextHandler
    def getNextHandler(self):
        return self._nextHandler
    def handleRequest(self,request):
        self._handleRequestImpl(request)
        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(request)
    @abstractmethod
    def _handleRequestImpl(self,request):
        #the actual method to handle request
        pass

class Person:
    def __init__(self,name):
        self.__name = name
        self.__leader = None
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setLeader(self,leader):
        self.__leader = leader
    def getLeader(self):
        return self.__leader
    def sendRequest(self,request):
        print("%s days: %d .reason:%s"%(self.__name,request.getDayOff(),request.getReason()))
        if(self.__leader is not None):
            self.__leader.handleRequest(request)
class Supervisor(Responsible):
    def __init__(self,name,title):
        super().__init__(name,title)
    def _handleRequestImpl(self,request):
        if (request.getDayOff() <= 2):
            print("agree %s,signed by %s(%s)"%(request.getName(),self.getName(),self.getTitle()))

class DepartmentManager(Responsible):
    def __init__(self,name,title):
        super().__init__(name,title)
    def _handleRequestImpl(self,request):
        if (request.getDayOff() > 2 and request.getDayOff() <= 5):
            print("agree %s,signed by %s(%s)"%(request.getName(),self.getName(),self.getTitle()))

class CEO(Responsible):
    def __init__(self,name,title):
        super().__init__(name,title)
    def _handleRequestImpl(self,request):
        if (request.getDayOff() > 5 and request.getDayOff() <= 22):
            print("agree %s,signed by %s(%s)"%(request.getName(),self.getName(),self.getTitle()))

class Administrator(Responsible):
    def __init__(self,name,title):
        super().__init__(name,title)
    def _handleRequestImpl(self,request):
        print("recorded!!!!!!")

def test():
    directLeader = Supervisor("eren","client manager")
    departmentLeader = DepartmentManager("eric","cto")
    ceo = CEO("helen","ceo")
    administrator = Administrator("nina","admin")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(administrator)
    
    sunny = Person("Sunny")
    sunny.setLeader(directLeader)
    sunny.sendRequest(Request(sunny.getName(),1,"mdcc"))
    tony = Person("tony")
    tony.setLeader(directLeader)
    tony.sendRequest(Request(tony.getName(),5,"home reason"))
    pony = Person("pony")
    pony.setLeader(directLeader)
    pony.sendRequest(Request(pony.getName(),15,"abroad"))

test()
