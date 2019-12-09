from copy import copy,deepcopy
class Clone():
    def clone(self):
        return copy(self)
    def deepClone(self):
        return deepcopy(self)

class AppConfig(Clone):
    def __init__(self,configName):
        self.__configName = configName
        self.parseFromFile("./config/default.xml")
    def parseFromFile(self,filePath):
        self.__fontType = "song"
        self.__fontSize = 14
        self.__language = "chinese"
        self.__logPath = "./logs/appException.log"
    def saveToFile(self,filePath):
        pass
    def copyConfig(self,configName):
        config = self.deepClone()
        config.__configName = configName
        return config
    def showInfo(self):
        print("%s 的配置信息："%self.__configName)
        print(self.__fontType)
        print(self.__fontSize)
        print(self.__language)
        print(self.__logPath)

    def setFontType(self,fontType):
        self.__fontType = fontType
    def setFontSize(self,fontSize):
        self.__fontSize = fontSize
    def setLanguage(self,language):
        self.__language = language
    def setLogPath(self,logPath):
        self.__logPath = logPath

def testAppConfig():
    defaultConfig = AppConfig("default")
    defaultConfig.showInfo()
    print()

    newConfig = defaultConfig.copyConfig("tonyConfig")
    newConfig.setFontType("black")
    newConfig.setFontSize(18)
    newConfig.setLanguage("english")
    newConfig.showInfo()
testAppConfig()
