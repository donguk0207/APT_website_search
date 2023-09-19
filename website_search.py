import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebsiteSearcher:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("prefs", {"safebrowsing.enabled": True})
        self.options.add_argument("--start-maximized")
        self.options.add_argument('user-agent=' + user_agent)
        self.chromeDriver = webdriver.Chrome('chromedriver', options=self.options)
        self.waitMaxTime = 60
        self.chromeDriver.implicitly_wait(self.waitMaxTime)

search_keyword = input('phishing page : ')
websites = [
    {'url': 'https://web-check.as93.net/', 'search_box_xpath': '//*[@id="user-input"]'},
    {'url': 'https://www.hybrid-analysis.com/', 'search_box_xpath': '//*[@id="homepage-submit"]/form/div[3]/div/input'},
    {'url': 'https://urlscan.io/', 'search_box_xpath': '//*[@id="url"]'},
    {'url': 'https://www.criminalip.io/ko/domain','search_box_xpath': '//*[@id="__next"]/div[1]/section/div[1]/div/form/div/input'},
    {'url': 'https://seculab.somansa.com/analysis', 'search_box_xpath': '//*[@id="inputData"]'},
    {'url': 'https://rancert.com/check_url.php', 'search_box_xpath': '//*[@id="strUrl"]'},
    {'url': 'https://www.scamadviser.com/', 'search_box_xpath': '/html/body/div[1]/div[4]/div/div[1]/div/form/div/div[1]/div/div[1]/input'},
    {'url': 'https://safeweb.norton.com/?ulang=kor', 'search_box_xpath': '//*[@id="appendedInputButton"]'},
    {'url': 'https://www.websiteplanet.com/ko/webtools/redirected/', 'search_box_xpath': '//*[@id="url"]'},
    {'url': 'https://urlhaus.abuse.ch/browse/', 'search_box_xpath': '//*[@id="search"]'},
    #{'url': 'https://www.virustotal.com/gui/home/url', 'search_box_xpath': '//*[@id="urlSearchInput"]'},
    #{'url': 'https://metadefender.opswat.com/', 'search_box_xpath': '//*[@id="mdc-focus-wrapper"]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/input'},
    #{'url': 'https://urlquery.net/', 'search_box_xpath': '//*[@id="url_submit"]'},
    #{'url': 'https://transparencyreport.google.com/safe-browsing/search', 'search_box_xpath': '//*[@id="scrolling-element"]/safe-browsing-report/ng-component/section/div/search-box/input'},
    #{'url': 'https://www.aioncloud.com/ko/wms-kr/', 'search_box_xpath': '//*[@id="panel-324-0-0-2"]/div/div/div/div/div[2]/input'},
]

website_searcher = WebsiteSearcher()

for i, website in enumerate(websites):
    print(f'{i+1}번째 Site Loading...')
    website_searcher = WebsiteSearcher()
    website_searcher.chromeDriver.get(website['url'])
    search_box = website_searcher.chromeDriver.find_element(By.XPATH, website['search_box_xpath'])
    search_box.send_keys(search_keyword)
    search_box.submit()
    input(f'{i+1}번째 Site Search Success : Next site - Enter...')

website_searcher.chromeDriver.quit()