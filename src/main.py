import time
# internal imports
from search_offers import search_offers


if __name__ == '__main__':
    while True:
        search_offers()

        print(f"Started sleeping")
        time.sleep(150)
        print(f"Finished sleeping")
