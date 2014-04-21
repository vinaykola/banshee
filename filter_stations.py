from __future__ import division
import os
import cPickle as pickle

data_path = './datasets/us_trunc_data/'
files = os.listdir(data_path)
stations = [filename[:-10] for filename in files]

filename = './datasets/ghcnd-stations.txt'

with open(filename,'r') as f:
    with open(filename+'_trunc','w') as f1:
        for line in f:
            stn = line[:11]
            if stn in stations:
                f1.write(line)
