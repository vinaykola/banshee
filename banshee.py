from __future__ import division
import numpy as np
import sys
import os.path
import cPickle as pickle

size = (1090727,31)

def load_variable(f_name,compute,*args):
    if os.path.isfile(f_name):
        with open(f_name,'rb') as f:
            a = pickle.load(f)
    else:
        a = compute(*args)
        with open(f_name,'wb') as f:
            pickle.dump(a,f)
    return a
                                                                            

#Features:
# 'tweet_id'          0   0
# 'tweet_tweetId'     1   1
# 'tweet_userId'      2   2
# 'tweet_artistId'    3   3
# 'tweet_trackId'     4   4
# 'tweet_datetime'    5   -
# 'tweet_unixtime'    6   5
# 'tweet_weekday'     7   6
# 'tweet_longitude'   8   7
# 'tweet_latitude'    9   8
# 'artist_mbid'       10  9
# 'artist_name'       11  10
# 'track_title'       12  11
# 'track_7digitalId'  13  12
# 'amazon_asin'       14  13
# 'amazon_albumAsin'  15  13
# 'country'           16  15
# 'state'             17  16
# 'county'            18  17
# 'city'              19  18
# 'postalCode'        20  19
# 'street'            21  -
# 'timezone'          22  20
# 'countryName'       23  21
# 'isoAlpha3'         24  22
# 'fipsCode'          25  -
# 'continent'         26  23
# 'continentName'     27  -
# 'capital'           28  -
# 'areaInSqKm'        29  24
# 'population'        30  25
# 'currencyCode'      31  -
# 'languages'         32  26
# 'west'              33  27
# 'north'             34  28
# 'east'              35  29
# 'south'             36  30
flist = [0,1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,26,29,30,32,33,34,35,36]
d_types = []

d_types += [np.int,np.int,np.int,np.int,np.int,np.int,np.int,np.float,np.float]

d_types += ['a50','a32','a32',np.int]

d_types += ['a32','a32']

d_types += ['a4','a32','a32','U2','a32','a6']

d_types += ['a32','a3','a4',np.int,np.int]

d_types += ['a32']

d_types += [np.float,np.float,np.float,np.float]

cols = len(flist)
rows = 1090727

# with open('mmtd.txt','r') as f:
#     for i,line in enumerate(f):
#         if i == 0:
#             features = line.split('\t')
#             print features
#             features = features[0:5] + features[6:37]
#             dtypes = zip(features,d_types)
#             print len(dtypes)
#             print dtypes
#             print cols
#             mmtd = np.recarray((rows/2,cols),dtype=dtypes)
#             #sys.exit()
#         else:
#             values = line.split('\t')
#             length = len(values[1])
#             if length > maxlen:
#                 maxlen = length
#             for k,feature_number in enumerate(flist):
#                 try:
                    
#                     if k == 0:
#                         print type(int(values[feature_number]))
#                         mmtd[i-1,k] = int(values[feature_number])
#                         print i-1, k, mmtd[i-1,k], values[feature_number]
#                         raw_input()
#                     else:
#                         pass
#                         mmtd[i-1,k] = values[feature_number]
#                 except:
#                     print 'fuck'
#                     break

flist = tuple(flist)

def parse_mmtd(flist):

    return np.genfromtxt('mmtd.txt',names=True,usecols=flist,delimiter='\t',invalid_raise=False,dtype=None)

mmtd = load_variable('/home/vinaykola/vinaykola/Acads/CSS/mmtd.pkl',parse_mmtd,flist)



