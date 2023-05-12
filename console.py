#!/usr/bin/python3

"""Command interpeter."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Class that handles the commands for AirBnB project."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the command interpeter."""
        return True
    
    def do_quit(self, line):
        """Exits the command interpeter."""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered."""
        pass



if __name__ == "__main__":
    HBNBCommand().cmdloop()

