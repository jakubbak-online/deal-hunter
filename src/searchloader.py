# loads csv file, and uses linkcomposer

import csv
from linkcomposer import linkcomposer
def searchloader():
    linklist = []

    with open('data.csv') as f:
        DictReaderObject = csv.DictReader(f)


        for row in DictReaderObject:
            search = dict(row)


            link = linkcomposer(primary_category=search['primary_category'],
                                secondary_category=search['secondary_category'],
                                subcategory=search['subcategory'],
                                localization=search['localization'],
                                query=search['query'],
                                distance=search['distance'],
                                min_price=search['min_price'],
                                max_price=search['max_price'])

            linklist.append(link)

    return linklist

