#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int size;
	int alloc;
	int counter;
	PyObject *object;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (counter = 0; counter < size; counter++)
	{
		printf("Element %d: ", counter);

		object = PyList_GetItem(p, counter);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
