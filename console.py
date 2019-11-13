#!/usr/bin/python3
"""
Console module
"""
import cmd
from datetime import datetime
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
                cl = all_classes[class_name]
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
        if not(inputs):
            print("** class name missing **")
        else:
            check = 0
            try:
                class_name = inputs.split(" ")[0]
                cl = all_classes[class_name]
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
                            del all_objs[class_name + '.' + obj.id]
                            storage.save()
                            break
                    if check == 0:
                        print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def destroy_help(self):
        """
        """
        pass

    def do_all(self, inputs):
        """
        """
        all_objs = storage.all()
        if not(inputs):
            for key, value in all_objs.items():
                print([str(value)])
            return
        try:
            cl = all_classes[inputs]
        except Exception:
            print("** class doesn't exist **")
            return
        for key in all_objs.keys():
            if key.split('.')[0] == inputs:
                print([str(all_objs[key])])

    def all_help(self):
        """
        """
        pass

    def do_update(self, inputs):
        """
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
                    if check == 0:
                        print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")
                return
            obj_key = class_name + '.' + object_id
            obj = all_objs[obj_key]
            try:
                atr = inputs.split(" ")[2]
            except Exception:
                print("** attribute name missing **")
                return
            try:
                value_name = inputs.split(" ")[3]
            except Exception:
                print("** value missing **")
                return
            if atr != 'created_at' or atr != 'update_at' or atr != 'id':
                obj.__dict__.update({atr: value_name})
                obj.save()
    def help_update(self):
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
