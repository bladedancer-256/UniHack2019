import googlemaps
import json
from datetime import datetime

#fp = open("keys.json").read()
#GOOGLE_API_KEY = json.loads(fp)["API"]
#gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

#converting from dictionary and json object purely for the sake of
#readabiliy and testing
def getAddressFromCoordinates(client, c):

	cParsed = json.dumps(client.reverse_geocode(c)[0], indent = 4, sort_keys = True)

	cDict = json.loads(cParsed)

	address = cDict['formatted_address']

	return address

#takes the coordinate and returns a tuple of time and distance
def getTimeAndDistance(client, origin, destination):

	origin = getAddressFromCoordinates(client, origin)
	destination = getAddressFromCoordinates(client, destination)

	matrix = client.distance_matrix([origin],
									[destination],
									mode ='walking')


	parsedMatrix = json.dumps(matrix, indent = 4, sort_keys = True)
	matrixDict = json.loads(parsedMatrix)
	distance = 	matrixDict['rows'][0]['elements'][0]['distance']['text']
	time = matrixDict['rows'][0]['elements'][0]['duration']['text']

	return (time, distance)



