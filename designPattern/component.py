#组合模式：
#将对象组合成树形结构以表示“整体-部分”的层次结构关系。组合使得用户对单个对象和符合对象的使用具有一致性
from abc import ABCMeta,abstractmethod

class Component(metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name
    def getName(self):
        return self._name
    def isComposite(self):
        return False
    @abstractmethod
    def feature(self,indent):
        pass

class Composite(Component):
    def __init__(self,name):
        super().__init__(name)
        self._components = []
    def addComponent(self,component):
        self._components.append(component)
    def removeComponent(self,component):
        self._components.remove(component)
    def isComposite(self):
        return True
    def feature(self,indent):
        indent += "\t"
        for component in self._components:
            print(indent,end="")
            component.feature(indent)

#优点调用简单，组合对象可以像一般对象一样使用
#组合对象可以自由的增加、删除组件，可灵活的组合不同的对象。
#缺点：在一些层次结构太深的场景中，组合结构会变得太庞杂
