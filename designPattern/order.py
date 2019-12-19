#命令模式：将一个请求封装成一个对象，从而让你使用不同的请求将客户端参数化，对请求排队或者记录请求日志，可以提供命令的撤销和恢复功能。
from abc import ABCMeta,abstractmethod

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class CommandImpl(Command):
    def __init__(self,reveiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.doSomething()

class Receiver:
    def doSomething(self):
        print("do something")

class Invoker:
    def __init__(self):
        self.__command = None
    def setCommand(self,command):
        self.__command = command
    def action(self):
        if self.__command is not None:
            self.__command.execute()

#命令模式有命令，接受者，调度者，用户。
#优点是对命令的发送者和接受者进行解耦，使得调用方不用关心具体的行动执行者如何执行，只需要发送正确的命令
#可以很方便的增加新命令
#缺点是在一些系统中可能会有很多命令，而每一个命令都需要一个具体的类去封装，容易使命令的类急剧膨胀
