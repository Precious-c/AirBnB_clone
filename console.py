#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Airbnb Commandline tool"""
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_quit(self, line):
        """Quits the program"""
        return True
    
    def do_EOF(self, line):
        """Quits tge program"""
        return True
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
