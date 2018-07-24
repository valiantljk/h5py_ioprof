#!/bin/bash
module load python 
module load darshan 
python setup.py install --user
export PYTHONPATH="${PYTHONPATH}:$HOME/.local/cori/2.7-anaconda-4.4/lib/python2.7/site-packages/"
export LD_PRELOAD=/usr/common/software/darshan/3.1.4/lib/libdarshan.so:$HOME/.local/cori/2.7-anaconda-4.4/lib/python2.7/site-packages/ioprof.so:/usr/common/software/python/2.7-anaconda-4.4/lib/libhdf5.so:$LD_PRELOAD
export PMI_NO_FORK=1
export PMI_NO_PREINITIALIZE=1

python fake_mpi_c.py 10 climate/data
