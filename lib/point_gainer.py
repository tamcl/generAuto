import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class point_gainer:
    def __init__(self, username: str, password: str, webdriver_path: str, extension_paths: list, db_path: str):
        self.username = username
        self.password = password
        self.extension_paths = extension_paths
        self.webdriver_path = webdriver_path
        self.db_path = db_path
        self.driver = None
        self.selenium_setup()
        self.login()
        self.watch_ads()
        self.driver.quit()

    def selenium_setup(self):
        chrome_options = Options()
        for path in self.extension_paths:
            chrome_options.add_extension(path)
        self.driver = webdriver.Chrome(options=chrome_options, executable_path=self.webdriver_path)

    def login(self):
        print('Start to login')
        self.driver.get('https://gener8ads.com/account/login')
        time.sleep(5)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[3]/div[1]/form/label[1]/input').send_keys(self.username)
        self.type('/html/body/div[2]/div[2]/section/div[3]/div[1]/form/label[1]/input', self.username)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[3]/div[1]/form/label[2]/input').send_keys(self.password)
        self.type('/html/body/div[2]/div[2]/section/div[3]/div[1]/form/label[2]/input', self.password)
        time.sleep(0.3)
        self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/section/div[3]/div[1]/form/div/div[2]/button').click()

        login_break = True
        while login_break:
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[3]/div[1]/header/h2')
                login_break = False
            except Exception as e:
                # print(e)
                pass
        buttons = self.driver.find_element_by_class_name('mode-switch')
        print(len(buttons.find_elements_by_tag_name('button')))
        mode = 'Rewards'
        button_selection = 0
        for index in range(len(buttons.find_elements_by_tag_name('button'))):
            if buttons.find_elements_by_tag_name('button')[index].text == mode:
                button_selection = index
                break
        buttons.find_elements_by_tag_name('button')[button_selection].click()

        # self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/section/div[3]/div[3]/div[3]/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/div[3]/div[3]/div[3]/button[2]').click()

        print("Login successful")

    def watch_ads(self, deadline=list(), threshold=30 ):
        for i in range(threshold):
            self.driver.get('https://www.standard.co.uk/')
            time.sleep(3)

            SCROLL_PAUSE_TIME = 1

            # Get scroll height
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                # Scroll down to bottom
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            ads = self.driver.find_elements_by_tag_name("iframe")
            ads_replace = 0
            for ad in ads:
                if 'gener8' in ad.get_attribute("name"):
                    ads_replace += 1
            print('Ads replacement count: {}'.format(ads_replace))
            # news reader

    def type(self, xpath, word: str, threshold=0.01):
        for letter in word:
            self.driver.find_element_by_xpath(xpath).send_keys(letter)
            time.sleep(threshold)
