import requests
from bs4 import BeautifulSoup
import image_scraper

def filename(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('img')
    return r"C:\Users\SATVIKA\Desktop\integratemodel\generated_captcha_images\\"+result['src']