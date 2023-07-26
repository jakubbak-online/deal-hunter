# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import time

# My imports
from searchloader import searchloader

# time measurement
start_time = time.time()

# Config
xpath = "//div[@data-testid='listing-grid']/div[@id='div-gpt-ad-listing-sponsored-ad']/" \
        "following-sibling::div[@data-cy='l-card'][not(contains(descendant::div, 'Wyróżnione'))]"
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
link_list = searchloader('data.csv')

# print(link_list)

# Setup
driver = webdriver.Chrome()

offers = []

for count, link in enumerate(link_list):
    driver.get(link)

    try:
        elements = WebDriverWait(driver, timeout=9, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, xpath))
        )

        offers.append(elements)

        for count2, offer in enumerate(offers[count]):
            print(offer.text)
            print("Oferta nr " + str(count2))

    finally:
        pass


driver.quit()

end_time = time.time()
print(end_time-start_time)


