from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
import time

chromedriverpath = '/usr/local/bin/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('-headless')
options.add_experimental_option("prefs", {
    "download.default_directory": '/Users/mauriciourrego/Downloads',
    "download.prompt_for_download": False,
})

driver = webdriver.Chrome(executable_path = chromedriverpath) #, options = options)

NameList = []
PriceList = []
#ProductInfoList = []
#RatingList = []
#ShippingList = []

driver.get('https://www.petsmart.com/dog/food/dry-food/#page_name=flyout&category=dog&cta=dryfood')
time.sleep(10)
try:
    while True:
        next_page_btn = driver.find_element_by_class_name('icon-arrow-right')
        if next_page_btn.__sizeof__() <1:
            print("no more pages left")
            break
        else:
            NameText = driver.find_elements_by_class_name('product-name')
            for i in NameText:
                NameList.append(i.text)

            PriceText = driver.find_elements_by_class_name('product-pricing')
            for i in PriceText:
                PriceList.append(i.text)
            next_page_btn.click()
            time.sleep(10)
finally:
    driver.quit()

    dict = {'Name': NameList, 'SalePrice': PriceList}

    import pandas as pd

    df = pd.DataFrame(dict)

    df.to_csv('petsmartproducts1.csv', index=False)

    print("done")
