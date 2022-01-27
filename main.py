import os, sys

folder_path = os.path.dirname(os.path.abspath(__file__))
library_path = 'lib'
sys.path.append(os.path.join(folder_path, library_path))
from selenium_setup import *
from auto_order import *
from point_gainer import *
from setup import *
import json, logging

logging.basicConfig(format=f'%(levelname)s: %(asctime)s - %(message)s',
                    level='INFO',
                    datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    # find current location
    # create data directory
    setup(folder_path)
    path_to_chromedriver = os.path.join(folder_path, 'chromedriver',
                                        os.listdir(os.path.join(folder_path, 'chromedriver'))[0])
    logging.info(f'Use chromedriver: {path_to_chromedriver}')
    extension_folder = os.path.join(folder_path, 'chromeExtension')
    extensions = os.listdir(extension_folder)
    extension_paths = [os.path.join(extension_folder, p) for p in extensions]

    logging.info('read credential')
    try:
        with open(os.path.join(folder_path, 'credential.json'), 'r') as f:
            credential = json.loads(f.read())

    except FileNotFoundError as e:
        logging.warning(f'File not found please create credential.json')
    except Exception as e:
        logging.warning(f'credential error:\n {repr(e)}')
        raise

    driver = create_driver(os.path.join(folder_path, 'chromedriver',
                                        os.listdir(os.path.join(folder_path, 'chromedriver'))[0]), extension_paths)

    login(driver, credential['email'], credential['password'])

    #TODO check order_list time
    #TODO if there isn't any / empty order_list create one
    #TODO if there is, check time for order then update
    #TODO with spare time we proceed to point gainer

    pg = point_gainer(driver)
    # pg.scrape_search_list()
    deadline_info = get_deadline(driver)
    # update_deadline(os.path.join(folder_path,'order_option','order_list.json'), deadline_info)

    # driver.quit()
    # logging.info('Quit Driver')

    # install Chrome webdriver
    # find correct gener8 extension
    # check credential
    #
