import cPickle as pickle
from geopy.geocoders import GoogleV3
from math import sin, cos, sqrt, atan2, radians

geolocator = GoogleV3()
coords = []

with open('./datasets/ghcnd-stations-us.txt') as f:
    for line in f:
        values = line.split()
        
        lat = values[1]
        longi = values[2]
        if lat == '' or longi == '':
            print values
        print 'lat',lat,'long',longi,
        coords.append((float(lat),float(longi)))
        # add = str(lat) + ', ' + str(longi)
        # print add
        # try:
        #     address, (latitude, longitude) = geolocator.reverse(str(lat)+', '+str(long))[0]
        #     #print(address, latitude, longitude)
        #     #77 East 42nd Street, New York, NY 10017, USA 40.7520802 -73.9775683
        #     print address
        #     print address.split(',')[-1],
        #     print address.split(',')[-2].split(' ')[-1]
        # except:
        #     #print address
        #     raw_input()

def dist(c1,c2):
    R = 6373.0
    lat1,lon1 = radians(c1[0]),radians(c1[1])
    lat2,lon2 = radians(c2[0]),radians(c2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c
        
test = (46.6670,41.550)

for i in xrange(200):
    print i
    for coord in coords:
        d = dist(test,coord)
