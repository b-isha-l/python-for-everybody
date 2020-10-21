"""
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse
that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely
identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as
often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the
address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in
http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. You will get different results
from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a
place_id of "ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2290 characters
Place id ChIJJ2MNmPl_bIcRt8t5x-X5ZhQ
Turn In

Please run your program to find the place_id for this location:

Smolensk State University
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below.
Hint: The first seven characters of the place_id are "ChIJD5y ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should
work with the Google API - but the place_id may not match for this assignment.
"""

import urllib.request, urllib.parse, urllib.error
import json, ssl

api_key = False
if api_key is False:
    api_key = 42  # using this api key and url
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = None
ctx.verify_mode = ssl.CERT_NONE

# input for location
address = input("Enter location: ")
if len(address)<1:
    "break"

parametr = dict()
parametr["address"] = address  # store address into parameter
if api_key is not False:
    parametr["key"] = api_key  # store api key into parameter
url = service_url + urllib.parse.urlencode(parametr)  # make actual url to retrieve service url + address + api key

print("Retrieving ", url)
url_hand = urllib.request.urlopen(url, context=ctx)
data = url_hand.read().decode()
print("Retrieved ", len(data), "characters")

try:
    js = json.loads(data)  # load json data into js
except:
    js = None

# show error message and display data
if not js or "status" not in js or js["status"] != "OK":
    print("--- Failure To Retrieve ---")
    print(data)
    "continue"

# find for place id and display as result
place_id = js["results"][0]["place_id"]
print("Place Id ", place_id)