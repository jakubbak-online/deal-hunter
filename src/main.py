import time

# internal imports
from time_utils import time_helper
from scraper.base import Backend, search_offers

if __name__ == '__main__':
    while True:
        # Selenium based backend
        # search_offers()

        # Beautiful Soup based backend
        search_offers(Backend.BEAUTIFUL_SOUP)

        print(f"{time_helper.human_readable_time()}: Started sleeping")
        time.sleep(150)
        print(f"{time_helper.human_readable_time()}: Finished sleeping")
