#策略模式：
#定义一系列算法，将每个算法都封装起来，并且使他们之间可以相互替换。
#策略模式使算法可以独立于使用它的用户而变化。
from abc import ABCMeta,abstractmethod
class Person:
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def showMyself(self):
        print("name=%s,age=%d,weight=%0.2f,height=%0.2f"%(self.name,self.age,self.weight,self.height))

class ICompare(metaclass=ABCMeta):
    @abstractmethod
    def comparable(self,person1,person2):
        pass

class CompareByAge(ICompare):
    def comparable(self,person1,person2):
        return person1.age - person2.age

class CompareByHeight(ICompare):
    def comparable(self,person1,person2):
        return person1.height - person2.height

class SortPerson:
    def __init__(self,compare):
        self.__compare = compare
    def sort(self,personList):
        n = len(personList)
        for i in range(0,n-1):
            for j in range(0,n-i-1):
                if(self.__compare.comparable(personList[j],personList[j+1])>0):
                    personList[j],personList[j+1]=personList[j+1],personList[j]

def testSortPerson():
    personList = [
        Person("tony",2,55,0.82),
        Person("jack",31,74.5,1.8),
        Person("nick",54,44.5,1.59),
        Person("eric",23,62,1.78),
        Person("helen",16,45.7,1.6)
    ]
    ageSorter = SortPerson(CompareByAge())
    ageSorter.sort(personList)
    print("after age sorting:")
    for person in personList:
        person.showMyself()
    print()

    heightSorter = SortPerson(CompareByHeight())
    heightSorter.sort(personList)
    for person in personList:
        person.showMyself()
    print()
