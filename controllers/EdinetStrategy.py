from commands.command import Command


class EdinetStrategy:
    def __init__(self):
        self.command_list = []

    def add(self, command: Command):
        self.command_list.append(command)

    def act(self):
        for command in self.command_list:
            command.execute()
