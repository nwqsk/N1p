import sys
import threading

class Console(threading.Thread): 
    def __init__(self, messages, bot): 
        threading.Thread.__init__(self) 
        self.messages = messages 
        self.bot = bot
        self.running = True

    def run(self): 
        while(self.running):
            command = input('$ ')

            if(command == "quit"):
                self.running = False
            else:
                self.messages.console_log(self.messages.unknownCommand + command)

        sys.exit(0)


                