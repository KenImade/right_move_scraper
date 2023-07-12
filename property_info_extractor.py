import pandas as pd
from selenium.common.exceptions import NoSuchElementException as BadLink
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import mysql.connector


class PropertyInfo:
    property_link_list = []
    address_list = []
    property_info_list = []
    closest_rail_station_list = []
    error_links = []
    last_link = 0

    def __init__(self, file):
        data = pd.read_csv(file)
        self.links = data['Property Links']
        self.conn = mysql.connector.connect(
            host="localhost",          # Your host name
            user="root",      # Your username
            password="admin",  # Your password
            database="property_info_db"   # Your database name
        )
        self.cur = self.conn.cursor()

    def get_property_data(self, index=0):
        """
        gets the property data from the url list
        :param index: position in list to begin extraction
        :return: None
        """
        options = Options()
        options.add_experimental_option('detach', True)
        options.add_argument('--headless')

        path = 'C:/SeleniumDrivers/chromedriver.exe'

        number_of_links = len(self.links)

        print(f"There are {number_of_links} possible links")
        print("Beginning info extraction...")
        for i in range(index, number_of_links):
            link = self.links[i]
            # print(len(link))
            # eliminates links that do not have the property id
            driver = webdriver.Chrome(service=Service(path), options=options)
            if len(link) > 27:
                print(f"Link {i}: {link}")
                driver.get(link)
                item = {
                    "address": "",
                    "property_details": "",
                    "closest_stations": "",
                    "property_link": ""
                }
                # check if property is available
                try:
                    # address info
                    item['address'] = driver.find_element(By.XPATH, '//h1[@itemprop="streetAddress"]').get_attribute(
                        'innerHTML')

                    # property reel
                    property_reel = driver.find_element(By.XPATH, '//div[@data-test="infoReel"]')
                    property_reel_children = property_reel.find_elements(By.TAG_NAME, 'dd')
                    property_details = []
                    for info in property_reel_children:
                        property_details.append(info.get_attribute('innerHTML'))

                    item['property_details'] = ','.join(property_details)

                    # nearness to station
                    closest_stations = []
                    rail_stations = (
                        driver.find_element(By.XPATH, '//div[@id="Stations-panel"]').find_element(By.TAG_NAME, 'ul')
                        .find_elements(By.TAG_NAME, 'li'))

                    for station in rail_stations:
                        list_station = station.find_elements(By.TAG_NAME, 'span')
                        for value in list_station:
                            closest_stations.append(value.get_attribute('innerHTML'))

                    item['closest_stations'] = ','.join(closest_stations)

                    # self.closest_rail_station_list.append(','.join(closest_stations))
                    item['property_link'] = link
                    self.process_item(item)
                    driver.quit()
                    print(f"Done with link {i}")
                except BadLink:
                    print(f"Bad link 😞")
                    self.error_links.append(link)
                finally:
                    self.last_link = i


    def process_item(self, item):
        self.cur.execute("""INSERT INTO property_info (address, property_details, closest_stations, 
                            property_link) VALUES (%s, %s, %s, %s)""", (
            item['address'],
            item['property_details'],
            item['closest_stations'],
            item['property_link']
        ))

        self.conn.commit()

    def get_error_links(self):
        return self.error_links

    def save_to_csv(self):
        data = {
            "Property Links": self.property_link_list,
            "Address": self.address_list,
            "Property Info": self.property_info_list,
            "Closest Rail Stations": self.closest_rail_station_list
        }
        df = pd.DataFrame.from_dict(data)
        df.to_csv(r'./Data/right_move_data_property_info.csv', encoding='utf-8', header=True, index=False)
