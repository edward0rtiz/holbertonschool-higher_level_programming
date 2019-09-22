#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - Function that prints basic info about python objects
 * @p: PyObject
 */

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);


void print_python_list(PyObject *p)
{
	long int size, b, alloc;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (b = 0; b < size; b++)
	{
		type = list->ob_item[b]->ob_type->tp_name;
		printf("Element %ld: %s\n", b, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[b]);
	}
}

/**
 * print_python_bytes - Fucntion that prints basic info of python bytes
 * @p: Pyobject of byte CPython structure
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	long int size, c;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf(" first %ld bytes: ", size);
	for (c = 0; c < size; c++)
	{
		printf("%02hhx", bytes->ob_sval[c]);
		if (c == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
