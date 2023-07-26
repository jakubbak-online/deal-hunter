import time

# my imports
from search_loader import search_loader
from search_offers import search_offers

# time measurement
start_time = time.time()

# config and setup
link_list = search_loader('data.csv')
search_offers(link_list)

end_time = time.time()
print(end_time - start_time)
