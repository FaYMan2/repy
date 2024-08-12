
class command:
    def __init__(self,rawCommand : str):
        self.__rawCommand = rawCommand
        self.type = None
        self.content = None
        self.expiry = None
    def decodeCommand(self):
        splitedCommand = self.__rawCommand.split("\r\n")
        self.type = splitedCommand[0]
        if splitedCommand[-2] == 'px':
            self.expiry = int(splitedCommand[-1])
            self.content = splitedCommand[1:-2]
        else:
            self.content = splitedCommand[1:]
        