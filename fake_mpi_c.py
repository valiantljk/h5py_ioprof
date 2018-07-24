import h5py
import time
import numpy
import os,sys
import ioprof
from ioprof import MPI_Init, MPI_Finalize
datadir="/global/cscratch1/sd/ftc/deep_learning_data/climate_deep_learn"
input_list= os.listdir(datadir)
print ('climate/data, climate/labels, climate/stats')
MPI_Init()
#def MPI_Init():
#    print("fake mpi init")

#def MPI_Finalize():
#    print("fake mpi finalize")

def h5py_read(file_name,dset_name):
    with h5py.File(file_name, 'r') as fx:
         try: 
            dset=fx[dset_name][:]
         except Exception as e:
            print ("file:%s,dset:%s reading error\n"%(file_name,dset_name))
            print (e)
def main():
    print (MPI_Init())
    print ("reading %d files, dsetname:%s"%(int(sys.argv[1]),sys.argv[2]))
    num_read=int(sys.argv[1])
    start = time.time()
    while (num_read>0):
        fname=datadir+"/"+input_list[num_read]
        #print ('reading:%s'%fname)
        h5py_read(fname,sys.argv[2])
        num_read-=1
    end = time.time()
    print ("Total read time: %f\n"%(end-start))
    print (MPI_Finalize())

if __name__ =="__main__":
    #from ioprof import MPI_Init, MPI_Finalize
    #print (ioprof.__file__)
    #print sys.path
    #MPI_Init()
    main()
    #MPI_Finalize()
