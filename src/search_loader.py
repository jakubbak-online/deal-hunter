import csv


def link_composer(
    primary_category=None,
    secondary_category=None,
    subcategory=None,
    subsubcategory=None,
    localization=None,
    query=None,
    distance=None,
    min_price=None,
    max_price=None,
    condition=None,
):
    final_query = "https://www.olx.pl/"
    empty = None or 0 or ""

    # https://www.olx.pl/elektronika/fotografia/obiektywy/Gdynia/q-Sigma/?search%5Bdist%5D=2&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_float_price%3Afrom%5D=50&search%5Bfilter_float_price%3Ato%5D=500&search%5Border%5D=created_at%3Adesc
    # https://www.olx.pl/elektronika/fotografia/obiektywy/Gdynia/q-Sigma/?search%5Bdist%5D=2&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_float_price%3Afrom%5D=50&search%5Bfilter_float_price%3Ato%5D=500&search%5Border%5D=created_at%3Adesc

    if primary_category and secondary_category and subcategory is (None or 0):
        final_query += "oferty/"
    else:
        if primary_category is not empty:
            final_query += primary_category + "/"

        if secondary_category is not empty:
            final_query += secondary_category + "/"

        if subcategory is not empty:
            final_query += subcategory + "/"

        if subsubcategory is not empty:
            final_query += subsubcategory + "/"

    if localization is not empty:
        final_query += localization + "/"

    if query is not empty:
        final_query += "q-" + query + "/"

    final_query += "?"

    if distance is (empty or not (0 or 2 or 5 or 10 or 15 or 30 or 50 or 75 or 100)):
        print(len(distance))
        print(
            "Błędnie wprowadzony dystans w wyszukiwaniu! Użyj jednej z tych wartości: "
            "0, 2, 5, 10, 15, 30, 50, 75, 100"
        )
        distance = None
    if distance is not empty:
        if final_query[-1] != "?":
            final_query += "&"
        final_query += f"search" f"%5Bdist%5D={distance}"

    if condition is not empty:
        if final_query[-1] != "?":
            final_query += "&"
        final_query += f"search" f"%5Bfilter_enum_state%5D%5B0%5D={condition}"

    if min_price is not empty:
        if final_query[-1] != "?":
            final_query += "&"
        final_query += f"search" f"%5Bfilter_float_price%3Afrom%5D={min_price}"

    if max_price is not empty:
        if final_query[-1] != "?":
            final_query += "&"
        final_query += f"search" f"%5Bfilter_float_price%3Ato%5D={max_price}"

    if final_query[-1] != "?":
        final_query += "&"
    final_query += "search" "%5Border%5D=created_at%3Adesc"

    return final_query


def search_loader(data):
    linklist = []

    with open(data) as f:
        dict_reader_object = list(csv.reader(f, delimiter=","))
        dict_reader_object.pop(0)

        for row in dict_reader_object:
            link = link_composer(
                primary_category=row[0],
                secondary_category=row[1],
                subcategory=row[2],
                subsubcategory=row[3],
                localization=row[4],
                query=row[5],
                distance=row[6],
                min_price=row[7],
                max_price=row[8],
                condition=row[9],
            )

            linklist.append(link)

    return linklist
