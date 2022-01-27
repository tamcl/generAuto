import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, logging

def check_element_exist(driver_, xpath):
    try:
        driver_.find_element_by_xpath(xpath)
        return True
    except Exception as e:
        logging.warning(f'element {xpath} cannot be found, error:\n{repr(e)}')
        return False


class point_gainer:
    def __init__(self, driver, order_list_time:list=list()):
        self.driver = driver
        self.order_list_time=order_list_time
        # self.login()

    def scrape_search_list(self,max_search:int =30, topics:list=list()):
        logging.info('Initiate search list scrape')
        if len(topics) ==0:
            topics.append('news')

        for search_topic in topics:
            self.driver.get(f'https://www.google.com/search?q={search_topic.replace(" ", "+")}')
            # try:
            #     self.driver.find_elements_by_xpath('//input[@title="Search"]')
            #     logging.info('Search bar found')
            # except:
            #     logging.warning(f'loading google search engine')

            if check_element_exist(self.driver, '//button[@id="L2AGLb"]'):
                self.driver.find_element_by_xpath('//button[@id="L2AGLb"]').click()
                logging.info('google consent agreed')

            # self.type('//input[@title="Search"]', search_topic, threshold=0.005)
            # self.driver.find_element_by_xpath('//input[@class="gNO89b"]').click()
            logging.info(f'search keyword: {search_topic}')
            sleep_time = 5
            for i in range(5):
                time.sleep(sleep_time)
                try:
                    self.google_next_page()
                    sleep_time = 5
                except:
                    sleep_time+=5

    def get_previoius_website_data(self, path:str):
        with open(path, 'r') as f:
            self.previous_raw = f.read()



    def google_next_page(self):
        if check_element_exist(self.driver, '//a[@id="pnnext"]'):
            self.driver.find_element_by_xpath('//a[@id="pnnext"]').click()
            logging.info('Google click next page')




    def watch_ads(self, deadline=list(), threshold=5):
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
