#!/bin/bash
module load python 
module load darshan 
export LD_PRELOAD=/usr/common/software/darshan/3.1.4/lib/libdarshan.so:/usr/common/software/python/2.7-anaconda-4.4/lib/libhdf5.so:$LD_PRELOAD
export PMI_NO_FORK=1
export PMI_NO_PREINITIALIZE=1
python fake_mpi.py 10 climate/data
