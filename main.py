import os, sys
folder_path = os.path.dirname(os.path.abspath(__file__))
library_path = 'lib'
sys.path.append(os.path.join(folder_path,library_path))
from auto_order import *
from point_gainer import *
from setup import *
import json

if __name__ == "__main__":
    # find current location
    # create data directory
    setup(folder_path)
    print(os.path.join(folder_path,'chromedriver',os.listdir(os.path.join(folder_path,'chromedriver'))[0]))
    extension_folder = os.path.join(folder_path, 'chromeExtension')
    extensions = os.listdir(extension_folder)
    extension_paths = [os.path.join(extension_folder, p) for p in extensions]
    with open(os.path.join(folder_path, 'credential.json'), 'r') as f:
        credential = json.loads(f.read())
    point_gainer(credential['email'], credential['password'],
                 os.path.join(folder_path,'chromedriver',os.listdir(os.path.join(folder_path,'chromedriver'))[0]),
                 extension_paths,
                 os.path.join(folder_path,'data'))
    # install Chrome webdriver
    # find correct gener8 extension
    # check credential
    #