#dependencies
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import requests
from splinter import Browser
import pandas as pd
from selenium import webdriver
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # NASA Mars News

    # url for NASA
    nasa_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(nasa_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

    #obtain title text
    news_title = soup.find('div', class_="content_title").get_text()
    print(news_title)

    #obtain paragraph text
    news_p = soup.find('div', class_="rollover_description").get_text()
    print(news_p)

    # JPL Mars Space Image - Featured Image

    # set up splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #use splinter to go to url
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    shortened_url = 'https://www.jpl.nasa.gov'

    imgclick = browser.find_by_id("full_image")
    imgclick.click()
    time.sleep(2)
    moreinfo = browser.find_link_by_partial_text("more info")
    moreinfo.click()
    time.sleep(2)
    #assign the url for the current Featured Mars Image to a variable
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')

    featured_image = image_soup.find('figure', class_='lede').find("img")["src"]
    print(featured_image)

    #
    final_url = shortened_url + featured_image
    print(final_url)


    # Mars Weather

    #twitter url
    twitter_url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    twitter_response = requests.get(twitter_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    twitter_soup = BeautifulSoup(twitter_response.text, 'html.parser')

    #obtain tweet text
    mars_weather = twitter_soup.find('div', class_="tweet-text").get_text()
    print(mars_weather)

    # Mars Facts

    #table url
    table_url = 'https://space-facts.com/mars/'

    #retrieve table
    tables = pd.read_html(table_url)
    tables

    #create dataframe
    df = tables[0]
    df.columns = ['Parameter', 'Actual']
    df.head()

    #set index to parameter
    df.set_index('Parameter', inplace=True)
    df.head()

    #generate html table
    html_table = df.to_html()
    html_table

    #Strip unwanted newlines to clean up the table.
    html_table.replace('\n', '')

    # Hemispheres

    #use splinter to navigate and obtain url for the title
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    browser.find_by_css("a.product-item")[1].click()
    titleurl1 =browser.url


    #open up a Firefox broswer and navigate to web page to obtain title url and image url

    driver = webdriver.Firefox()
    driver.get(titleurl1)

    title_url_1= driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[3]/section/h2[1]')
    print(title_url_1[0].text)

    for a in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'):
        print(a.get_attribute('href'))

    image_url_1= a.get_attribute('href')
    print(image_url_1)

    url_title_1 = (title_url_1[0].text)
    time.sleep(2)
    #use splinter to navigate and obtain url for the title
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    browser.find_by_text("Schiaparelli Hemisphere Enhanced").click()
    titleurl2 =browser.url


    #open up a Firefox broswer and navigate to web page to obtain title url and image url

    driver = webdriver.Firefox()
    driver.get(titleurl2)

    title_url_2= driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[3]/section/h2[1]')
    print(title_url_2[0].text)




    for a in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'):
        print(a.get_attribute('href'))

    image_url_2= a.get_attribute('href')
    print(image_url_2)

    url_title_2 = (title_url_2[0].text)
    time.sleep(2)
    #use splinter to navigate and obtain url for the title
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    browser.find_by_text("Syrtis Major Hemisphere Enhanced").click()
    titleurl3 =browser.url


    #open up a Firefox browser and navigate to web page to obtain title url and image url
    time.sleep(2)
    driver = webdriver.Firefox()
    driver.get(titleurl3)

    title_url_3= driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[3]/section/h2[1]')
    print(title_url_3[0].text)

    for a in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'):
        print(a.get_attribute('href'))

    image_url_3= a.get_attribute('href')
    print(image_url_3)

    url_title_3 = (title_url_3[0].text)
    time.sleep(2)
    #use splinter to navigate and obtain url for the title
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    browser.find_by_text("Valles Marineris Hemisphere Enhanced").click()
    titleurl4 =browser.url


    #open up a Firefox broswer and navigate to web page to obtain title url and image url

    driver = webdriver.Firefox()
    driver.get(titleurl4)

    title_url_4= driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[3]/section/h2[1]')
    print(title_url_4[0].text)

    for a in driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/a'):
        print(a.get_attribute('href'))

    image_url_4= a.get_attribute('href')
    print(image_url_4)

    url_title_4 = (title_url_4[0].text)
    time.sleep(2)
    # use a Python dictionary to store the data using the keys "img_url" and "title_url"
    #img_url = [image_url_1, image_url_2, image_url_3, image_url_4]

    #title_url = [url_title_1, url_title_2, url_title_3, url_title_4]

    # append the dictionary with the image url string and the hemisphere title to a list.
    hemisphere_image_urls = [url_title_1, image_url_1, url_title_2, image_url_2, url_title_3, image_url_3, url_title_4, image_url_4]

    #create a dictionary and append all the scraped data
    mars_data = {}

    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p
    mars_data["featured_image"] = final_url
    mars_data["mars_weather"] = mars_weather
    mars_data["html_table"] = html_table
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_data
