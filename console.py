#!/usr/bin/python3

"""Command interpeter."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json


class HBNBCommand(cmd.Cmd):
    """Class that handles the commands for AirBnB project."""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]
    all_objects = models.storage.all()

    def do_EOF(self, line):
        """Exits the command interpeter."""
        return True

    def do_quit(self, line):
        """Exits the command interpeter."""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered."""
        pass

    def get_instance(self, name, ins_id):
        """Gets the object by the class name and id."""
        key = f"{name}.{ins_id}"
        instance = self.all_objects.get(key, None)
        return instance

    def check_line(self, line, count):
        """Checks the arguments passed with the command."""
        args = line.split()
        length = len(args)
        if length == 0:
            print("** class name missing **")
            return False
        else:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return False
            if count == 1:
                return True
            if length == 1:
                print("** instance id missing **")
                return False
            else:
                instance = self.get_instance(args[0], args[1])
                if instance is not None:
                    return True
                else:
                    print("** no instance found **")
                    return False

    def do_create(self, line):
        """Creates a new instance."""
        if self.check_line(line, 1):
            args = line.split()
            new = eval(f"{args[0]}()")
            new.save()
            print(new.id)

    def do_show(self, line):
        """Shows information about created instance by id."""
        args = line.split()
        if self.check_line(line, 2):
            instance = self.get_instance(args[0], args[1])
            print(instance)

    def do_all(self, line):
        """Prints all objects with the class name provided."""
        args = line.split()
        objects = []
        if len(args) == 0:
            objects = [str(v) for k, v in self.all_objects.items()]
            print(objects)
        elif self.check_line(line, 1):
            objects = [str(v) for k, v in self.all_objects.items()
                       if k.startswith(args[0])]
            print(objects)

    def do_destroy(self, line):
        """Deletes an instance based on class name and id."""
        if self.check_line(line, 2):
            args = line.split()
            key = f"{args[0]}.{args[1]}"
            self.all_objects.pop(key)
            models.storage.save()

    def do_update(self, line):
        """Updates instance by class name and id
        by adding or updating instances.
        """
        if self.check_line(line, 2):
            args = line.split()
            length = len(args)
            if length == 2:
                print("** attribute name missing **")
            elif length == 3:
                print("** value missing **")
            else:
                instance = self.get_instance(args[0], args[1])
                name = args[2]
                value = args[3]
                if value.startswith('"'):
                    value = line.split('"')[1]
                try:
                    attr_type = type(getattr(instance, name))
                    value = attr_type(value)
                except (ValueError, AttributeError):
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            pass
                setattr(instance, name, value)
                instance.save()

    def try_update(self, cls_name, obj_attr):
        """Try to use update function if arguments are correct."""
        args = obj_attr.split(',')
        obj_id = args[0].strip('" ')
        try:
            obj_attr.index("{")
            dict_attr = obj_attr.split("{")
            new_dict = "{" + dict_attr[1]
            new_dict = new_dict.replace("'", '"')
            update_dict = json.loads(new_dict)
            ins = self.get_instance(cls_name, obj_id)
            origin_dict = ins.to_dict()
            origin_dict.update(update_dict)
            cls_type = type(ins)
            self.all_objects[f"{cls_name}.{obj_id}"] = cls_type(**origin_dict)
        except Exception as e:
            try:
                attr_name = args[1].strip('" ')
                attr_value = args[2].strip('" ')
                self.do_update(f"{cls_name} {obj_id} {attr_name} {attr_value}")
            except Exception as e:
                cmd.Cmd.default(self, f"{cls_name}.{obj_attr}")

    def count(self, line):
        """Counts the number of instances of a class."""
        args = line.split()
        objects = [k for k in self.all_objects.keys() if k.startswith(args[0])]
        print(len(objects))

    def default(self, line):
        """Defines a default implmentation if any other command was passed."""
        args = line.split(".")
        try:
            cls_name = args[0]
            function = args[1].split("(")[0]
            obj_id = args[1].split("(")[1][0:-1]
        except IndexError:
            return cmd.Cmd.default(self, line)
        functions = {
            "all": self.do_all,
            "count": self.count,
            "show": self.do_show,
            "update": self.try_update,
            "destroy": self.do_destroy
            }
        if (cls_name not in self.classes
                or function not in functions.keys()):
            return cmd.Cmd.default(self, line)
        else:
            if function == "update":
                self.try_update(cls_name, obj_id)
            else:
                functions[function](f"{cls_name} {obj_id}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
