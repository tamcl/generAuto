import os
import zipfile
import wget
import requests
import json
import logging



class setup:
    def __init__(self, path):
        self.path = path
        # print('Initiate setup')
        logging.info(f'Initiate setup')
        self.create_data_repo()
        self.chromedriver_setup()
        # self.choice_file()

    def create_data_repo(self):
        # print('Check data directory')
        logging.info(f'Check data directory')
        try:
            os.mkdir(os.path.join(self.path, 'data'))
            # print('Data directory created')
            logging.info('data directory created')
        except:
            # print('Data directory exist')
            logging.info(f'Data directory exist')

        if 'search_topic.txt' not in os.listdir(os.path.join(self.path, 'data')):
            with open(os.path.join(self.path, 'data', 'search_topic.txt'), 'wb') as f:
                f.write(''.encode())
            logging.info('search_topic created')
        else:
            logging.info('search_topic exist')

        if 'order_list.json' not in os.listdir(os.path.join(self.path, 'data')):
            with open(os.path.join(self.path, 'data', 'order_list.json'), 'wb') as f:
                f.write(json.dumps(dict()).encode())
            logging.info('order list created')
        else:
            logging.info('order list exist')

    def chromedriver_setup(self):
        dir_exist = self.chromedriver_directory()
        if not dir_exist:
            self.download_chromedriver()


    def chromedriver_directory(self):
        dir_exist = False
        try:
            os.mkdir(os.path.join(self.path, 'chromedriver'))
        except:
            dir_exist = True
        return dir_exist

    def download_chromedriver(self):
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_95.0.4638'
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text

        download_url = 'https://chromedriver.storage.googleapis.com/' + version_number + '/chromedriver_win32.zip'

        # download the zip file using the url built above
        latest_driver_zip = wget.download(download_url, 'chromedriver.zip')

        # extract the zip file
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(path=os.path.join(self.path,'chromedriver'))  # you can specify the destination folder path here
        # delete the zip file downloaded above
        os.remove(latest_driver_zip)

    def choice_file(self):
        logging.info(f'initiate choice file function')
        try:
            os.mkdir(os.path.join(self.path, 'order_option'))
            logging.info(f'order option created')
        except:
            logging.info(f'order option exist')



