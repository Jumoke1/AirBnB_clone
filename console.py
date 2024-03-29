#!/usr/bin/python3
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

all_classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Command to exit from keyboard interruption"""
        print('')
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def precmd(self, line):
        """Defines instructions to execute before <line> is interpreted.
        """
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            args = match_tuple[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", match_tuple[2]))
            else:
                match_json = re.findall(r"{.*}", match_tuple[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        match_tuple[1], match_tuple[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_help(self, line):
        """To get help on a command, type help <command>"""
        return super().do_help(line)

    def do_create(self, line):
        """Creates new object"""
        storage.reload()
        objs = storage.all()
        if not line.strip():
            print("** class name missing **")
            return
        # call_classes = [obj["__class__"] for obj in objs.values()]
        chosen_class = line.strip()
        if chosen_class not in all_classes:
            print("** class doesn't exist **")
            return

        new_mod = eval(f"{chosen_class}()")
        storage.new(new_mod)
        storage.save()
        print(new_mod.id)

    def do_show(self, line):
        """Show info about a specified object"""
        storage.reload()
        objs = storage.all()
        if not line.strip():
            print("** class name missing **")
            return
        # all_classes = [obj["__class__"] for obj in objs.values()]
        chosen_class = line.strip().split()[0]
        if chosen_class not in all_classes:
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return

        obj_id = line.split()[1]
        all_ids = [obj["id"] for obj in objs.values()]
        if obj_id.strip() not in all_ids:
            print("** no instance found **")
            return
        key = ".".join(line.split())
        dict_of_obj_to_show = objs[key]
        new_obj = eval(f"{chosen_class}(**{dict_of_obj_to_show})")
        print(new_obj)

    def do_destroy(self, line):
        """Delete info of an object from storage"""
        storage.reload()
        objs = storage.all()
        if not line.strip():
            print("** class name missing **")
            return
        # all_classes = [obj["__class__"] for obj in objs.values()]
        chosen_class = line.strip().split()[0]
        if line.strip().split()[0] not in all_classes:
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return
        obj_id = line.split()[1]
        all_ids = [obj["id"] for obj in objs.values()]
        if obj_id.strip() not in all_ids:
            print("** no instance found **")
            return
        key = ".".join(line.split())
        del objs[key]  # objs.pop(key)
        storage.save2(objs)

    def do_all(self, line):
        """Display a list of string rep of objects of a specified class"""
        storage.reload()
        objs = storage.all()
        # all_classes = [obj["__class__"] for obj in objs.values()]
        chosen_class = line.strip().split()[0] if line.strip() else ""
        if chosen_class != "" and chosen_class not in all_classes:
            print("** class doesn't exist **")
            return

        list_obj_str = []
        if chosen_class == "":
            for dic in objs.values():
                new_obj = eval(f"{dic['__class__']}(**{dic})")
                list_obj_str.append(str(new_obj))
        else:
            for dic in objs.values():
                if dic["__class__"] == chosen_class:
                    new_obj = eval(f"{chosen_class}(**{dic})")
                    list_obj_str.append(str(new_obj))
        print(list_obj_str)

    def do_update(self, line):
        """Updates an object's attribute"""
        storage.reload()
        objs = storage.all()
        if not line.strip():
            print("** class name missing **")
            return
        # all_classes = [obj["__class__"] for obj in objs.values()]
        chosen_class = line.strip().split()[0]
        if chosen_class not in all_classes:
            print("** class doesn't exist **")
            return
        if len(line.split()) < 2:
            print("** instance id missing **")
            return

        obj_id = line.split()[1]
        all_ids = [obj["id"] for obj in objs.values()]
        if obj_id.strip() not in all_ids:
            print("** no instance found **")
            return
        if len(line.split()) < 3:
            print("** attribute name missing ** ")
            return
        if len(line.split()) < 4:
            print("** value missing **")

        args_list = line.split()
        # update <class name> <id> <attribute name> "<attribute value>"
        obj_id = f"{args_list[0]}.{args_list[1]}"
        attribute = args_list[2]
        value = args_list[3]
        obj_dict = objs[obj_id]
        new_obj = eval(f"{chosen_class}(**{obj_dict})")
        # value = type(getattr(new_obj, attribute))(value)
        setattr(new_obj, attribute, value)
        storage.new(new_obj)
        storage.save()

    def do_exit(self, line):
        """Exits from the program"""
        return True

    def emptyline(self):
        """Handles empty entry + Enter"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
