from selenium import webdriver
from selenium.webdriver.common.by import By

from searchloader import searchloader

driver = webdriver.Chrome()

xpath = "//div[@data-testid='listing-grid']/div[@id='div-gpt-ad-listing-sponsored-ad']/following-sibling::div[@data-cy='l-card'][not(contains(descendant::div, 'Wyróżnione'))]"
linklist = searchloader()

print(linklist)

for link in linklist:
    print(str(link))
    #link = "https://www.olx.pl/elektronika/fotografia/q-canon/"
    driver.get(str(link))

    offers = driver.find_elements(By.XPATH, xpath)

    print(offers[0].text)
