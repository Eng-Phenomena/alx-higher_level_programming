#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - prints info of python lists
 * @p: Pyobject 
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *object;

	printf("[*] Size of the Python List = %d\n", Py_SIZE(p));
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);
		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
