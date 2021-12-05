import os
import zipfile
import wget
import requests



class setup:
    def __init__(self, path):
        self.path = path
        print('Initiate setup')
        self.create_data_repo()
        self.chromedriver_setup()

    def create_data_repo(self):
        print('Check data directory')
        try:
            os.mkdir(os.path.join(self.path, 'data'))
            print('Data directory created')
        except:
            print('Data directory exist')

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
