# from rightmove_web_scraper import RightMoveScraper
from property_info_extractor import PropertyInfo

postcodes = {
    'BN1': '5E220',
    'BN13': '5E224',
    'BN17': '5E228',
    'BN21': '5E232',
    'BN25': '5E236',
    'BN41': '5E240',
    'BN45': '5E244',
    'BN8': '5E248',
    'BN10': '5E221',
    'BN14': '5E225',
    'BN18': '5E229',
    'BN22': '5E233',
    'BN26': '5E237',
    'BN42': '5E241',
    'BN5': '5E245',
    'BN9': '5E249',
    'BN11': '5E222',
    'BN15': '5E226',
    'BN2': '5E230',
    'BN23': '5E234',
    'BN27': '5E238',
    'BN43': '5E242',
    'BN6': '5E246',
    'BN12': '5E223',
    'BN16': '5E227',
    'BN20': '5E231',
    'BN24': '5E235',
    'BN3': '5E239',
    'BN44': '5E243',
    'BN7': '5E247'
}

# scrapper = RightMoveScraper(postcodes)
# scrapper.get_data()
# scrapper.save_to_csv()

file = 'Data/right_move_data.csv'
extractor = PropertyInfo(file)

extractor.get_property_data(2392)
# extractor.save_to_csv()
