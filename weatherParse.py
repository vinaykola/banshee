import csv
from geopy.geocoders import GoogleV3


geolocator = GoogleV3()
address, (latitude, longitude) = geolocator.reverse("40.752067, -73.977578")
print(address, latitude, longitude)
#77 East 42nd Street, New York, NY 10017, USA 40.7520802 -73.9775683
address.split(',')[-1]
address.split(',')[-2].split(' ')[-1]