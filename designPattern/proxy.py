from abc import ABCMeta,abstractmethod

class Subject(metaclass=ABCMeta):
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    @abstractmethod
    def request(self,content=''):
        pass

class RealSubject(Subject):
    def request(self,content):
        print("read subject todo somethin...")

class ProxySubject(Subject):
    def __init__(self,name,subject):
        super().__init__(name)
        self._realSubject = subject
    def request(self,content=''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()
    def preRequest(self):
        print("preRequest")
    def afterRequest(self):
        print("afterRequest")

def testProxy():
    realObj = RealSubject("RealSubject")
    proxyObj = ProxySubject("ProxySubject",realObj)
    proxyObj.request()

class TonyReception(Subject):
    def __init__(self,name,phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum
    def getPhoneNum(self):
        return self.__phoneNum
    def request(self,content):
        print("owner: %s ,phone:%s"%(self.getName(),self.getPhoneNum()))
        print("received a package which content is %s" % str(content))

class WendyReception(ProxySubject):
    def __init__(self,name,receiver):
        super().__init__(name,receiver)
    def preRequest(self):
        print("i am %s friend,helping to receive the package" %(self._realSubject.getName()+""))
    def afterRequest(self):
        print("代收人：%s" %self.getName())

def testReceiverParcel2():
    tony = TonyReception("tony","12312313")
    print("tony receive:")
    tony.request("shoes")
    print()

    print("wendy receive:")
    wendy = WendyReception("wendy",tony)
    wendy.request("shoes")

testReceiverParcel2()
#应用场景
#1 不想或者不能直接引用一个对象
#2 想对一个对象的功能进行加强
#3 各种特殊用途的代理：远程代理，虚拟代理，copy-on-write代理，保护代理，cache代理，
#防火墙代理，同步化代理，只能引用代理
