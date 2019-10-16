======================
1-my_list.py
======================

Module defined as MyList that inherits from list

=====================

::

    >>> MyList = __import__('1-my_list').MyList
    >>> my_list = MyList()
    >>> type(my_list)
    <class '1-my_list.MyList'>

::

    >>> print(my_list)
    []

::

    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]

It works when using type()

::

    >>> my_list = MyList([1, 2, 3])
    >>> print(my_list)
    [1, 2, 3]

TypeError when None argument is in the list

::

    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]

It works when adding eleemtne in a given index

::

    >>> my_list[1] = 6
    >>> print(my_list)
    [1, 6, 2, 3, 5]

It works when removing a element using remove function

::

    >>> my_list.remove(6)
    >>> print(my_list)
    [1, 2, 3, 5]

====================

Public instance method defined as print_sorted

=====================

::

    >>> my_list = MyList()
    >>> print(my_list.print_sorted)
    <bound method MyList.print_sorted of []>

It works when appending a list

::

 >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]

::

    >>> my_list.print_sorted
    <bound method MyList.print_sorted of [1, 4, 2, 3, 5]>

TypeError print_sorted when method is given 1 argument

::

    >>> my_list.print_sorted(1)
    Traceback (most recent call last):
    TypeError: print_sorted() takes 1 positional argument but 2 were given

::

    >>> my_list = MyList()
    >>> my_list.append("Edward")
    >>> my_list.append("Ortiz")
    >>> my_list.append("Jhon")
    >>> my_list.append("Doe")
    >>> my_list.append("Mr Puffles")
    >>> print(my_list)
    ['Edward', 'Ortiz', 'Jhon', 'Doe', 'Mr Puffles']

::

    >>> my_list.print_sorted()
    ['Doe', 'Edward', 'Jhon', 'Mr Puffles', 'Ortiz']

::

    >>> my_list = MyList()
    >>> my_list.print_sorted()
    []

::

    >>> my_list = MyList([3, "Edward", "Ortiz", 2])
    >>> my_list.print_sorted()
    Traceback (most recent call last):
    TypeError: unorderable types: str() < int()
