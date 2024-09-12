

from message import Message

class UserInterface:
    def __init__(self):
        self.commands = {}
        self.message = Message()

    def show_commands(self):
        for key,val in self.commands.items():
            message = key + " - " + val["description"]
            self.message.display(message) # Renamed to display
            

    def register_command(self, command, callback, description=""):
        self.commands[command] = {
            "callback": callback,
            "description": description
        }

    def deregister_command(self, command):
        if commind in self.commands:
            self.commands.pop(command)
        else:
             self.message.display(f"Command '{command}' not found")  # Inform if command not found


    def execute_command(self, command, args):
        try:
            func = self.commands[command]["callback"]
            return func(args)
        except KeyError:
            self.message.display("sorry, that is not a valid command") # Renamed to display
            return None
        except Exception as e:
            self.message.display(f"An error occurred: {e}")  # Renamed to display
            return None
