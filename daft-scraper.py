from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location
import csv


# credits - https://pypi.org/project/daft-scraper/

def inputs():

    property_type = input('House or Apartment (h/a)')
    if property_type.lower() == 'h':
        property_type = PropertyType.HOUSE
    elif property_type.lower() == 'a':
        property_type = PropertyType.APARTMENT
    else:
        print('Invalid input. Please enter h for house or a for apartment.')
        property_type = input('House or Apartment (h/a)')
    
    rent_range = int(input('Maximum rent: '))
    
    bedrooms = int(input('Number of bedrooms: '))

    area = Location.DUBLIN_2_DUBLIN

    options = [    
            PropertyTypesOption([property_type]),   
            PriceOption(0, rent_range),
            BedOption(1, bedrooms),
            LocationsOption([area])            
            ]


    api = DaftSearch(SearchType.RENT)
    listings = api.search(options)

    return listings

def results(listings):


    rows = []

    for listing in listings:
        # Print results in terminal
        print("(" + str(getattr(listing, 'id')) + ")" + " €" + str(getattr(listing, 'price')) + " " + getattr(listing, 'title')+ "\n" + getattr(listing, 'url'))
        # Print results in csv file
        rows.append([getattr(listing, 'id'), getattr(listing, 'price'), getattr(listing, 'title'), getattr(listing, 'url')])

    return rows

def print_results_to_csv(rows):

    #credits https://www.geeksforgeeks.org/python-save-list-to-csv/

    with open('daft_search_results.csv', 'w') as f:    
        fields = ['Id','Price','Address', 'Url']
        # using csv.writer method from CSV package
        write = csv.writer(f)    
        write.writerow(fields)
        write.writerows(rows)


print_results_to_csv(results(inputs()))