import urllib.request
from selenium import webdriver
import time,os

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--headless")
# options.add_argument={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}#my user agent
br = webdriver.Chrome('C:/Users/gians/Desktop/stuff/chromedriver_win32/chromedriver.exe')#,options=options)

def getKeertanis(keertanis):
    peopleUrl={}
    for keertani in keertanis:
        br.get("https://www.akj.org/keertan.php")
        br.find_element_by_css_selector("#select2-keert_drpdwn-container").click()
        dropDown=br.find_element_by_css_selector("body > span > span > span.select2-search.select2-search--dropdown > input")
        dropDown.send_keys(keertani) #send name of keertani to input box

        optCont=br.find_element_by_css_selector("#select2-keert_drpdwn-results")
        optCont=optCont.find_elements_by_tag_name('li')

        optLst=[i.text for i in optCont]
        if optLst[0]=='No results found':
            print(f"{keertani}: not valid input")
            continue
        for i in range(len(optLst)):
            print(f'{i+1}) {optLst[i]}')
        
        ind=0;
        if len(optLst)>1:
            ind=int(input("Type the number for the keertani you want: "))-1  #if more than 1 keertani of that name, you can pick which one you want
        theKeertani=optLst[ind]  
        print(theKeertani, end="\n\n")
        optCont[ind].click()
        br.find_element_by_css_selector("input.btn").click() #click search button
        peopleUrl[theKeertani]=br.current_url
    print(peopleUrl)
    return peopleUrl

#this will take in the dictionary generated from the getKeertanis func
def getShabads(keertanis,maxDepth=100,recursed=0):
    print("Finding tracks...")
    keertanTracks={}
    for keertani in keertanis:
        br.get(keertanis[keertani]) #the key is the name and the value is the url
        pluses=br.find_elements_by_class_name("fa-plus")
        keertanTracks[keertani]=[]
        for plus in pluses:
            plus.click()
            time.sleep(0.2)  #All this code above in this func is to open all the '+' buttons on the akj website so I can scrape the shabads
        atags=br.find_elements_by_tag_name("a")
        for atag in atags:
            link=atag.get_attribute("href")
            if link!=None:
                if 'Keertan' in link and "akj" in link and "mp3" in link:  #there are alot of href links on the site so this basiclly only adds the keertani file and not the other links
                    keertanTracks[keertani].append(link)
        nextPageUl=br.find_elements_by_class_name("setPaginate") #on the buttom of the page, if the keetani has more than 1 page of keertani, this will be there
        if recursed>=(maxDepth-1): continue #don't want to recurse for all keertan
        if len(nextPageUl)>0: #if more than one page
            li=nextPageUl[0].find_elements_by_tag_name("li")
            actualPages=li[2:-2] #so basically the buttom page switcher is a ul tag. The first li tag is to let you know what page your are on like "Page 2 of 4". The last two li tags are "Next" and "Last" buttons
            theLinks=[i.find_element_by_tag_name("a").get_attribute("href") for i in actualPages] #get all the links for the differt pages of the keertani if they have more than 1
            for i in theLinks: #links to the differt pages of the same keerani
                if None not in theLinks:  #When you are on like page "2 of 5", the second li tag will have no href since you are in that link rn so it will give none. This way in the next itteration when you recurse, it wont keep recusing again becaue there will be a none in the list. This way it will only recurse once for each page
                    tracksOnOtherPage=getShabads({keertani:i},maxDepth,recursed+1)
                    for track in tracksOnOtherPage[keertani]:
                        keertanTracks[keertani].append(track)
    return keertanTracks 


def download(keertanis,thePath):
    for keertani in keertanis:
        counter=0
        path=thePath+keertani
        os.mkdir(path)
        tracks=keertanis[keertani]
        for ind,track in enumerate(tracks):
            counter+=1
            b=track.split('/')
            title=b[-1][:-1]+"3"
            title=f"{counter}) {title}"
            try:
                urllib.request.urlretrieve(track,f"{path}\\{title}")
                print(f"Downloading track {ind+1} of {len(tracks)} - {title}")
            except Exception:
                print(f"Couldn't download: {title}")

# keertanis=["Bibi Sant Kaur","bhai harsimran singh", "bibi harkiran kaur", "bhai gurbir singh","bibi baljinder kaur", "bhai jagjit singh", "bhai amolak singh","bhai harpreet singh toronto","bhai prabhjot singh delhi","bhai gurinder singh california","bhai davinderbir singh","bhai gursharan singh faridabad","bhai pritpal singh regina", "bhai dilveer singh"]
keertanis=["Bhai jeevan Singh"]
keertanis=["Bhai mehar"]
a=getKeertanis(keertanis) #{'keetaniName':linkToKeetantracksBykeertani}
pages=1
# shabads=getShabads(a,pages) #{'keertaniName': [links to all their tracks]}

shabads=getShabads(a);
with open("./linksOfTracks.txt",'w') as file:
    for keertani in shabads:
        for j in shabads[keertani]:
            file.write(j+",\n");

        
# path="C:/Users/gians/Desktop/test/akj/"
# if not os.path.isdir(path):
    # os.mkdir(path)
# download(shabads,path)
