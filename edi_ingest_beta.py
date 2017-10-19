import csv
import re

class Event:

    __init__(self, gcal_string):
        pattern = '(?P<category>\D{4}(\s\D{4})?)\s(?P<sale_id>\d{10})\s(?P<name>[\D*\s*]*)'
        parse_gcal = re.search()

    metadata_fields = {
        'CPRO:Art Director': None,
        'CPRO:Shoot Date': None,
        'CPRO:Photographer': None,
        'CPRO:Stylist': None,
        'CPRO:Studio': None,
        'CPRO:Original Sale ID': None,
        'PRTD:Brand': None,
        'PRTD:Product Catagory': None, 
    }