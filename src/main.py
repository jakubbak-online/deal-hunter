import time
# internal imports
from search_offers import search_offers
from time_utils import time_helper

if __name__ == '__main__':
    while True:
        search_offers()

        print(f"{time_helper.human_readable_time()}: Started sleeping")
        time.sleep(150)
        print(f"{time_helper.human_readable_time()}: Finished sleeping")
