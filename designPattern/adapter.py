#适配模式：将一个类的接口变成客户端所期望的另一种接口，从而使得原本接口不匹配而无法一起工作的两个类能够一起工作
#接口转换，用新接口包装一个已有的类，匹配一个老组件到一个新接口
from abc import ABCMeta,abstractmethod

class Target(metaclass=ABCMeta):
    @abstractmethod
    def function(self):
        pass

class Adaptee:
    def speciaficFunction(self):
        print("special funcs")

class Adapter(Adaptee,Target):
    def function(self):
        print("transform funcs")

