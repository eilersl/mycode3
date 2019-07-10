#!/usr/bin/env python3
import urllib.request
import json

## Define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=eolSbbCwrvK38KbX5pdCzuJTBYJZ0XBJwWuXgaQ1' ## your key goes in place of DEMO_KEY

neourl = neourl + startdate + mykey

## call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeneo)
