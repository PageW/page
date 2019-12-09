from copy import copy,deepcopy
class Clone:
	def clone(self):
		return copy(self)
	def deepClone(self):
		return deepcopy(self)

class Person(Clone):
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def showMyself(self):
		print("i am "+self.__name+"age is "+str(self.__age)+".")
	def coding(self):
		print("i am programmer,coding")
	def reading(self):
		print("reading is happy")
	def fallInLove(self):
		print("flowers")


def testClone():
	
    print("start testing")
    tony = Person("tony",27)	
    tony.showMyself()
    tony.coding()
    tony1 = tony.clone()
    tony1.showMyself()
    tony1.coding()
        
    tony2 = tony.deepClone()
    tony2.showMyself()
    tony1.coding()
testClone()
