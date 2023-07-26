from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
xpath = "//div[@data-testid='listing-grid']/div[@id='div-gpt-ad-listing-sponsored-ad']/" \
        "following-sibling::div[@data-cy='l-card'][not(contains(descendant::div, 'Wyróżnione'))]"


def search_offers(link_list_inner):
    offers = []

    driver = webdriver.Chrome()

    for count, link in enumerate(link_list_inner):
        driver.get(link)

        try:
            elements = WebDriverWait(driver, timeout=9, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath))
            )

            offers.append(elements)

            for count2, offer in enumerate(offers[count]):
                chunks = offer.text.split("\n")

                if chunks[2] != "do negocjacji":
                    chunks.insert(2, "")

                for chunk in chunks:
                    print(chunk)
                '''
                if chunks[3] != "do negocjacji":
                    chunks.append(chunks[3])
                    chunks[3] = None

                print(f"{chunks[0]:30}", end=None)
                print(f"{chunks[1]}", end=None)
                print(f"{chunks[2]}", end=None)
                print(f"{chunks[3]}", end=None)
                print(f"{chunks[4]}", end=None)
                '''

                print("-------------------------------------------------------------------------------------")

                '''
                for count3, chunk in enumerate(chunks):
                    print(str(count3) + " " + str(chunk))
                '''
                # print("Oferta nr " + str(count2))

        finally:
            pass

    driver.quit()
