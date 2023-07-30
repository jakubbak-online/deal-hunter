import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import prettytable
# import csv

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException)
xpath = '//div[not(preceding::div[contains(descendant::text(), "Znaleźliśmy  0 ogłoszeń")])]' \
        '/div[@data-testid="listing-grid"]/child::div[@data-cy="l-card"' \
        'and not(contains(descendant::div, "Wyróżnione"))' \
        'and not(preceding::*[contains(descendant::text(), "Sprawdź ogłoszenia w większej odległości:")])]'


def search_offers(link_list_inner, file_name="./data/search_offers_data.csv"):

    # creates driver instance
    driver = webdriver.Chrome()

    table = prettytable.PrettyTable(header=False)

    # initializes empty list
    # DON'T MOVE PLS
    offers = []

    # goes through every link in list of links
    for count, link in enumerate(link_list_inner):
        # driver goes to link
        driver.get(link)

        # prints progress count
        print("("+str(count+1)+"/"+str(len(link_list_inner))+") "+link)

        try:
            # gets the elements of a page by xpath specified earlier
            elements = WebDriverWait(driver, timeout=2, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath))
            )
            # print(elements)
            offers.append(elements)

            # iterates through offers, preparing them for further actions
            for offer in offers[count]:
                split_offer = offer.text.split("\n")

                # handles offer's availability to negotiate
                if split_offer[2] != "do negocjacji":
                    split_offer.insert(2, "nie do negocjacji")

                # inserts id into offer
                split_offer.insert(0, offer.get_attribute("id"))

                # separates location from time
                split_offer_buffer = split_offer[5].split(" - ")
                split_offer.append(split_offer_buffer[1])
                split_offer[5] = split_offer_buffer[0]

                # adds split offer to table
                table.add_row(split_offer)

        except TimeoutException:
            print("("+str(count+1)+"/"+str(len(link_list_inner))+") "+"BRAK ELEMENTÓW W WYSZUKIWANIU")

            # adds empty list to offers object, in case if elements are empty
            offers.append([])

    # print(table)
    # print(table.get_csv_string())
    driver.quit()

    with open(file_name, 'wt+', encoding="utf-8", newline='') as f:
        f.write(table.get_csv_string())

    return table.get_csv_string()
