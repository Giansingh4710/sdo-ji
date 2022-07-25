from selenium import webdriver
import time,os
from bs4 import BeautifulSoup as bs
import urllib.request 

options = webdriver.ChromeOptions()
# options.headless = True

# driverPath='C:\\Users\\gians\\Desktop\\stuff\\chromedriver.exe'
driverPath='C:/Users/gians/Desktop/stuff/chromedriver_win32/chromedriver.exe'
def downloadPlaylist(link):
    br =  webdriver.Chrome(driverPath,options=options)
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
    
def getAllSDOlinks():
    br =  webdriver.Chrome(driverPath,options=options)
    theUrl="https://soundcloud.com/search/sounds?q=bhai%20mohinder%20singh%20sdo"
    br.get(theUrl)
    # time.sleep(5)
    for i in range(15):
        print(i)
        br.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
    tracks=br.find_elements_by_class_name("searchItem__trackItem")
    atags=[track.find_elements_by_tag_name('a')[3] for track in tracks]
    links=[i.get_attribute("href") for i in atags]
    print(links)
    br.close()
    return links

def getLinksForPlaylist(link): #gets links for katha in a playlist. This func is used for the func above
    br =  webdriver.Chrome(driverPath,options=options)
    br.get(link)
    scroll=0
    end=False
    while not end:
        firstScroll=br.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(1)
        if firstScroll==scroll:
            end=True
        else:
            scroll=firstScroll
    atags=br.find_elements_by_css_selector("div > div.trackItem__content.sc-truncate > a")
    links=[i.get_attribute('href') for i in atags]
    br.close()
    return links

def downloadLinks(path,links):
    if(os.path.isdir(path)==False):
        os.mkdir(path)
    total_dwn=0
    for link in links:
        name=link.split("/")[-1]
        track=[name,link]
        try:
            downloadLink(path,track)
            print("Downloaded!")
            total_dwn+=1
        except Exception:
            print(f"No Download - {track}")
    print(f"Downloaded {total_dwn} of {len(links)}")
    
def downloadLink(dir,track):
    br =  webdriver.Chrome(driverPath,options=options)
    # theUrl="https://soundcloudtomp3.app"
    theUrl="https://soundcloudmp3.org/"
    br.get(theUrl)
    # time.sleep(5)
    entry=br.find_element_by_css_selector("#conversionForm > div > input.form-control")
    entry.send_keys(track) #track[1] is the soundcloud url link of katha
    button=br.find_element_by_css_selector("#conversionForm > div > span > button")
    button.click()

    print("After download clicked !!!!!")
    atag=br.find_elements_by_xpath('//*[@id="dlMP3"]')
    theDownloadLink=atag[2].get_attribute("href")
    urllib.request.urlretrieve(theDownloadLink,f'{dir}{track.split("/")[-1]}.mp3')
    time.sleep(1)
    br.close()

dirr="C:/Users/gians/Desktop/test/bhai_mehar_singh/"
# url="https://soundcloud.com/nirbaankeertan/sets/giani-amolak-singh-ji"
# link="https://www.genmp3.net/tracks.php?u=https%3A%2F%2Fsoundcloud.com%2Fnirbaankeertan%2Fsets%2Fgiani-amolak-singh-ji&t=https%3A%2F%2Fsoundcloud.com%2Fnirbaankeertan%2Fsets%2Fgiani-amolak-singh-ji"
# downloadPlaylist(link)
# links=getAllSDOlinks()

link="https://soundcloud.com/satnam-singh-b/sets/dr-pritam-singh-ji-anjaan"
[print(i) for i in getLinksForPlaylist(link)]
link="https://soundcloud.com/nirbaankeertan/sets/dr-pritam-singh-ji-anjaan"
[print(i) for i in getLinksForPlaylist(link)]

# link='https://soundcloud.com/harsimransinghlalli/bhai-mohinder-singh-sdo-aree-bayee-gobind-naam-mat-beesrai',
# downloadLink(dirr,link)
