# BEAUTIFUL SOUP IMPORTS
import requests
from bs4 import BeautifulSoup

# OTHER IMPORTS
import threading
from typing import List

from . import search_loader
from .base import Offer

# VARIABLES FROM CONFIG
from config import SEARCH_INFO_LOCATION

# Internal imports
from time_utils import time_helper, measure_time

LINK_LIST = search_loader.search_loader(SEARCH_INFO_LOCATION)

def search_bs(link_list_inner=LINK_LIST) -> List[Offer]:
    """Beautiful Soup 4 based scraping backend"""
    offers = []
    urls = generate_urls(link_list_inner)

    threads = []

    def worker(url: str):
        page_offers = search_link(url)
        print(
            f"\n{time_helper.human_readable_time()} | scraped: {url}" +
            f"\n\tgot {len(page_offers)} results."
        )
        offers.extend(page_offers)

    for link in urls:
        # print(f"\n{time_helper.human_readable_time()} | ({count+1}/{len(urls)}) || {link}")

        thread = threading.Thread(target=worker, args=(link,))
        thread.start()

        threads.append(thread)

    for thread in threads:
        thread.join()

    return offers

def generate_urls(link_list_inner=LINK_LIST) -> List[str]:
    """Helper for generating urls used for scraping search queries"""
    urls = []

    for link in link_list_inner:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        pagination_elements = soup.find_all('li', attrs={'data-testid': 'pagination-list-item'})

        number_of_pages = 1 if (pagination_elements == []) else int(pagination_elements[-1].text)

        for page in range(number_of_pages):
            # putting `page` at the end of the url causes olx to return error page, this mimicks the urls found in page navigation buttons
            urls.append(link[:link.find('/?') + 2] + f"page={page + 1}&" + link[link.find('/?') + 2:])

    return urls

def search_link(url: str) -> List[Offer]:
    offers = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # on any search page there will be one or more elements with `listing-grid` data-testid.
    # First one contains the data we want, the rest contain offerts that are outside of our area of interest

    # TODO: we could probably skip the rest of the pages if we find more then one such element, but this has to be looked into
    offerts_within_reach = soup.find('div', attrs={'data-testid': 'listing-grid'})
    offer_elements = offerts_within_reach.find_all('div', attrs={'data-cy': 'l-card'})

    if not offer_elements:
        return []

    for offer_element in offer_elements:
        if "Wyróżnione" in offer_element.text:
            continue

        try:
            price_element = offer_element.find('p', attrs={'data-testid': 'ad-price'}).text
            negotiation = "do negocjacji" if ("do negocjacji" in price_element) else "nie do negocjacji"
            price = price_element.strip("do negocjacji") if (negotiation == "do negocjacji") else price_element
            location_date_element = offer_element.find('p', attrs={'data-testid': 'location-date'})
            location, date = location_date_element.text.split(' - ') if location_date_element else ("", "")

            offer = Offer(
                id = offer_element['id'],
                name = offer_element.find('h6', class_='css-1wxaaza').text,
                price = price,
                negotiation = negotiation,
                condition = offer_element.find('span', class_='css-3lkihg').text,
                location = location,
                date = date,
                link = "https://olx.pl" + offer_element.find('a')['href']
            )

            offers.append(offer)

        except Exception as e:
            print(f"\tError processing offer: {e}")

    return offers
