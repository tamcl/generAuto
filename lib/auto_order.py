import datetime
import time
import json
import logging


def get_deadline(driver):
    def return_element_text(element, xpath, dataType=str):
        try:
            return dataType(element.find_element_by_xpath(xpath).text)
        except Exception as e:
            logging.warning(e)
            return 0

    driver.get('https://gener8ads.com/marketplace')
    time.sleep(5)
    # get all the purchase options
    # while True:
    #     try:
    #         driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/header/h1')
    #         break
    #     except Exception as e:
    #         print(e)

    gift_card_containers = driver.find_elements_by_xpath('//article[@class="c-product-item"]')
    gift_info = []
    # print('gift card container {}'.format(len(gift_card_containers)))

    for container in gift_card_containers:
        # print(container.find_element_by_xpath('.//h3[@class="c-product-item__title"]').text)

        info = dict(title=return_element_text(container, './/h3[@class="c-product-item__title"]'),
                    day=return_element_text(container,
                                            './/div[@class="segment segment--days"]//div[@class="chunk chunk--active"]',
                                            int),
                    hour=return_element_text(container,
                                             './/div[@class="segment segment--hrs"]//div[@class="chunk chunk--active"]',
                                             int),
                    min=return_element_text(container,
                                            './/div[@class="segment segment--mins"]//div[@class="chunk chunk--active"]',
                                            int),
                    sec=return_element_text(container,
                                            './/div[@class="segment segment--secs"]//div[@class="chunk chunk--active"]',
                                            int))


        # print(info,end='\n\n')
        gift_info.append(info)
        # print(container.find_element_by_xpath('//div[@class="c-countdown"]').text)
    print('\n'.join([json.dumps(i) for i in gift_info]))
    # get all the containers
    # get the name
    # get the time left
    return None  # TODO return info


def update_deadline(option_choice_path, info):
    print('option_choice_path')
    print(info)
