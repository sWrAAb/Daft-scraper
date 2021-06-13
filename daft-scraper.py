from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location
import pandas as pd
import csv


# credits - https://pypi.org/project/daft-scraper/

def inputs():

    property_type = input('House or Apartment (h/a)')
    if property_type.lower() == 'h':
        property_type = PropertyType.HOUSE
    elif property_type.lower() == 'a':
        property_type = PropertyType.HOUSE
    else:
        print('Invalid input. Please enter h for house or a for apartment.')
        property_type = input('House or Apartment (h/a)')
    
    rent_range = int(input('Maximum rent: '))
    
    bedrooms = int(input('Bedrooms: '))

    options = [    
            PropertyTypesOption([property_type]),   
            PriceOption(0, rent_range),
            BedOption(1, bedrooms)            
            ]


    api = DaftSearch(SearchType.RENT)
    listings = api.search(options)

    return listings

def results(listings):


    search_results = []


    for listing in listings:
        print("(" + str(getattr(listing, 'id')) + ")" + " €" + str(getattr(listing, 'price')) + " " + getattr(listing, 'title')+ "\n" + getattr(listing, 'url'))
        search_results.append([getattr(listing, 'id'), getattr(listing, 'price'), getattr(listing, 'title'), getattr(listing, 'url')])

    return search_results

def CSV_results(search_results):
    search_details = ['id', 'price', 'address', 'url']  
    with open('daft_search_results.csv', 'w') as f: 
        write = csv.writer(f) 
        write.writerow(search_details) 
        write.writerows(search_results) 

CSV_results(results(inputs()))