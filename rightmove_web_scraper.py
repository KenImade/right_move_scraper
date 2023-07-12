import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random


class RightMoveScraper:
    link_list = []
    description_list = []
    address_list = []
    price_list = []

    def __init__(self, postcodes):
        self.postcodes = postcodes

    def get_data(self):
        for postcode, value in self.postcodes.items():
            index = 0
            print(f"Currently collecting data for postcode: {postcode}")
            for pages in range(41):
                rightmove_link = f'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier' \
                                 f'=OUTCODE%{value}&index={index}&propertyTypes=&includeSSTC=false&mustHave=&dontShow' \
                                 f'=&furnishTypes=&keywords='

                #     request webpage
                res = requests.get(rightmove_link).text

                soup = BeautifulSoup(res, 'html.parser')

                # gets the list of apartments
                listings = soup.find_all("div", class_="l-searchResult")

                #     gets the number of listings
                number_of_listings = soup.find("span", {"class": "searchHeader-resultCount"})
                number_of_listings = int(number_of_listings.get_text().replace(",", ""))
                print(f"The number of listings in this {postcode} is: {number_of_listings}")
                for listing in listings:
                    url = 'https://www.rightmove.co.uk' + listing.find('a', class_='propertyCard-link')['href']
                    address = (
                        listing.find("address", class_="propertyCard-address")
                        .get_text()
                        .strip()
                    )
                    self.link_list.append(url)
                    self.address_list.append(address)
                    description = (
                        listing.find("h2", class_="propertyCard-title")
                        .get_text()
                        .strip()
                    )
                    self.description_list.append(description)
                    price = (
                        listing.find("div", class_="propertyCard-priceValue")
                        .get_text()
                        .strip()
                    )
                    self.price_list.append(price)

                print(f"You have scrapped {pages + 1} pages of apartment listings.")
                print(f"You have {number_of_listings - index} listings left to go")
                print("\n")

                time.sleep(random.randint(1, 3))

                index = index + 24

                if index >= number_of_listings:
                    break

            print(f"Done collecting data for {postcode} 😊")

    def save_to_csv(self):
        data = {
            "Property Links": self.link_list,
            "Address": self.address_list,
            "Description": self.description_list,
            "Price": self.price_list
        }
        df = pd.DataFrame.from_dict(data)
        df.to_csv(r'right_move_data.csv', encoding='utf-8', header=True, index=False)
