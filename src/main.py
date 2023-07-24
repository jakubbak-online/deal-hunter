from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = "https://www.olx.pl/oferty/q-canon/?search%5Border%5D=created_at:desc&reason=observed_search"
driver.get(link)


xpath = "//div[@data-testid='listing-grid']/div[@id='div-gpt-ad-listing-sponsored-ad']/following-sibling::div[@data-cy='l-card'][not(contains(descendant::div, 'Wyróżnione'))]"
offers = driver.find_elements(By.XPATH, xpath)

print(offers[0].get_attribute("id"))

#for offer in offers:
#    print(offer.text+"\n"+"\n")
#    print(dir(offer))
