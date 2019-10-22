#!/usr/bin/python3
"""Module of Base"""

import json
import csv


class Base:
    """Type class for base"""

    __nb_objects = 0

    def __init__(self, id=None):
    """__init function"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file function"""

        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write('')
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string function"""

        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create function"""

        new_instance = cls(5, 5)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """load_from_file function"""

        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, 'r') as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv function"""

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None:
                f.write("")
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""

        filename = cls.__name__ + '.csv'
        try:
            with open(filename, 'r', newline='') as csvfile:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dictionaries = csv.DictReader(csvfile,
                                                   fieldnames=fieldnames)
                list_dictionaries = [dict([i, int(j)]for i, j in dicti.items())
                                     for dicti in list_dictionaries]
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []
