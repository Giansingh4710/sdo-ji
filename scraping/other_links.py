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

    _,links=goldenKhajana("http://sikhsoul.com/golden_khajana/index.php?q=f&f=%2FKeertan%2FBhai+Mohinder+Singh+SDO")
    path="./goldenKhajana"
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
            audio=item.find("img",src="index.php?i=a")
            new_link=baseLink+item.find("a")['href']
            if not audio:
                #only folders are supposed to be in here
                ikirtan(new_link,baseLink)
                continue
            print(new_link)

    base="https://www.ikirtan.com/"
    ikirtan("https://www.ikirtan.com/index.php?q=f&f=%2FBhai_Mohinder_Singh_Jee_SDO",base)
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

    # svLink="https://www.youtube.com/channel/UCqsuEPZckzKnl2M03wp_V6w/videos"
    # sabadVartaraLinks=youtubeChannelLinks(svLink)
    links=['https://www.youtube.com/watch?v=SReNea7V2VA', 'https://www.youtube.com/watch?v=Yreb6P-oNSQ', 'https://www.youtube.com/watch?v=2XGJTXkixIw', 'https://www.youtube.com/watch?v=yGK0raOM8kk', 'https://www.youtube.com/watch?v=jmURku9DIOg', 'https://www.youtube.com/watch?v=Iz0GOsdybUs', 'https://www.youtube.com/watch?v=-URnF2dkRjk', 'https://www.youtube.com/watch?v=dMtFLCIjhyc', 'https://www.youtube.com/watch?v=nsyqV8B5Kko', 'https://www.youtube.com/watch?v=TFw5DIp7B_M', 'https://www.youtube.com/watch?v=zEg8iLCHXAo', 'https://www.youtube.com/watch?v=QbqQQ_PigCI', 'https://www.youtube.com/watch?v=iKvbLsUOc-M', 'https://www.youtube.com/watch?v=f71it9SAn30', 'https://www.youtube.com/watch?v=NXpWb1FvZEI', 'https://www.youtube.com/watch?v=bKWX5ydeEQU', 'https://www.youtube.com/watch?v=-A4rBQ21bj8', 'https://www.youtube.com/watch?v=Nw403HYVkGo', 'https://www.youtube.com/watch?v=3eklX1SL15g', 'https://www.youtube.com/watch?v=eZntxX76xCU', 'https://www.youtube.com/watch?v=BuGmsUT9O6A', 'https://www.youtube.com/watch?v=VjFTZ-KLMM8', 'https://www.youtube.com/watch?v=sciw-0SWxpA', 'https://www.youtube.com/watch?v=JvC8Mkx53XE', 'https://www.youtube.com/watch?v=lckmwaH-xcg', 'https://www.youtube.com/watch?v=VfRXvXTynmo', 'https://www.youtube.com/watch?v=PTb8PCXqZ_M', 'https://www.youtube.com/watch?v=WVFAokmXWdI', 'https://www.youtube.com/watch?v=sViE_wHnIjQ', 'https://www.youtube.com/watch?v=WvVusV2dY_c', 'https://www.youtube.com/watch?v=vVMoOBtuxfc', 'https://www.youtube.com/watch?v=X_zX79Lj9-8', 'https://www.youtube.com/watch?v=LHERKGLaZYk', 'https://www.youtube.com/watch?v=yYmLNmvTwN4', 'https://www.youtube.com/watch?v=eCR8sC3FfOw', 'https://www.youtube.com/watch?v=K4DTsyXx72g', 'https://www.youtube.com/watch?v=6cmGRqNscyM', 'https://www.youtube.com/watch?v=IRlUkrg2Ci0', 'https://www.youtube.com/watch?v=yQGo4mH1bgo', 'https://www.youtube.com/watch?v=i2lsMwAJbdw', 'https://www.youtube.com/watch?v=C8TU4r9rb2s', 'https://www.youtube.com/watch?v=PnQqE6c-ziM', 'https://www.youtube.com/watch?v=ytKUKvzp7ik', 'https://www.youtube.com/watch?v=zx9yeMoEb2Y', 'https://www.youtube.com/watch?v=0ep9PrayM2I', 'https://www.youtube.com/watch?v=7H0_FDlFAF0', 'https://www.youtube.com/watch?v=yueoynBsEOc', 'https://www.youtube.com/watch?v=VBjnZwmEXnM', 'https://www.youtube.com/watch?v=3LnrHdvAWB0', 'https://www.youtube.com/watch?v=TufSi45TbkE', 'https://www.youtube.com/watch?v=AljST7rRmEY', 'https://www.youtube.com/watch?v=v3wJnZgN0sE', 'https://www.youtube.com/watch?v=d4MqoQnPLQA', 'https://www.youtube.com/watch?v=X6BMaUADSnA', 'https://www.youtube.com/watch?v=96bBT-rH8d8', 'https://www.youtube.com/watch?v=zCS8HvVVZ8o', 'https://www.youtube.com/watch?v=ZKw5U0fVsa8', 'https://www.youtube.com/watch?v=_N6gK2Wrxik', 'https://www.youtube.com/watch?v=H1Bv2Ri_hgA', 'https://www.youtube.com/watch?v=6SGec24caPU', 'https://www.youtube.com/watch?v=2R7448JMQOg', 'https://www.youtube.com/watch?v=JC4wuoII3S0', 'https://www.youtube.com/watch?v=1aScJ8lskaU', 'https://www.youtube.com/watch?v=GPfYavyS2Do', 'https://www.youtube.com/watch?v=HjxH6LpXKm8', 'https://www.youtube.com/watch?v=80MGZ0MtHaI', 'https://www.youtube.com/watch?v=KqjW1Ukb60s', 'https://www.youtube.com/watch?v=48XKaW1J62w', 'https://www.youtube.com/watch?v=urQNegvQMJo', 'https://www.youtube.com/watch?v=G32u0ChTPvk', 'https://www.youtube.com/watch?v=btVeRAwtReM', 'https://www.youtube.com/watch?v=BiRp-EjtEjk', 'https://www.youtube.com/watch?v=7nPBq0VIrwU', 'https://www.youtube.com/watch?v=9T1JSGo8wpY', 'https://www.youtube.com/watch?v=Y4coX4gRiEA', 'https://www.youtube.com/watch?v=rGi3pijU93w', 'https://www.youtube.com/watch?v=gNXrX4eOADs', 'https://www.youtube.com/watch?v=mSeuDuuNL_o', 'https://www.youtube.com/watch?v=q_ENZZXUmHk', 'https://www.youtube.com/watch?v=Q_1OsIGfngg', 'https://www.youtube.com/watch?v=Lb6vbZXqApQ', 'https://www.youtube.com/watch?v=kEtvQAMNBIU', 'https://www.youtube.com/watch?v=uwEDib4yZ8s', 'https://www.youtube.com/watch?v=2ByisT0ryyk', 'https://www.youtube.com/watch?v=4_JWm6lCSpE', 'https://www.youtube.com/watch?v=al1RTzfxcWE', 'https://www.youtube.com/watch?v=zSDnWBpzQRM', 'https://www.youtube.com/watch?v=bGVdECWEF1I', 'https://www.youtube.com/watch?v=63YU3CTrrRE', 'https://www.youtube.com/watch?v=w3rF4feybH8', 'https://www.youtube.com/watch?v=BITfGWd1E7o', 'https://www.youtube.com/watch?v=uI8jwztxOts', 'https://www.youtube.com/watch?v=tblUNtpombg', 'https://www.youtube.com/watch?v=ijuBLxJsoTk', 'https://www.youtube.com/watch?v=g9pWiurKOyo', 'https://www.youtube.com/watch?v=esFNgyrYFVg', 'https://www.youtube.com/watch?v=36aXVB3olPU', 'https://www.youtube.com/watch?v=vwbo-zam8K4', 'https://www.youtube.com/watch?v=WjbbgYw5Zyo', 'https://www.youtube.com/watch?v=ahg2zD6NPP8', 'https://www.youtube.com/watch?v=NH5aZtGr4WE', 'https://www.youtube.com/watch?v=uWvWd3pTcEY', 'https://www.youtube.com/watch?v=2sgJ_FfnVZM', 'https://www.youtube.com/watch?v=XVXAe2kdlrM', 'https://www.youtube.com/watch?v=9D2cTsh4hHk', 'https://www.youtube.com/watch?v=AqsSrCcXedY', 'https://www.youtube.com/watch?v=Q6ojXUQQzDE', 'https://www.youtube.com/watch?v=FAJ9PSpGLs8', 'https://www.youtube.com/watch?v=1U2_Tj3NkWk', 'https://www.youtube.com/watch?v=x3IBNclrioU', 'https://www.youtube.com/watch?v=ztVsz2rVvDM', 'https://www.youtube.com/watch?v=5J-L4D1eFgQ', 'https://www.youtube.com/watch?v=N5tlbGXj7rc', 'https://www.youtube.com/watch?v=sCaJHF6WERs', 'https://www.youtube.com/watch?v=vRxuC0owCOc', 'https://www.youtube.com/watch?v=XxLwyMTTssk', 'https://www.youtube.com/watch?v=SiAAWvxH9K8', 'https://www.youtube.com/watch?v=pN2XtNYXMGo', 'https://www.youtube.com/watch?v=FC6Sdh1H5BI', 'https://www.youtube.com/watch?v=ORqegnRQhzs', 'https://www.youtube.com/watch?v=uuPS2g5Vcm4', 'https://www.youtube.com/watch?v=aPkCRwdsEeA', 'https://www.youtube.com/watch?v=mS2RgXcrv0Q', 'https://www.youtube.com/watch?v=g9fDo6-4V8s', 'https://www.youtube.com/watch?v=2goyXIzS5sk', 'https://www.youtube.com/watch?v=cIHdCmI0_lY', 'https://www.youtube.com/watch?v=W5CC6orlrws', 'https://www.youtube.com/watch?v=lODhP-sGqjc', 'https://www.youtube.com/watch?v=aGrQ9UbLTA0', 'https://www.youtube.com/watch?v=dtIGtwf9ksQ', 'https://www.youtube.com/watch?v=yk7v6UuZRJI', 'https://www.youtube.com/watch?v=7V2NN-ne2Bs', 'https://www.youtube.com/watch?v=FBPoUbyQoT4', 'https://www.youtube.com/watch?v=-PTTuV9Id1E', 'https://www.youtube.com/watch?v=w10s2_wOW7w', 'https://www.youtube.com/watch?v=C8CnGxvXq3s', 'https://www.youtube.com/watch?v=5EmfjqJWHV0', 'https://www.youtube.com/watch?v=IwP2cdJDXUE', 'https://www.youtube.com/watch?v=-59_G7BKaMo', 'https://www.youtube.com/watch?v=sOlbKyQ40jo', 'https://www.youtube.com/watch?v=eC5ine9RNzA', 'https://www.youtube.com/watch?v=MoJTKmr0-SU', 'https://www.youtube.com/watch?v=ZDTBooWPEwM', 'https://www.youtube.com/watch?v=yn7V81ALw2I', 'https://www.youtube.com/watch?v=0O9xYbNutEQ', 'https://www.youtube.com/watch?v=l4lhcqkgWl4', 'https://www.youtube.com/watch?v=xlTe9hQGjN0', 'https://www.youtube.com/watch?v=UX6B6CpoM6Q', 'https://www.youtube.com/watch?v=jX_J-aeAtrI', 'https://www.youtube.com/watch?v=NS8zfKHkURA', 'https://www.youtube.com/watch?v=oSM2Jgsolxo', 'https://www.youtube.com/watch?v=hF6ZP0RkBn0', 'https://www.youtube.com/watch?v=c-IlVM5giwI', 'https://www.youtube.com/watch?v=WerPhwJXD_A', 'https://www.youtube.com/watch?v=-2dAa7aonKk', 'https://www.youtube.com/watch?v=9Kfd72nFgHE', 'https://www.youtube.com/watch?v=uMYZIv4--bI', 'https://www.youtube.com/watch?v=AlJmtNoMNhc', 'https://www.youtube.com/watch?v=fcSqf89-17o', 'https://www.youtube.com/watch?v=WrqQI18wSHI', 'https://www.youtube.com/watch?v=zGhi1WFp0Ww', 'https://www.youtube.com/watch?v=6IdZd1Cfr60', 'https://www.youtube.com/watch?v=hSw9EVLBRJM', 'https://www.youtube.com/watch?v=uslheQ2TFXY']
    downloadLinks(links,"./sabadVartara/")

# golden_khajana()
i_kirtan();
# youtube()
