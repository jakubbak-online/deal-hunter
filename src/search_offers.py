# SELENIUM IMPORTS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# OTHER IMPORTS
import pickle
import time
import chromedriver_autoinstaller_fix

# MY IMPORTS
import notify
import search_loader

# VARIABLES FROM CONFIG
from config import search_info_location
# Internal imports
from mierz_czas import mierz_czas

# CONSTANTS TO BE USED LATER
IGNORED_EXCEPTIONS = (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

XPATH = (
    '//div[not(preceding::div[contains(descendant::text(), "Znaleźliśmy  0 ogłoszeń")])]'
    '/div[@data-testid="listing-grid"][1]'
    '/child::div[@data-cy="l-card"and not(contains(descendant::div, "Wyróżnione"))]'
)

ALREADY_NOTIFIED_PATH = "./data/already_notified.pickle"

LINK_LIST = search_loader.search_loader(search_info_location)

chromedriver_autoinstaller_fix.install()


@mierz_czas.mierz_czas
def search_offers(link_list_inner=LINK_LIST):
    # CREATES WEBDRIVER INSTANCE, WITH OPTIONS ADDED
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    # chrome_options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=chrome_options)
    # EMPTY LIST OF OFFERS (offers is later used as a list of lists)
    # DON'T MOVE PLS
    offers = list()

    # GOES FOR EVERY LINK IN LIST OF LINKS
    for count, link in enumerate(link_list_inner):
        # DRIVER GOES TO LINK
        driver.get(link)

        # PROGRESS COUNT PRINT
        offer_progress = f"({count+1}/{len(link_list_inner)})"
        offer_notify_count = 1
        print(f"\n{offer_progress} {time.ctime()[11:19]} || {link}")

        try:
            # SEARCH ELEMENTS IN DOM WITH XPATH SPECIFIED EARLIER
            elements = WebDriverWait(
                driver, timeout=2, ignored_exceptions=IGNORED_EXCEPTIONS
            ).until(
                expected_conditions.visibility_of_all_elements_located(
                    (By.XPATH, XPATH)
                )
            )

            # ADDS LIST OF ELEMENTS TO OFFERS LIST
            offers.append(elements)

            # ITERATES THROUGH EVERY OFFER IN SEARCH
            for count2, offer in enumerate(offers[count]):
                split_offer = offer.text.split("\n")

                # LOADS ALREADY_NOTIFIED
                with open(ALREADY_NOTIFIED_PATH, "rb") as f:
                    already_notified = pickle.load(f)

                # IF ID IS IN ALREADY_NOTIFIED THEN SKIP ONE ITERATION OF THE LOOP
                if offer.get_attribute("id") in already_notified:
                    continue

                # HANDLES IF OFFER IS OPEN TO NEGOTIATIONS
                if split_offer[2] != "do negocjacji":
                    split_offer.insert(2, "nie do negocjacji")

                # INSERTS ID INTO OFFER
                split_offer.insert(0, offer.get_attribute("id"))

                ''' OLX modified their display UI, doesnt work (for now)
                # SEPARATES LOCATION FROM TIME
                try:
                    split_offer_buffer = split_offer[5].split(" - ")
                except IndexError:
                    pass
                split_offer.append(split_offer_buffer[1])
                split_offer[5] = split_offer_buffer[0]
                '''

                # APPENDS LINK TO SPLIT_OFFER
                split_offer.append(
                    offer.find_element(By.TAG_NAME, "a").get_attribute("href")
                )

                for _ in range(0, 10):
                    try:
                        if split_offer[_] is not None:
                            pass
                    except IndexError:
                        split_offer.append("error")

                notify.notify(
                    offer_id=split_offer[0],
                    offer_name=split_offer[1],
                    offer_price=split_offer[2],
                    offer_negotiation=split_offer[3],
                    offer_condition=split_offer[4],
                    offer_location=split_offer[5],
                    offer_date=split_offer[6],
                    offer_link=split_offer[7],
                )

                print(
                    f"{offer_progress} Notified user about offer number {offer.get_attribute('id'):9}. "
                    f"It was {offer_notify_count}'th offer"
                )
                offer_notify_count += 1

                # AFTER NOTIFYING ADDS ID TO ALREADY_NOTIFIED
                with open(ALREADY_NOTIFIED_PATH, "wb") as f:
                    already_notified.add(offer.get_attribute("id"))
                    pickle.dump(already_notified, f, protocol=pickle.HIGHEST_PROTOCOL)

        except TimeoutException:
            offer_notify_count = 0
            print(f"{offer_progress} No offers in search")
            # APPENDS EMPTY LIST TO OFFERS, SO LOOP CAN PROCEED NORMALLY
            offers.append([])

        if offer_notify_count == 1:
            print(f"{offer_progress} No new offers were seen")

    driver.quit()
