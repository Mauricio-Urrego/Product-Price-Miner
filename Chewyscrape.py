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
ProductInfoList = []
RatingList = []
ShippingList = []

driver.get('https://www.chewy.com/b/dry-food-294')
time.sleep(15)
try:
    while True:
        next_page_btn = driver.find_element_by_class_name('cw-pagination__next')
        if next_page_btn.__sizeof__() <1:
            print("no more pages left")
            break
        else:
            time.sleep(10)
            NameText = driver.find_elements_by_class_name('content')
            for i in NameText:
                NameList.append(i.text)

            PriceText = driver.find_elements_by_class_name('price')
            for i in PriceText:
                PriceList.append(i.text)

            ProductInfoText = driver.find_elements_by_class_name('product-info')
            for i in ProductInfoText:
                ProductInfoList.append(i.text)

            RatingText = driver.find_elements_by_class_name('rating.item-rating')
            for i in RatingText:
                RatingList.append(i.text)

            ShippingText = driver.find_elements_by_class_name('shipping')
            for i in ShippingText:
                ShippingList.append(i.text)
            next_page_btn.click()
            time.sleep(10)
finally:
    driver.quit()

    dict = {'Name': NameList, 'Price': PriceList, 'ProductInfo': ProductInfoList, 'Rating': RatingList, 'Shipping': ShippingList}

    import pandas as pd

    df = pd.DataFrame(dict)

    df.to_csv('chewyproductsclean.csv', index=False)

    print("done")
