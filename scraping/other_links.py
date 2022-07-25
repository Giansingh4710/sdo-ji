from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import requests,os
from bs4 import BeautifulSoup as bs
import urllib.request

def download(links,path):
    print("Downloading..."+path)
    if path[-1]!="/":
        path+="/"
    if(os.path.isdir(path)==False):
        os.mkdir(path)
    count=0
    for i in links:
        count+=1
        title=i.split("/")
        title=''.join(title[-1])
        title=title.replace("%20"," ",-1)
        title=f'{count}) {title}'
        try:
            urllib.request.urlretrieve(i,path+title)
            print(f"Downloaded: {title}")
        except Exception as e:
            print(f"No download :{e}")

def golden_khajana():
    def goldenKhajana(link):
        res=requests.get(link)
        soup=bs(res.text,"lxml")
        td=soup.find_all("td",valign="top")
        atags=[i.find("a") for i in td]
        links=[]
        names=[]
        for i in atags:
            title="http://sikhsoul.com"+i["href"]
            if title not in links:
                links.append("http://sikhsoul.com"+i["href"])
            if i.text not in names:
                names.append(i.text)
        names=names[1:]        
        return names,links

    theLink="http://sikhsoul.com/golden_khajana/index.php?q=f&f=%2FKeertan%2FBhai+Mohinder+Singh+SDO"
    theLink="http://sikhsoul.com/golden_khajana/index.php?q=f&f=%2FKeertan%2FBhai+Joginder+Singh+Talwara"
    theLink="http://sikhsoul.com/golden_khajana/index.php?q=f&f=%2FKeertan%2FBhai+Mehar+Singh"
    _,links=goldenKhajana(theLink)
    # path="./goldenKhajana"
    # download(links,path)
    [print(i) for i in links]


def i_kirtan():
    def ikirtan(link,baseLink): 
        res=requests.get(link)
        soup=bs(res.text,"lxml")
        if link[-1]!='/': link+='/'
        
        tables=soup.find_all("table",bgcolor="CCCCCC",width="80%",cellspacing="0",cellpadding="4",border="0")
        tables+=soup.find_all("table",bgcolor="9999CC")
        for item in tables:
            audio=item.find("img",src="index.php?i=a") or item.find("img",src="index.php?i=v")
            new_link=baseLink+item.find("a")['href']
            if not audio:
                #only folders are supposed to be in here
                print(f"folder: {new_link}")
                ikirtan(new_link,baseLink)
                continue
            print(new_link)

    base="https://www.ikirtan.com/"
    theLink="https://www.ikirtan.com/index.php?q=f&f=%2FBhai_Mohinder_Singh_Jee_SDO"
    theLink="http://www.ikirtan.com/index.php?f=%2FBhai_Joginder_Singh_Jee_Talwara&q=f"
    theLink="https://www.ikirtan.com/index.php?q=f&f=%2FBhai_Mehar_Singh_Jee"
    ikirtan(theLink,base)
    # ikirtan("https://www.ikirtan.com/index.php?q=f&f=%2F_Bhai_Jeevan_Singh_Jee",base)
    # path="./ikirtan"


def youtube():
    from pytube import YouTube
    def youtubeChannelLinks(urll):
        # br = webdriver.Chrome('/mnt/c/Users/gians/Desktop/stuff/chromedriver_win32/chromedriver.exe')#,options=options)
        br = webdriver.Chrome('C:/Users/gians/Desktop/stuff/chromedriver_win32/chromedriver.exe')#,options=options)
        br.get(urll)
        html = br.find_element_by_tag_name('html')
        for i in range(150):
            html.send_keys(Keys.END) #scroll to end of page
        content=br.page_source.encode('utf-8').strip()
        br.close()
        soup=bs(content,"lxml")
        vids=soup.findAll("a",id="video-title") #this highlghts ALL the titles under the thumnail and has the href in it
        print("Total videos: "+str(len(vids)))
        hrefs=["https://www.youtube.com"+i.get("href") for i in vids] #hrefs from the videos
        return hrefs

    def downloadLinks(links,path):
        print("Download youtube link to "+path)
        if path[-1]!="/":
            path+="/"
        if(os.path.isdir(path)==False):
            os.mkdir(path)

        count=0
        for url in links:
            count+=1;
            try:
                yt = YouTube(url)
                yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(path)
                print("Downloaded: "+str(count)+")"+url)
            except Exception as e:
                print(e)
                print("Couldn't download "+str(count)+")"+url)

        return

    svLink="https://www.youtube.com/channel/UCqsuEPZckzKnl2M03wp_V6w/videos"
    links=youtubeChannelLinks(svLink)
    downloadLinks(links,"./sabadVartara/")

def sikhRoots():
    def sikh_roots(link):
        br = webdriver.Chrome('C:/Users/gians/Desktop/stuff/chromedriver_win32/chromedriver.exe')#,options=options)
        br.get(link)
        time.sleep(5)
        tracks=br.find_elements_by_class_name("song-icons")
        links=[i.find_element_by_tag_name('a').get_attribute('href') for i in tracks]
        #i just clicked on each link and that downloaded them
        [print(i) for i in links]
        # for i in tracks:
            # atag=i.find_element_by_tag_name('a')
            # atag.click()
    theLink="https://www.sikhroots.com/audio-mp3/M/Bhai-Mehar-Singh/Mixed-Kirtan"
    sikh_roots(theLink)
        

golden_khajana()
# i_kirtan();
# youtube()
# sikhRoots()
