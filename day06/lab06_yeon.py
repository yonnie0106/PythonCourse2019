# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 


import imp
import sys

sys.path.insert(0, '/Users/yonni/Desktop/Secret')
imported_items = imp.load_source('goog', '/Users/yonni/Desktop/Secret/start_google.py')

gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location = gmaps.geocode(whitehouse)
latlong = location[0]['geometry']['location'] # lat. and long. of the white house


## 1) The closest Embassy
embassies = [[38.917228,-77.0522365], [38.9076502, -77.0370427], [38.916944, -77.048739] ]
embassies_dicts = []
for i in range(len(embassies)):
	embassies_dicts.append({'lat' : embassies[i][0], 'lng' : embassies[i][1]})
	distance = gmaps.distance_matrix(embassies_dicts[i], latlong)
	print(distance['rows'][0]['elements'][0]['distance']['text']) # the second embassy closest to the White House

closest_embassy = gmaps.reverse_geocode(embassies_dicts[1])
closest_embassy_address = closest_embassy[0]['formatted_address'] # the address of the second embassy 
print(closest_embassy_address)



## 2) Cafe
cafes  = gmaps.places_nearby(embassies_dicts[1], 500, type = "cafe", keyword = "breakfast")
print(type(cafes))
print(cafes.keys())
print(len(cafes))
for i in range(len(cafes["results"])):
	cafe_latlong = cafes["results"][i]["geometry"]["location"]
	cafe_distance = gmaps.distance_matrix(embassies_dicts[1], cafe_latlong)
	print(cafe_distance['rows'][0]['elements'][0]['distance']['text'])



#	print(len(cafes["results"])





