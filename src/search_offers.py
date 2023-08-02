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

# MY IMPORTS
import notify

# VARIABLES TO BE USED LATER
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException)
xpath = '//div[not(preceding::div[contains(descendant::text(), "Znaleźliśmy  0 ogłoszeń")])]' \
        '/div[@data-testid="listing-grid"]/child::div[@data-cy="l-card"' \
        'and not(contains(descendant::div, "Wyróżnione"))' \
        'and not(preceding::*[contains(descendant::text(), "Sprawdź ogłoszenia w większej odległości:")])]'
already_notified_path = "./data/already_notified.pickle"

# ATOMIC OPEN, use in case pickle file is missing or sth
'''
with open(already_notified_path, "wb") as f:
    already_notified = {"851840892"}
    pickle.dump(already_notified, f, protocol=pickle.HIGHEST_PROTOCOL)
'''


def search_offers(link_list_inner):

    # CREATES WEBDRIVER INSTANCE, AND MINIMIZES IT
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.minimize_window()


    # EMPTY LIST OF OFFERS (offers is later used as a list of lists)
    # DON'T MOVE PLS
    offers = []

    # GOES FOR EVERY LINK IN LIST OF LINKS
    for count, link in enumerate(link_list_inner):
        # DRIVER GOES TO LINK
        driver.get(link)

        # PROGRESS COUNT PRINT
        print("("+str(count+1)+"/"+str(len(link_list_inner))+") "+link)

        try:
            # SEARCH ELEMENTS IN DOM WITH XPATH SPECIFIED EARLIER
            elements = WebDriverWait(driver, timeout=2, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath))
            )

            # ADDS LIST OF ELEMENTS TO OFFERS LIST
            offers.append(elements)

            # ITERATES THROUGH EVERY OFFER IN SEARCH
            for count2, offer in enumerate(offers[count]):
                split_offer = offer.text.split("\n")

                # LOADS ALREADY_NOTIFIED
                with open(already_notified_path, "rb") as f:
                    already_notified = pickle.load(f)

                # IF ID IS IN ALREADY_NOTIFIED THEN SKIP ONE ITERATION OF THE LOOP
                if offer.get_attribute("id") in already_notified:
                    continue

                # HANDLES IF OFFER IS OPEN TO NEGOTIATIONS
                if split_offer[2] != "do negocjacji":
                    split_offer.insert(2, "nie do negocjacji")

                # INSERTS ID INTO OFFER
                split_offer.insert(0, offer.get_attribute("id"))

                # SEPARATES LOCATION FROM TIME
                split_offer_buffer = split_offer[5].split(" - ")
                split_offer.append(split_offer_buffer[1])
                split_offer[5] = split_offer_buffer[0]

                # APPENDS LINK TO SPLIT_OFFER
                split_offer.append(offer.find_element(By.TAG_NAME, "a").get_attribute("href"))

                notify.notify(split_offer[0], split_offer[1], split_offer[2], split_offer[3], split_offer[4],
                              split_offer[5], split_offer[6], split_offer[7])

                print(f"Notified user about offer number {offer.get_attribute('id')}")

                # AFTER NOTIFYING ADDS ID TO ALREADY_NOTIFIED
                with open(already_notified_path, "wb") as f:
                    already_notified.add(offer.get_attribute("id"))
                    pickle.dump(already_notified, f, protocol=pickle.HIGHEST_PROTOCOL)


        except TimeoutException:
            print("("+str(count+1)+"/"+str(len(link_list_inner))+") "+"BRAK ELEMENTÓW W WYSZUKIWANIU")

            # APPENDS EMPTY LIST TO OFFERS, SO LOOP CAN PROCEED NORMALLY
            offers.append([])

    driver.quit()

