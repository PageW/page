#外观模式：为子系统中的一组借口提供一个一致的界面称为外观模式，外观模式定义了一个高层接口，这个接口是的这一个子系统更容易使用。
#外观模式只有两个角色，外观角色和子系统。
#优点实现了子系统和客户端之间的松耦合关系，简化了客户端对子系统的使用难度，为不同的用户提供了统一的调用借口。
#文件的压缩与解压缩系统
from os import path
import logging

class ZIPModel:
    def compress(self,srcFilePath,dstFilePath):
        print("zip is compressing %s docs..."%srcFilePath)
    def decompress(self,srcFilePath,dstFilePath):
        print("zip is decompressing %s docs..." % srcFilePath)

class RARModel:
    def compress(self,srcFilePath,dstFilePath):
        print("rar is compressing...")
    def decompress(self,srcFilePath,dstFilePath):
        print("rar is decompressing...")

class ZModel:
    def compress(self,srcFilePath,dstFilePath):
        print("7z is compressing ...")
    def decompress(self,srcFilePath,dstFilePath):
        print("7z is decompressing ...")

class CompressionFacade:
    def __init__(self):
        self.__zipModel = ZIPModel()
        self.__rarModel = RARModel()
        self.__zModel = ZModel()

    def compress(self,srcFilePath,dstFilePath,type):
        extName = "." + type
        fullName = dstFilePath + extName
        if (type.lower() == "zip"):
            self.__zipModel.compress(srcFilePath,fullName)
        elif (type.lower() == "rar"):
            self.__rarModel.compress(srcFilePath,fullName)
        elif (type.lower() == "7z"):
            self.__zModel.compress(srcFilePath,fullName)
        else:
            logging.error("not support this format:"+str(type))
            return False
        return True

    def decompress(self,srcFilePath,dstFilePath):
        baseName = path.basename(srcFilePath)
        extName = baseName.split(".")[1]
        if (extName.lower() == "zip"):
            self.__zipModel.decompress(srcFilePath,dstFilePath)
        elif (extName.lower() == "rar"):
            self.__rarModel.decompress(srcFilePath,dstFilePath)
        elif(extName.lower() =="7z"):
            self.__zModel.decompress(srcFilePath,dstFilePath)
        else:
            logging.error("not support this format:" + str(extName))
            return False
        return True

def testCompression():
    facade = CompressionFacade()
    facade.compress("e:\标准文件\生活中的外观模式.md","e:\压缩文件、生活中的外观模式.md","zip")
    facade.decompress("e:\压缩文件\生活中的外观模式.zip","E:\标准文件\生活中的外观模式.md")

testCompression()
#实际情况下，应该通过文件的魔数来判断解压缩类型。
#应用场景
#1 要为一个复杂子系统提供一个简单借口
#2 客户程序与多个子系统之间存在很大的依赖性时。引入外观类将子系统与客户以及其他子系统解耦，可以提高子系统的独立性和可移植性
#3 在层次化结构中，可以使用外观模式定义系统中每一层的入口，层与层之间不直接产生联系。通过外观类建立联系，降低层之间的耦合度。
