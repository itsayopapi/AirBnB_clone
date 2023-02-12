#!/usr/bin/python3

import cmd

from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
     prompt = '(hbnb) '
     
     def do_quit(self,line):
         return True
     def do_EOF(self, line):
         return True
     def do_help(self, line):
         return True

if __name__ == '__main__':
     HBNBCommand().cmdloop()
