#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Function that prints basic info about python objects
 * @p: PyObject
 */

void print_python_list(PyObject *p)
{
	int size;
	int alloc;
	int counter;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (counter = 0; counter < size; counter++)
	{
		type = list->ob_item[counter]->ob_type->tp_name;
		printf("Element %d: %s\n", counter, type);

		/*object = PyList_GetItem(p, counter);
		  printf("%s\n", Py_TYPE(object)->tp_name); */
	}
}
