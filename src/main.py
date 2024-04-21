import time
# internal imports
from search_offers import search_offers


# generates link list using search_loader.py from a csv file


while True:
    search_offers()

    print(f"Started sleeping")
    time.sleep(150)
    print(f"Finished sleeping")
