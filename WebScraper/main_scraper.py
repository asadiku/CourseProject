from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import time
from page_scraper import get_page_data

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome('./chromedriver.exe', options=options)  # Make sure you have the correct chromedriver installed

base_url = 'https://www.coursera.org'

with open('lectureUrls.txt') as uf:
    lecture_urls = uf.readlines()   # Starting urls for each week's lecture videos (12 total)


def login():
    '''Log in to Coursera page with your school email and password. Maybe solve captcha?'''

    login_url = 'https://www.coursera.org/?authMode=login'
    driver.get(login_url)
    driver.implicitly_wait(20)

    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")

    username.send_keys("your-email")
    password.send_keys("your-password")
    driver.find_element_by_css_selector("._6dgzsvq.css-1af0gyj").click()
    time.sleep(55) # Give some time to manually solve captcha, if needed.


def scrape_each_video(soup):
    '''Scrapes each video transcript data for a given week'''

    video_links = []
    video_elements = soup.select('a[data-click-key="open_course_home.item_layout.click.item_link"]')

    for element in video_elements:
        video_links.append(element['href'])

    for vid_url in video_links:
        time.sleep(4)
        driver.get(base_url + vid_url)
        time.sleep(10)

        res_html = driver.page_source
        soup = BeautifulSoup(res_html,'html.parser')
        get_page_data(soup, base_url + vid_url)


login()
count = 1
for url in lecture_urls:
    print(f"Scraping lecture week {count}/12")
    time.sleep(4)
    driver.get(url)
    time.sleep(10)

    res_html = driver.page_source
    soup = BeautifulSoup(res_html,'html.parser')
    scrape_each_video(soup)
    count += 1

driver.quit()
