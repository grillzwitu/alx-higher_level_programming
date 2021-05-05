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
	size_t len, i = 0;
	PyObject *obj;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %u\n", (unsigned) sizeof(len));
	printf("[*] Allocated = %u\n",
	       (unsigned) sizeof((PyListObject *)p)->allocated);
	while (i < len)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %u: %s\n",
		       (unsigned) sizeof(i), Py_TYPE(obj)->tp_name);
		i++;
	}
}
