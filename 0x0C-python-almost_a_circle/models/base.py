#!/usr/bin/python3
"""
    Implements the base class.
"""
import json
import csv


class Base:
    """
        A class base that manages the id attribute for all the classes.
        Arguments:
            @id: The id of an instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
           Initializes the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Converting a dict into a json string
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            Returns a dict from a string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the string representation of an object of a class
            into a file
        """
        file_name = cls.__name__ + ".json"

        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)

        with open(file_name, mode="w") as fd:
            json.dump(content, fd)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with all the attributes already set
        """

        if cls.__name__ == "Rectangle":
            r2 = cls(1, 1)
        elif cls.__name__ == "Square":
            r2 = cls(1)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        """
            loading dict representing the parameters for
            and instance and from that creating instances
        """
        file_name = cls.__name__ + ".json"
        content = []

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
            for i, e in enumerate(content):
                content[i] = cls.create(**content[i])
        except:
            pass
        return content

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Opens a window and draws all the squares and rectangles
        """
        import turtle

        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("black")
        turtle.color("teal")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Serializes a list of Rectangles or Squares in csv
        """
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode="w", newline='', encoding="UTF8") as csvf:
            write_csv = csv.writer(csvf)

            if cls.__name__ == "Rectangle":
                for item in list_objs:
                    write_csv.writerow([item.id, item.width, item.height,
                                        item.x, item.y])

            if cls.__name__ == "Square":
                for item in list_objs:
                    write_csv.writerow([item.id, item.size, item.x, item.y])

    @classmethod
    def load_from_file_csv(cls):
        """
            Deserializes a list of Rectangles or Squares in csv
        """
        file_name = cls.__name__ + ".csv"

        li_st = []
        try:
            with open(filename, 'r') as csvf:
                csv_reader = csv.reader(csvf)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    li_st.append(obj)
        except:
            pass
        return li_st
