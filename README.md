# RightMove WebScraper
This is a web scraper which can be used to scrape property data from [RightMove](https://www.rightmove.co.uk) and saves
it to a local MySQL database. It makes use of both the beautifulsoup and selenium packages.

How to use: Rightmove stores the postcode of various locations using special identifiers therefore you need to manually
find these identifiers e.g. "BN1" = "5E220".

Note ⚠️: Due to the dynamic nature and continuous changes made to the website the code might not work at the time you 
access this repository, however a few changes to the html elements being accessed should get the code working.

## File Description
main.py - Used to call the various classes.

rightmove_web_scraper.py - Gets the link and price of various property listings and saves into the file 
'right_move_data.csv'

property_info_extract.py - Uses the 'right_move_data.csv' file to extract further information for each property listing

test.py - Used in testing the elements being selected from the rightmove website.
