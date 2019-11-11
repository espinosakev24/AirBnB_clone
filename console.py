#!/usr/bin/python3
"""
Console module
"""
import cmd
from models import all_classes
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, inputs):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id """
        if not(inputs):
            print("** class name missing **")
        else:
            try:
                if all_classes[inputs]:
                    instance = all_classes[inputs]()
                    instance.save()
                    print(instance.id)
            except Exception:
                print("** class doesn't exist **")

    def help_create(self):
        """
        Prints the message to the help command
        """
        print("  This command create a new instance of BaseModel.\n"
              "  To create an instance you can write:\n   create BaseModel")
    def do_show(self, inputs):
        """ Prints the string representation of an
        instance based on the class name and id.
        """
        if not(inputs):
            print("** class name missing **")
        else:
            check = 0
            try:
                class_name = inputs.split(" ")[0]
                try:
                    object_id = inputs.split(" ")[1]
                except Exception:
                    print("** instance id missing **")
                    return
                if all_classes[class_name]:
                    all_objs = storage.all()
                    for key in all_objs.keys():
                        obj = all_objs[key]
                        if obj.id == object_id:
                            check = 1
                            print(obj)
                    if check == 0:
                        print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")
    def help_show(self):
        """
        """
        pass

    def do_destroy(self, inputs):
        """
        """
        try:
            class_name = inputs.split(" ")[0]
            try:
                if all_classes[inputs]:
                    print("Exitst")
            except Exception:
                print("** class doesn't exist **")
                return
            try:
                object_id = inputs.split(" ")[1]
            except Exception:
                print("** instance id missing **")
                return
            all_objs = storage.all()
            for key in all_objs[key]
                obj = all_objs[key]
                if obj.id == object_id:
        except Exception:
            print("** class name missing **")

    def destroy_help(self):
        """
        """
        pass    
    def do_quit(self, inputs):
        """ Exit the console when the input is exit """
        return True

    def help_quit(self):
        """
        Prints the message to the help command
        """
        print("  Quit command to exit the program")

    def do_EOF(self, inputs):
        """ Exit the console when the input is Ctr+D """
        print()
        return True

    def help_EOF(self):
        """
        Prints the message to the help command
        """
        print("  EOF command to exit the program")

    def do_help(self, inputs):
        """
        List of commands that have help for each command
        """
        cmd.Cmd.do_help(self, inputs)

    def emptyline(inputs):
        """ If inputs is a new line, do not execute anything """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
