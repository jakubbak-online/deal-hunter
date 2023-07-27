import time

# my imports
from search_loader import search_loader
from search_offers import search_offers

# time measurement
start_time = time.time()

# generates link list using search_loader.py from a csv file
link_list = search_loader('datashort.csv')

# searches offers using link list generated before
search_offers(link_list)

# time measurement
end_time = time.time()
print(end_time - start_time)
