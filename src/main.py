import time

# my imports
from search_loader import search_loader
from search_offers import search_offers


# generates link list using search_loader.py from a csv file
link_list = search_loader(".\data\data_very_long.csv")


while True:
    # time measurement
    start_time = time.time()

    search_offers(link_list)

    # time measurement
    end_time = time.time()
    print(f"\nSearch took {round(end_time - start_time, 2)} seconds \n"
          f"Iterated through {len(link_list)} links \n"
          f"Average time per offer is {round((end_time - start_time) / len(link_list), 2)} \n")


    print(f"Started sleeping")
    time.sleep(150)
    print(f"Finished sleeping")
