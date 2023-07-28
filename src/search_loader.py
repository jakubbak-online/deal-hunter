import csv


def link_composer(primary_category=None, secondary_category=None, subcategory=None,
                  localization=None, query=None, distance=None, min_price=None, max_price=None):
    final_query = "https://www.olx.pl/"

    empty = (None or 0 or '')

    if primary_category and secondary_category and subcategory is (None or 0):
        final_query += "oferty/"
    else:
        if primary_category is not empty:
            final_query += (primary_category + "/")

        if secondary_category is not empty:
            final_query += (secondary_category + "/")

        if subcategory is not empty:
            final_query += (subcategory + "/")

    if localization is not empty:
        final_query += (localization + "/")

    if query is not empty:
        final_query += ("q-" + query + "/")

    final_query += "?search%5Border%5D=created_at:desc&"

    addand = False

    if distance is not empty:
        final_query += ("%5Bdist%5D=" + distance)

        if addand is True:
            final_query += "&search"
        addand = True

    if min_price is not empty:
        if addand is True:
            final_query += "&search"
        addand = True
        final_query += ("%5Bfilter_float_price:from%5D=" + min_price)

    if max_price is not empty:
        if addand is True:
            final_query += "&search"

        final_query += ("%5Bfilter_float_price:to%5D=" + max_price)

    return final_query


def search_loader(data):
    linklist = []

    with open(data) as f:
        dict_reader_object = csv.DictReader(f)

        for row in dict_reader_object:
            search = dict(row)

            link = link_composer(primary_category=search['primary_category'],
                                 secondary_category=search['secondary_category'],
                                 subcategory=search['subcategory'],
                                 localization=search['localization'],
                                 query=search['query'],
                                 distance=search['distance'],
                                 min_price=search['min_price'],
                                 max_price=search['max_price'])

            linklist.append(link)

    return linklist
