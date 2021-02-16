from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import scraping
import solve_captchas_with_model

web = webdriver.Chrome(ChromeDriverManager().install())
URL='https://satvika-eda.github.io/captchaweb/index.html'
web.get(URL)

time.sleep(3)
#/html/body/div/form/img
name=scraping.filename(URL)
result=solve_captchas_with_model.decoder(name)
last = web.find_element_by_xpath('//*[@id="captcha"]')
last.send_keys(result)

time.sleep(2)

Submit = web.find_element_by_xpath('/html/body/div/form/button')
Submit.click()