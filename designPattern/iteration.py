#迭代模式提供一种方法顺序地访问一组聚合对象中的各个元素，而又不需要暴露该对象的内部细节。
#provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation
#代码框架
class BaseIterator:
    def __init__(self,data):
        self.__data = data
        self.toBegin()
    def toBegin(self):
        self.__curIdx = -1
    def toEnd(self):
        self.__curIdx = len(self.__data)
    def next(self):
        if (self.__curIdx < len(self.__data)-1):
            self.__curIdx += 1
            return True
        else:
            return False
    def previous(self):
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False
    def current(self):
        if self.__curIdx >= 0 and self.__curIdx < len(self.__data):
            return self.__data[self.__curIdx]
        else:
            return None
#有了这些功能，可以从前往后遍历，也可以从后往前遍历
#还可以实现多次遍历
def testBaseIterator():
    print("forward to back:")
    iterator = BaseIterator(range(0,10))
    while(iterator.next()):
        customer = iterator.current()
        print(customer,end="\t")
    print()
    print("back forward:")
    iterator.toEnd()
    while(iterator.previous()):
        customer = iterator.current()
        print(customer,end="\t")

testBaseIterator()
#优点：
#1 迭代器模式将存储数据和遍历数据的职责分离
#2 简化了聚合数据的访问方式
#3 可支持多种不同的方式遍历一个聚合对象
#应用场景
#1集合的内部结构复杂，不想暴露对象的内部细节，只提供精简的访问方式
#2 需要提供统一的访问接口，从而对不同的集合使用统一的算法
#3 需要未一系列聚合对象提供多种不同的访问方式
