from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

def getSources():

    page = webdriver.Firefox()
    page.get('https://www.rotowire.com/baseball/news.php?injuries=all')

    time.sleep(10)
    soup = BeautifulSoup(page.page_source, 'html.parser')
    page.close()

    hyperlinks = [subSoup.find_all('a') for subSoup in soup.find_all('div', {'class':'news-update is-injured'})]
    hyperlinks = [links for nested_hyperlinks in hyperlinks for links in nested_hyperlinks]
    hyperlinks = [subSoup['href'] for subSoup in hyperlinks if 'twitter' in subSoup['href']]
    accounts = set([twitterLink.split('/')[3] for twitterLink in hyperlinks])
    accounts = {accountNames + '\n' for accountNames in accounts}

    file = open('accountList.txt', 'r')
    text = file.readlines()
    file.close()

    with open('accountList.txt', 'w') as myfile:
        for twitterAccounts in set(text).union(accounts):
            myfile.write(twitterAccounts)
            
    print(len(set(text).union(accounts)), " new sources.")
