import time

# my imports
from search_loader import search_loader
from search_offers import search_offers
# from process_search_results import remove_duplicates


# generates link list using search_loader.py from a csv file
link_list = search_loader(".\data\data_short.csv")

# searches offers using link list generated before, and saves it to specified location
while True:
    # time measurement
    start_time = time.time()

    search_offers(link_list)

    # time measurement
    end_time = time.time()
    print(str(round(end_time - start_time, 2)) + " seconds")
    print(str(len(link_list)) + " offers")
    print(str(round((end_time - start_time) / len(link_list), 2)) + " seconds/offer")
