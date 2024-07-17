import time
# internal imports
from scraper import search_selenium, search_bs
from time_utils import time_helper

if __name__ == '__main__':
    while True:
        # Selenium based backend
        search_selenium.search_selenium()

        # Beautiful Soup based backend
        # search_bs.search_bs()

        print(f"{time_helper.human_readable_time()}: Started sleeping")
        time.sleep(150)
        print(f"{time_helper.human_readable_time()}: Finished sleeping")
