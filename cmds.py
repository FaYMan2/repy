
class command:
    def __init__(self,rawCommand : str):
        self.rawCommand = rawCommand
        self.type = None
        self.content = None
    def decodeCommand(self):
        splitedCommand = self.rawCommand.split("\r\n")
        self.type = splitedCommand[0]
        self.content = splitedCommand[1:]
        