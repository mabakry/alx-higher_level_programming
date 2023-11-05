#include <Python.h>
/**
 * print_python_list_info -  prints some basic info about Python lists
 * @p: Python lists
 */

void print_python_list_info(PyObject *p)
{
	int len, i, n;
	PyObject *o;

	len = Py_SIZE(p);
	n = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", n);

	for (i = 0; i < len; i++)
	{
		o = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(o)->tp_name);
	}
}	
