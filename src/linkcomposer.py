# composes final link used in the OLXBot link format is
# olx.pl/<primary_category>/<secondary_category>/<subcategory>/<localization>/q-<query>/?search%5Bdist%5D=<distance>
# &search%5Bfilter_float_price:from%5D=<min_price>&search%5Bfilter_float_price:to%5D=(max_price))

def linkcomposer(primary_category=None, secondary_category=None, subcategory=None,
                 localization=None, query=None, distance=None, min_price=None, max_price=None):

    final_query = "https://www.olx.pl/"

    if primary_category and secondary_category and subcategory is (None or 0):
        final_query += "oferty/"
    else:
        if primary_category is not (None or 0 or ''):
            final_query += (primary_category + "/")

        if secondary_category is not (None or 0 or ''):
            final_query += (secondary_category + "/")

        if subcategory is not (None or 0 or ''):
            final_query += (subcategory + "/")


    if localization is not (None or 0 or ''):
        final_query += (localization + "/")

    if query is not (None or 0 or ''):
        final_query += ("q-" + query + "/")

    final_query += "?search"

    addand = False

    if distance is not (None or 0 or ''):
        final_query += ("%5Bdist%5D="+distance)

        if addand is True:
            final_query += ("&search")
        addand = True

    if min_price is not (None or 0 or ''):

        if addand is True:
            final_query += ("&search")
        addand = True

        final_query += ("%5Bfilter_float_price:from%5D="+min_price)

    if max_price is not (None or 0 or ''):

        if addand is True:
            final_query += ("&search")
        addand = True

        final_query += ("%5Bfilter_float_price:to%5D="+max_price)

    return final_query
