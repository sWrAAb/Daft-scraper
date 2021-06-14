# Import library - https://pypi.org/project/daft-scraper/
from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location
import csv
import datetime

# Date and time now

now = datetime.datetime.now()

# Global variables

listings = None
rows = []

# User inputs
def inputs():
    global listings

    # Property type
    property_type = input('House or Apartment (h/a): ')
    if property_type.lower() == 'h':
        property_type = PropertyType.HOUSE
    elif property_type.lower() == 'a':
        property_type = PropertyType.APARTMENT
    else:
        print('Invalid input. Please enter h for house or a for apartment.')
        property_type = input('House or Apartment (h/a): ')

    # Maximum rent
    rent_range = int(input('Maximum rent: '))
    
    # Maximum number of bedrooms
    bedrooms = int(input('Maximum number of bedrooms: '))

    # CCT college area
    area = Location.DUBLIN_2_DUBLIN

    # Search parameters
    options = [    
            PropertyTypesOption([property_type]),   
            PriceOption(0, rent_range),
            BedOption(1, bedrooms),
            LocationsOption([area])            
            ]


    api = DaftSearch(SearchType.RENT)
    listings = api.search(options)

    return listings

# Sorting and printing results into terminal and CSV file

def results(listings):

    # Credits - https://stackoverflow.com/questions/3766633/how-to-sort-with-lambda-in-python

    sorted_list = sorted(list(listings), key=lambda a: a.price, reverse=False)

    for listing in sorted_list:
        # Print results in terminal
        print(now.strftime("%d-%m-%Y %H:%M") + ' ' + str(getattr(listing, 'id')) + " " + " €" + str(getattr(listing, 'price')) + " " + getattr(listing, 'title')+ "\n" + getattr(listing, 'url'))
        # Print results in csv file
        rows.append([now.strftime("%d-%m-%Y %H:%M"),getattr(listing, 'id'), getattr(listing, 'price'), getattr(listing, 'title'), getattr(listing, 'url')])

    if not rows:
        print("\n No results match your search criteria!\n")

    return rows

def print_results_to_csv(rows):

    # credits https://www.geeksforgeeks.org/python-save-list-to-csv/

    with open('daft_search_results.csv', 'w') as f: 
        # Columns   
        fields = ['Time','Id','Price','Address', 'Url']
        # using csv.writer method from CSV package
        write = csv.writer(f)    
        # Write columns
        write.writerow(fields)
        # Write rows
        write.writerows(rows)

# Prints result to csv file
print_results_to_csv(results(inputs()))