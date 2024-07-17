# BEAUTIFUL SOUP IMPORTS
import requests
from bs4 import BeautifulSoup

# OTHER IMPORTS
import os
import pickle

# MY IMPORTS
import notify
from . import search_loader
from data.pickle_helper import clear_file
from .base import Offer

# VARIABLES FROM CONFIG
from config import ALREADY_NOTIFIED_PATH, SEARCH_INFO_LOCATION

# Internal imports
from time_utils import measure_time, time_helper

LINK_LIST = search_loader.search_loader(SEARCH_INFO_LOCATION)

@measure_time.measure_time
def search_bs(link_list_inner=LINK_LIST):
    offers = []

    for count, link in enumerate(link_list_inner):
        print(f"\n{time_helper.human_readable_time()}: ({count+1}/{len(link_list_inner)}) || {link}")
        offer_notify_count = 1

        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        pagination_elements = soup.find_all('li', attrs={'data-testid': 'pagination-list-item'})

        number_of_pages = 1 if (pagination_elements == []) else int(pagination_elements[-1].text)

        title_element = soup.find('span', attrs={'data-testid': 'total-count'}).text.strip("Znaleźliśmy ")
        title_element = title_element[:title_element.find(' ')]

        # title will contains '1000+' if we have more then 20 pages
        # so let's just check for that, to determine if we can cast to int
        number_of_offerts = int(title_element if ('+' not in title_element) else 1000)

        offerts_seen = 0

        for page in range(1, number_of_pages + 1):
            # putting `page` at the end of the url causes olx to return error page, this mimicks the urls found in page navigation buttons
            url = link[:link.find('/?') + 2] + f"page={page}&" + link[link.find('/?') + 2:]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            print(f"\tnow scraping: [{page} of {number_of_pages}]: {url}")

            # on any search page there will be one or more elements with `listing-grid` data-testid.
            # First one contains the data we want, the rest contain offerts that are outside of our area of interest

            # TODO: we could probably skip the rest of the pages if we find more then one such element, but this has to be looked into
            offerts_within_reach = soup.find('div', attrs={'data-testid': 'listing-grid'})
            offer_elements = offerts_within_reach.find_all('div', attrs={'data-cy': 'l-card'})

            if not offer_elements:
                break

            for offer_element in offer_elements:
                offerts_seen += 1

                print(f"\tgot another one: {offerts_seen} / {number_of_offerts}")

                if "Wyróżnione" in offer_element.text:
                    continue

                try:
                    offer_id = offer_element['id']
                    name = offer_element.find('h6', class_='css-1wxaaza').text
                    price_element = offer_element.find('p', attrs={'data-testid': 'ad-price'}).text
                    negotiation = "do negocjacji" if ("do negocjacji" in price_element) else "nie do negocjacji"
                    price = price_element.strip("do negocjacji") if (negotiation == "do negocjacji") else price_element
                    location_date_element = offer_element.find('p', attrs={'data-testid': 'location-date'})
                    location, date = location_date_element.text.split(' - ') if location_date_element else ("", "")
                    condition = offer_element.find('span', class_='css-3lkihg').text
                    offer_link = "https://olx.pl" + offer_element.find('a')['href']

                    offer = Offer(
                        offer_id,
                        name,
                        price,
                        negotiation,
                        condition,
                        location,
                        date,
                        offer_link
                    )

                    if (not os.path.isfile(ALREADY_NOTIFIED_PATH)):
                        clear_file()

                    with open(ALREADY_NOTIFIED_PATH, "rb") as f:
                        already_notified = pickle.load(f)

                    if offer in already_notified:
                        print(f"\t\talready seen, skipping")
                        continue

                    notify.notify(offer)

                    match offer_notify_count:
                        case 1:
                            suffix = "st"
                        case 2:
                            suffix = "nd"
                        case 3:
                            suffix = "rd"
                        case _:
                            suffix = "th"

                    print(
                        f"\tNotified user about offer {offer.id:9}. "
                        f"It was the {offer_notify_count}{suffix} offer"
                    )
                    offer_notify_count += 1

                    with open(ALREADY_NOTIFIED_PATH, "wb") as f:
                        already_notified.add(offer)
                        pickle.dump(already_notified, f, protocol=pickle.HIGHEST_PROTOCOL)

                except Exception as e:
                    print(f"\tError processing offer: {e}")

            page += 1

        if offer_notify_count == 1:
            print(f"\tNo new offers were seen")
