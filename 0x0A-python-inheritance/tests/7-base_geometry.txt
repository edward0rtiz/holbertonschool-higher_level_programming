======================
7-base_geometry.py
======================

Module defined as base_geometry class used second blueprint

=====================

>>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
>>> bg = BaseGeometry()
>>> bg.integer_validator("string", 7)
>>> bg.integer_validator("name", 12)
>>> bg.integer_validator("age", 0)
Traceback (most recent call last):
...
ValueError: age must be greater than 0
>>> bg.integer_validator("name", "Edward")
Traceback (most recent call last):
...
TypeError: name must be an integer
>>> bg.integer_validator("name", [1])
Traceback (most recent call last):
...
TypeError: name must be an integer
>>> bg.integer_validator("name", {2,3})
Traceback (most recent call last):
...
TypeError: name must be an integer
>>> bg.integer_validator("name", (7, ))
Traceback (most recent call last):
...
TypeError: name must be an integer
>>> bg.integer_validator("name", None)
Traceback (most recent call last):
...
TypeError: name must be an integer
>>> bg.integer_validator("num", "3")
Traceback (most recent call last):
...
TypeError: num must be an integer
>>> bg.integer_validator("negative", -1)
Traceback (most recent call last):
...
ValueError: negative must be greater than 0
>>> bg.integer_validator("float", 2.2)
Traceback (most recent call last):
...
TypeError: float must be an integer
>>> bg.integer_validator("negative2", -1.2)
Traceback (most recent call last):
...
TypeError: negative2 must be an integer
>>> bg.integer_validator("bool", True)
Traceback (most recent call last):
...
TypeError: bool must be an integer
>>> bg.integer_validator("age")
Traceback (most recent call last):
...
TypeError: integer_validator() missing 1 required positional argument: 'value'
>>> bg.area()
Traceback (most recent call last):
...
Exception: area() is not implemented
