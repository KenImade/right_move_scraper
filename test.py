# import requests
# from bs4 import BeautifulSoup
# import re
# import pandas as pd
# import time
# import random
#
# link_list = []
# description_list = []
# address_list = []
# price_list = []
#
# postcodes = {
#         'BN1': '5E220'
#     }
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/89.0.4389.114 Safari/537.36"
# }
#
# link = f'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=OUTCODE%5E247&index=24' \
#        f'&propertyTypes=&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='
#
# res = requests.get(link).text
# soup = BeautifulSoup(res, 'html.parser')
# number_of_listings = soup.find("span", {"class": "searchHeader-resultCount"})
# number_of_listings = int(number_of_listings.get_text().replace(",", ""))
# print(f"The number of listings in this postcode is: {number_of_listings}")
# listings = soup.find_all('div', class_="l-searchResult")
import selenium.common.exceptions
# for listing in listings:
#     url = 'https://www.rightmove.co.uk' + listing.find('a', class_='propertyCard-link')['href']
#     address = (
#         listing.find("address", class_="propertyCard-address")
#         .get_text()
#         .strip()
#     )
#     description = (
#         listing.find("h2", class_="propertyCard-title")
#         .get_text()
#         .strip()
#     )
#     price = (
#         listing.find("div", class_="propertyCard-priceValue")
#         .get_text()
#         .strip()
#     )
#     information = (
#         listing.find("div", class_="property-information")
#     )
#     price_list.append(price)
#     description_list.append(description)
#     address_list.append(address)
#     link_list.append(url)
#
# print(link_list)
# print(price_list)
# print(description_list)
# print(address_list)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# leaves browser open after action is finished
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--headless')

path = 'C:/SeleniumDrivers/chromedriver.exe'
link = 'https://www.rightmove.co.uk/properties/136878848#/?channel=RES_NEW'
broken_link = 'https://www.rightmove.co.uk/properties/132352442#/?channel=RES_BUY'
driver = webdriver.Chrome(service=Service(path), options=options)

driver.maximize_window()

driver.get(link)

# try:
#     driver.find_element(By.XPATH, '//div[@class="propertyUnpublished"]')
#     link_status = True
# except selenium.common.exceptions.NoSuchElementException:
#     link_status = False
#
# print(link_status)


# # address info
# address = driver.find_element(By.XPATH, '//h1[@itemprop="streetAddress"]').get_attribute('innerHTML')
# print(address)
#
# # property reel
propertyReel = driver.find_element(By.XPATH, '//div[@data-test="infoReel"]')
propertyReel_children = propertyReel.find_elements(By.TAG_NAME, 'dl')
property_info = []

for items in propertyReel_children:
    property_info.append(items.get_property('innerHTML'))

print(property_info)

# # propertyReel_dict = {key: value.get_attribute('innerHTML') for key, value in zip(my_dict.keys(),
# #                                                                                  propertyReel_children)}
# # print(propertyReel_children[0].get_attribute('innerHTML'))
# # print(propertyReel_children[1].get_attribute('innerHTML'))
# # print(propertyReel_children[2].get_attribute('innerHTML'))
# # print(propertyReel_children[3].get_attribute('innerHTML'))
#
# # nearness to station
# closest_stations = []
# rail_stations = (driver.find_element(By.XPATH, '//div[@id="Stations-panel"]').find_element(By.TAG_NAME, 'ul')
#                  .find_elements(By.TAG_NAME, 'li'))
#
# for station in rail_stations:
#     list_station = station.find_elements(By.TAG_NAME, 'span')
#     for index, item in enumerate(list_station):
#         if index % 2 != 0:
#             closest_stations.append(item.get_attribute('innerHTML'))
#
# print(closest_stations)
# # closest primary schools
# # closest_primary_schools = []
# # primary_schools_btn = driver.find_element(By.XPATH, '//button[@id="Schools-button"]')
# # primary_schools_btn.click()
# #
# # primary_schools = (driver.find_element(By.XPATH, '//div[@id="Schools-panel"').find_element(By.TAG_NAME, 'ul')
# #                    .find_elements(By.TAG_NAME, 'li'))
# #
# # for school in primary_schools:
# #     list_school = school.find_elements(By.TAG_NAME, 'span')
# #     for index, item in enumerate(list_school):
# #         if index % 2 != 0:
# #             closest_primary_schools.append(item.get_attribute('innerHTML'))
# #
# # print(closest_primary_schools)
#
# # close driver
# driver.quit()