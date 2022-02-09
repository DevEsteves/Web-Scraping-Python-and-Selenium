from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://finance.yahoo.com/quote/BTC-EUR/history")

with open('eur_btc_rates.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|')
    spamwriter.writerow([driver.find_element(By.CSS_SELECTOR, "thead > tr th:nth-child(1) > span").text, # writes "Date" title element
    driver.find_element(By.CSS_SELECTOR, "thead > tr th:nth-child(5) > span").text]) # writes "Close" title element
    for i in range(1,11):                   #iterates "date" and "close" values until 10 elements
        stringIterator = str(i)             # turns int iterator into string
        spanElementCloseValue = "5"         # Location of span in element
        spamwriter.writerow([driver.find_element(By.CSS_SELECTOR,"tbody > tr:nth-child("+stringIterator+") > td.Py\(10px\).Ta\(start\).Pend\(10px\) > span").text, # writes the respective Date values 
        driver.find_element(By.CSS_SELECTOR, "tbody > tr:nth-child("+stringIterator+") > td:nth-child("+spanElementCloseValue+") > span").text]) # writes close values for the respective Date
driver.quit()