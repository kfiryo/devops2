import requests
from requests.exceptions import InvalidURL
from selenium import webdriver
# try:
#     response = requests.get("httpswldjfnsdgf:dsf hdsfg")
# except InvalidURL:
#     print("invalid url was given")

driver = webdriver.Chrome('/home/user/drivers/chromedriver')
driver.get("file:///C:/devops%20vid/L4/tip_calc/tip_calc/index.html")
billamt = driver.find_element(by="id", value= "billamt")
billamt.send_keys("100")
serviceQual = driver.find_element(by="xpath", value= "//*[@id=\"serviceQual\"]/option[5]")
serviceQual.click()
peopleamt = driver.find_element(by="id", value= "peopleamt")
peopleamt.send_keys("5")
music = driver.find_element(by="id", value= "music")
music.send_keys("2")
calculate = driver.find_element(by="id", value= "calculate")
calculate.click()
actual = driver.find_element(by="id", value= "tip").text
expected = "4.00"

assert expected == actual

driver.close()
