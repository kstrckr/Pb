import csv
import re

class Event:

    calendar_string = ''
    category = ''
    sale_id = ''
    name = ''
    underscore_name = ''
    date = ''
    date_digits = 0
    


    def __init__(self, gcal_string):
        self.calendar_string = gcal_string
        pattern = '(?P<category>\D{4}(\s\D{4})?)\s(?P<sale_id>\d{10})\s(?P<name>[\D*\s]*(?=\sPO|\sTO|\sPRO)).*(?P<date>(\d{2}/){2}\d{2})'
        parse_gcal = re.search(pattern, self.calendar_string)
        self.category = parse_gcal.group('category')
        self.sale_id = parse_gcal.group('sale_id')
        self.name = parse_gcal.group('name')
        self.underscore_name = self.name.replace(' ', '_')
        self.date = parse_gcal.group('date')
        self.date_digits = self.date.replace('/', '')


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

    def __str__(self):
        output = '{}_{}_{}_{}'.format(self.date_digits, self.underscore_name, self.sale_id, self.category,)
        return output