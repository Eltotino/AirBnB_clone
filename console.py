#!/usr/bin/python3
""" HBNBCommand Class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit program"""
        print()
        return True

    def emptyline(self):
        """Empty line case"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
