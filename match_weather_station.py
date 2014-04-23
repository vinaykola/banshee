from __future__ import division
import cPickle as pickle
from geopy.geocoders import GoogleV3
from math import sin, cos, sqrt, atan2, radians
import numpy as np
import datetime
import os.path
import sys

global fcounts
fcounts = {}
fcounts['PRCP'] = 0
fcounts['SNOW'] = 0
fcounts['TMAX'] = 0
fcounts['TMIN'] = 0

geolocator = GoogleV3()

def load_station_coords(fname):

    coords = {}

    with open(fname,'r') as f:
        for line in f:
            values = line.split()
            name = values[0]
            lat = values[1]
            longi = values[2]
            coords[name] = (float(lat),float(longi))

    return coords


# Returns dist in km
def dist(c1,c2):
    R = 6373.0
    lat1,lon1 = radians(c1[0]),radians(c1[1])
    lat2,lon2 = radians(c2[0]),radians(c2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c
        


def get_weather_station(source,coords):

    min_dist = 1000000
    min_dist_stn = None
    for name,coord in coords.iteritems():
        d = dist(source,coord)
        if d < min_dist:
            min_dist = d
            min_dist_stn = name

    return min_dist_stn,min_dist

def loadMMTD():
    DATA_LOC = '/home/vinaykola/vinaykola/Acads/CSS/data/mmtd-subset-3000.pkl'
    with open(DATA_LOC,'r') as f:
        arr = pickle.load(f)
    return arr

def get_weather(stn,year,month,day):
    print stn
    fname = './datasets/us_trunc_data/' + stn + '.dly.trunc'
    features = ['PRCP','SNOW','TMAX','TMIN']
    data ={}
    for feature in features:
        data[feature] = None
    if not os.path.isfile(fname):
        return None
    else:
        with open(fname,'r') as f:
            for line in f:
                feature = line[17:21]
                line_stn = line[:11]
                line_year = line[11:15]
                line_month = line[15:17]
                if int(year) == int(line_year) and int(month) == int(line_month) and feature in features:
                    data[feature] = getvalue(line,day)
                    fcounts[feature] += 1
                    #raw_input()
                #print line

    print data
    raw_input()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def getvalue(line,day):
    splits = line.split()
    new_splits = []
    for split in splits:
        
        if len(split) > 5:
            idx = split.find('-9999')
            if idx != -1:
                if is_number(split[:idx]):
                    new_splits.append(split[:idx])
                if is_number(split[idx:]):
                    new_splits.append(split[idx:])
            else:
                if is_number(split):
                    new_splits.append(split)
                elif is_number(split[:-1]):
                    new_splits.append(split[:-1])
        else:
            if is_number(split):
                new_splits.append(split)
            elif is_number(split[:-1]):
                new_splits.append(split[:-1])
                
    print line
    print new_splits
    if len(new_splits) == 31:
        x = int(new_splits[int(day)])
        if x != -9999:
            return x
        else:
            return None
    elif len(new_splits) == 62:
        x = int(new_splits[2*int(day)])
        if x != -9999:
            return x
        else:
            return None
    else:
        x = int(new_splits[int(day)])
        if x != -9999:
            return x
        else:
            return None

    
    
                    
    
def main():
    test = (46.6670,41.550)
    test = (42.8679,-101.4056)
    coords = load_station_coords('./datasets/ghcnd-stations-us.txt')

    mmtd = loadMMTD()
    size =  mmtd.shape

    for i in xrange(size[0]):
        tweet_time = mmtd[i]['tweet_unixtime']

        date = datetime.datetime.fromtimestamp(int(tweet_time))
        year = date.year
        month = date.month
        day = date.day
        source = (mmtd[i]['tweet_latitude'],mmtd[i]['tweet_longitude'])
        stn,dist = get_weather_station(source,coords)
        stn = stn.upper()
        weather_data = get_weather(stn,year,month,day)

    print fcounts
        
if __name__ == '__main__':
    main()
