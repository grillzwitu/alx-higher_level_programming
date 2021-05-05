#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Entry Point
 *
 * @p: pointer to python object/list
 *
 * Description: Prints some basic info about python lists
 */

void print_python_list_info(PyObject *p)
{
	long int len, i = 0;
	PyObject *obj;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	while (i < len)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
