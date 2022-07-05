from selenium import webdriver
import time,os
from bs4 import BeautifulSoup as bs
import urllib.request 

options = webdriver.ChromeOptions()
# options.headless = True

# driverPath='C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe'
driverPath='C:/Users/gians/Desktop/stuff/chromedriver_win32/chromedriver.exe'
def downloadLink(dir,track):
    br =  webdriver.Chrome(driverPath,options=options)
    theUrl="https://soundcloudtomp3.app"
    br.get(theUrl)
    # time.sleep(5)
    entry=br.find_element_by_css_selector("body > div.jumbotron > div > center > form > div > input")
    entry.send_keys(track[1]) #track[1] is the soundcloud url link of katha
    button=br.find_element_by_css_selector("#fd")
    button.click()

    atag=br.find_elements_by_xpath('//*[@id="dlMP3"]')
    theDownloadLink=atag[2].get_attribute("href")
    urllib.request.urlretrieve(theDownloadLink,f'{dir}{track[0]}.mp3')
    time.sleep(1)
    br.close()

def downloadPlaylist():
    br =  webdriver.Chrome(driverPath,options=options)
    link="https://www.genmp3.net/tracks.php?u=https%3A%2F%2Fsoundcloud.com%2Fnirbaankeertan%2Fsets%2Fgiani-amolak-singh-ji&t=https%3A%2F%2Fsoundcloud.com%2Fnirbaankeertan%2Fsets%2Fgiani-amolak-singh-ji"
    br.get(link)
    br.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    atags=br.find_elements_by_class_name("mp3down")
    time.sleep(5)
    for atag in atags:
        br.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        atag.click()
        print("clicked")
    br.close()
    
dirr="C:/Users/gians/Desktop/test/"


# url="https://soundcloud.com/nirbaankeertan/sets/giani-amolak-singh-ji"
downloadPlaylist()
