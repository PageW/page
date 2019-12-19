#享元模式：运用共享技术有效的支持大量细粒度对象的复用
from abc import ABCMeta,abstractmethod
class Flyweight(metaclass=ABCMeta):
    @abstractmethod
    def operation(self,extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    def __init__(self,color):
        self.__color = color
    def operation(self,extrinsicState):
        print("%s 取得 %s 色颜料"%(extrinsicState,self.__color))

class FlyweightFactory:
    def __init__(self):
        self.__flyweights ={}
    def getFlyweight(self,key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment

def testFlyweight():
    factory = FlyweightFactory()
    pigmentRed = factory.getFlyweight("红")
    pigmentRed.operation("dream")
    pigmentYellow = factory.getFlyweight("黄")
    pigmentYellow.operation("dream")
    pigmentBlue = factory.getFlyweight("蓝")
    pigmentBlue.operation("hero")

#享元对象：即你期望用来共享的对象
#享元工厂：核心角色，负责创建和管理享元对象。