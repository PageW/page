#备忘模式在不破坏内部结构的前提下捕获一个对象的内部状态，这样可以在以后将该对象恢复到原先保存的状态
#capture the object's internal state without exposing its internal structure,so that the object can be returned to this state later.
#备忘模式的最大功能就是备份，可以保存对象的一个状态作为备份，这样便可以让对象在将来的某一时刻恢复到之前保存的状态


#备忘模式框架
from copy import deepcopy
class Memento:
    def setAtrributes(self,dict):
        self.__dict__ = deepcopy(dict)

    def getAttributes(self):
        return self.__dict__

class Caretaker:
    def __init__(self):
        self._mementos = {}
    def addMemento(self,name,memento):
        self._mementos[name] = memento
    def getMemento(self,name):
        return self._mementos[name]

class Originator:
    def createMemento(self):
        memento = Memento()
        memento.setAtrributes(self.__dict__)
        return memento
    def restoreFromMemento(self,memento):
        self.__dict__.update(memento.getAttributes())


import logging
class TerminalCmd(Originator):
    def __init__(self,text):
        self.__cmdName = ""
        self.__cmdArgs = []
        self.parseCmd(text)
    def parseCmd(self,text):
        subStrs = self.getArgumentsFromString(text," ")
        if (len(subStrs)>0):
            self.__cmdName = subStrs[0]
        if (len(subStrs)>1):
            self.__cmdArgs = subStrs[1:]

    def getArgumentsFromString(self,str,splitFlag):
        if(splitFlag == ""):
            logging.warning("splitFlag is empty")
            return ""
        data = str.split(splitFlag)
        result = []
        for item in data:
            item.strip()
            if(item != ""):
                result.append(item)
        return result

    def showCmd(self):
        print(self.__cmdName,self.__cmdArgs)

class TerminalCaretaker(Caretaker):
    def showHistroyCmds(self):
        for key,obj in self._mementos.items():
            name = ""
            value = []
            if(obj._TerminalCmd__cmdName):
                name = obj._TerminalCmd__cmdName
            if(obj._TerminalCmd__cmdArgs):
                value = obj._TerminalCmd__cmdArgs
            print(key,name,value)

def testTerminal():
    cmdIdx = 0
    caretaker = TerminalCaretaker()
    curCmd = TerminalCmd("")
    while(True):
        strCmd = input("input:");
        strCmd = strCmd.lower()
        if(strCmd.startswith("q")):
            exit(0)
        elif(strCmd.startswith("h")):
            caretaker.showHistroyCmds()
        elif(strCmd.startswith("!")):
            idx = int(strCmd[1:])
            curCmd.restoreFromMemento(caretaker.getMemento(idx))
            curCmd.showCmd()
        else:
            curCmd = TerminalCmd(strCmd)
            curCmd.showCmd()
            caretaker.addMemento(cmdIdx,curCmd.createMemento())
            cmdIdx += 1

testTerminal()

#应用场景：需要保存/恢复对象的状态或数据的时候，比如游戏存档，虚拟机的快照
#需要实现撤销、恢复功能的场景，如word中的ctrl+z
#提供一个可回滚的操作，如数据库的事务管理