from distutils.core import setup, Extension
setup(name='ioprof', version='1.0',  \
      ext_modules=[Extension('ioprof', ['fake_mpi.c'])])
