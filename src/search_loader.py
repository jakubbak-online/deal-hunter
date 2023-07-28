import csv


def link_composer(primary_category=None, secondary_category=None, subcategory=None,
                  localization=None, query=None, distance=None, min_price=None, max_price=None):
    final_query = "https://www.olx.pl/"

    # https://www.olx.pl/muzyka-edukacja/ksiazki/ksiazki-naukowe/jastrzebie-zdroj/q-python/?search%5Bdist%5D=30&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:to%5D=50
    # https://www.olx.pl/muzyka-edukacja/ksiazki/ksiazki-naukowe/jastrzebie-zdroj/q-python/?search%5Border%5D=created_at:desc&search%5Bdist%5D=25&search%5Bfilter_float_price:to%5D=50
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

    final_query += "?"


    if distance is not empty:
        final_query += ("&search[dist]=" + distance)
    addand = True

    final_query += "&search[order]=created_at:desc"

    if min_price is not empty:
        if addand is True:
            final_query += "&search"
        addand = True
        final_query += ("[filter_float_price:from]=" + min_price)

    if max_price is not empty:
        if addand is True:
            final_query += "&search"

        final_query += ("[filter_float_price:to]=" + max_price)

    return final_query


def search_loader(data):
    linklist = []

    with open(data) as f:
        dict_reader_object = list(csv.reader(f, delimiter=","))
        dict_reader_object.pop(0)

        for row in dict_reader_object:

            link = link_composer(primary_category=row[0],
                                 secondary_category=row[1],
                                 subcategory=row[2],
                                 localization=row[3],
                                 query=row[4],
                                 distance=row[5],
                                 min_price=row[6],
                                 max_price=row[7])

            linklist.append(link)

    return linklist
