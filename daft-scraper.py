from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location

# credits - https://pypi.org/project/daft-scraper/

def user_inputs():

    property_type = input('House or Apartment (h/a)')
    if property_type == 'h' or property_type == 'H':
        property_type = PropertyType.HOUSE
    elif property_type == 'a' or property_type == 'A':
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

user_inputs()