#!/usr/bin/python3
'''
    implementing the console class
'''

import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Simple command processor.  """

    prompt = '(hbnb)'

    classes = {
        'BaseModel': BaseModel,
        "User": User,
        'Place': Place,
        'State': State,
        'City': City,
        'Review': Review,
        'State': State,
        'City': City,
    }

    def do_EOF(self, arg):
        '''exit the cmd iteration'''
        return True

    def do_help(self, arg):
        return super().do_help(arg)

    def do_quit(self, arg):
        return True

    def help_quit(self):
        '''help the quit command'''
        print("Quit command to exit the program.")

    def emptyline(self):
        '''do nothing when an empty line is entered'''
        pass

    def do_create(self, arg):
        '''create a new instance of BaseModel'''
        arg = arg.split()
        classes = {
            'BaseModel': BaseModel,
            "User": User,
            'Place': Place,
            'State': State,
            'City': City,
            'Review': Review,
            'State': State,
            'City': City,
        }
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg[0]]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, arg):
        '''show the string representation of an instance'''
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn\'t exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn\'t exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn\'t exist **")
        else:
            print([str(obj) for obj in models.storage.all().values()
                   if arg[0] == obj.__class__.__name__])

    def do_update(self, arg):
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.classes.keys():
            print("** class doesn\'t exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in models.storage.all():
                print("** no instance found **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                setattr(models.storage.all()[key], arg[2], arg[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
