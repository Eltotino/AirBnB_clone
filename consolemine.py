#!/usr/bin/python3
""" HBNBCommand Class"""
import cmd
from models import storage
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class"""
    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City, "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """empty line"""
        pass

    def default(self, line):
        """default method"""
        lista = (line.replace('(', '.').replace(',', '.').replace(' ', '')
               [:-1].split('.'))
        if len(lista) > 1:
            if lista[1] == "all":
                return self.do_all(lista[0])

            elif lista[1] == "show":
                return self.do_show(lista[0] + ' ' + lista[2])

            elif lista[1] == "destroy":
                return self.do_destroy(lista[0] + ' ' + lista[2])

            elif lista[1] == "update":
                return (self.do_update(lista[0] + ' ' + lista[2] +
                                       ' ' + lista[3] + ' ' + lista[4]))

            elif lista[1] == "count":
                print(len(storage.all()))

        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_create(self, args):
        """Create command a new instance
        """
        args = args.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        else:
            bm = HBNBCommand.classes[args[0]]()
            bm.save()
            print(bm.id)

    def do_show(self, args):
        """Show command print the dict format of instance
        """
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            print(_all["{}.{}".format(args.split()[0], args.split()[1])])

    def do_destroy(self, args):
        """Destroy created instance"""
        arg = args.split()
        _all = storage.all()
        if not arg:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        else:
            del _all["{}.{}".format(args.split()[0], args.split()[1])]
            storage.save()

    def do_all(self, args):
        """All command Prints all string representation of \
            all instances based or not on the class name
        """
        args = args.split()
        lista = []
        if args and args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif not args:
            for c in storage.all().values():
                lista.append(str(c))
        else:
            for c in storage.all().values():
                if args[0] == c.__class__.__name__:
                    lista.append(str(c))
        if len(lista):
            print(lista)

    def do_update(self, args):
        """Update command for resetting user attributes
        """
        _all = storage.all()
        if len(args.split()) == 0:
            print("** class name missing **")

        elif args.split()[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")

        elif len(args.split()) == 1:
            print("** instance id missing **")

        elif "{}.{}".format(args.split()[0], args.split()[1]) not in _all:
            print("** no instance found **")

        elif len(args.split()) == 2:
            print("** attribute name missing **")

        elif len(args.split()) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args.split()[0], args.split()[1])
            setattr(_all[key], args.split()[2],
                    re.search(r'\w+', args.split()[3]).group())
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()