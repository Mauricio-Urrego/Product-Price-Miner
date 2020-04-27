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

driver.get('https://www.petsuppliesplus.com/Categories/Dog/Food/Dry%20Food#sort=relevancy')
time.sleep(15)
try:
    while True:
        next_page_btn = driver.find_element_by_class_name('coveo-pager-next.coveo-pager-anchor.coveo-pager-list-item')
        if next_page_btn.__sizeof__() <1:
            print("no more pages left")
            break
        else:
            time.sleep(10)
            NameText = driver.find_elements_by_class_name('caption')
            for i in NameText:
                NameList.append(i.text)

            PriceText = driver.find_elements_by_class_name('actual-price')
            for i in PriceText:
                PriceList.append(i.text)

            ProductInfoText = driver.find_elements_by_class_name('sale-price')
            for i in ProductInfoText:
                ProductInfoList.append(i.text)

            RatingText = driver.find_elements_by_class_name('prod-rating')
            for i in RatingText:
                RatingList.append(i.text)
            next_page_btn.click()
            time.sleep(10)
finally:
    driver.quit()

    dict = {'Name': NameList, 'ActualPrice': PriceList, 'Rating': RatingList}

    import pandas as pd

    df = pd.DataFrame(dict)

    df.to_csv('petsuppliesplusproducts.csv', index=False)

    print("done")
