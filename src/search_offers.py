from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import prettytable

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
xpath = '//div[@data-testid="listing-grid"]/child::div[@data-cy="l-card" and ' \
        'not(contains(descendant::div, "Wyróżnione")) and not(preceding::*' \
        '[contains(descendant::text(), "Sprawdź ogłoszenia w większej odległości:")])]'


def search_offers(link_list_inner):
    offers = []

    driver = webdriver.Chrome()

    table = prettytable.PrettyTable(header=False)
    for count, link in enumerate(link_list_inner):
        driver.get(link)

        print(link)
        try:
            elements = WebDriverWait(driver, timeout=9, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath))
            )
            offers.append(elements)

            # table = prettytable.PrettyTable(header=False)
            for offer in offers[count]:
                split_offer = offer.text.split("\n")

                if split_offer[2] != "do negocjacji":
                    split_offer.insert(2, "nie do negocjacji")

                split_offer.insert(0, offer.get_attribute("id"))

                split_offer_buffer = split_offer[5].split(" - ")
                split_offer.append(split_offer_buffer[1])
                split_offer[5] = split_offer_buffer[0]

                table.add_row(split_offer)

                '''
                for chunk in chunks:
                    table.add_column(chunk)
                    table.add_row()
                    # print("{:20}".format(chunk), end=None)
                '''

            # print(table.get_csv_string())
            # print("Oferta nr " + str(count2))

        finally:
            pass

    print(table)
    driver.quit()
