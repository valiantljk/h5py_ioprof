#include<Python.h>
static PyObject* MPI_Init(PyObject * self){
 return Py_BuildValue("s", "Hello, Fake MPI Init!!");
}

static PyObject* MPI_Finalize(PyObject * self){
 return Py_BuildValue("s", "Hello, Fake MPI Finalize!!");
}

static PyMethodDef ioprof_MPI_Init[] ={
 {"MPI_Init", (PyCFunction)MPI_Init, METH_NOARGS, NULL},{NULL}
};

static PyMethodDef ioprof_MPI_Finalize[] ={
 {"MPI_Finalize", (PyCFunction)MPI_Finalize, METH_NOARGS, NULL},{NULL}
};

void initioprof(void){
 Py_InitModule3("ioprof",ioprof_MPI_Init, NULL);
 Py_InitModule3("ioprof", ioprof_MPI_Finalize, NULL);
}
