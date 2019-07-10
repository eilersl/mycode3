#!/usr/bin/env python3
import requests ## 3rd party URL lookup

## define the main function
def  main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2019-07-09' ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=eolSbbCwrvK38KbX5pdCzuJTBYJZ0XBJwWuXgaQ1'

    neourl = neourl + startdate = mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()
