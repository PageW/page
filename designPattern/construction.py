#构建模式：将一复杂对象的构建过程和它的表现分离，使得同样的构建过程可以获取不同的表现
from abc import ABCMeta,abstractmethod

class Toy(metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name
        self.__components = []
    def getName(self):
        return self._name
    def addComponent(self,component,count=1,unit="个"):
        self.__components.append([component,count,unit])
    @abstractmethod
    def feature(self):
        pass
class Car(Toy):
    def feature(self):
        print("i am %s,i can run fast..."%self._name)

class Manor(Toy):
    def feature(self):
        print("i am %s,i can play"%self._name)

class ToyBuilder(metaclass=ABCMeta):
    @abstractmethod
    def buildProduct(self):
        pass

class CarBuilder(ToyBuilder):
    def buildProduct(self):
        car = Car("mini car")
        print("constructing %s..."%car.getName())
        car.addComponent("wheel",4)
        car.addComponent("body",1)
        car.addComponent("engine",1)
        return car

class ManorBuilder(ToyBuilder):
    def buildProduct(self):
        manor = Manor("tt house")
        print("constructing %s"%manor.getName())
        manor.addComponent("kitchen",1,"间")
        manor.addComponent("bedroom",2,"间")
        manor.addComponent("garden",1,"个")
        return manor

class BuilderMgr:
    def __init__(self):
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()
    def buildCar(self,num):
        count = 0
        products = []
        while count < num:
            car = self.__carBuilder.buildProduct()
            products.append(car)
            count += 1
            print("building %d %s completed"%(count,car.getName()))
        return products
    def buildManor(self,num):
        count = 0
        products = []
        while count < num:
            manor = self.__manorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print("building %d %s completed"%(count,manor.getName()))
        return products

def testAdvancedBuilder():
    builderMgr = BuilderMgr()
    builderMgr.buildManor(2)
    print()
    builderMgr.buildCar(4)

testAdvancedBuilder()
#构造模式主要有三种角色：产品，构建者，指挥者
#应用场景：
#产品的创建过程比较复杂，希望将产品的创建过程和它本身的功能分离开来
#产品有很多种类，每个种类之间的内部结构比较相似，但有很多差异；不同的创建顺序或者不同组合模式会创建不同产品