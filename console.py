#!/usr/bin/python3
"""import modules"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        print()
        return True

    def emptyline(self):
        """shouldn’t execute anything by enter"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if arg == None or arg == "":
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            base = storage.classes()[arg]()
            base.save()
            print(base.id)

    def do_show(self,arg):
        """ Prints the string representation of an instance
        based on the class name and id"""
        base = storage.classes()[arg]()
        if arg == None or arg == "":
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        elif base.id == None or base.id == "":
            print("** instance id missing **")
        elif base.id not in storage.classes():
            print("** no instance found **")
        else:
            print(base.id)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        base = storage.classes()[arg]()
        if arg == None or arg == "":
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        elif base.id == None or base.id == "":
            print("** instance id missing **")
        elif base.id not in storage.classes():
            print("** no instance found **")
        else:
            del storage.all()[arg]

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        if arg not in storage.classes():
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute"""
        base = storage.classes()[arg]()
        if arg == None or arg == "":
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        elif base.id == None or base.id == "":
            print("** instance id missing **")
        elif base.id not in storage.classes():
            print("** no instance found **")
        for items in storage.all().keys():
            if items == None or items == "":
                print("** attribute name missing **")
            elif items not in allinstances.keys():
                print("** value missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
