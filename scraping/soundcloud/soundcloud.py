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

def downloadLinks(directory,links):
    total_dwn=0
    for link in links:
        name=link.split("/")[-1]
        track=[name,link]
        try:
            downloadLink(directory,track)
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

dirr="C:/Users/gians/Desktop/test/sdo_soundcloud/"
# url="https://soundcloud.com/nirbaankeertan/sets/giani-amolak-singh-ji"
# link="https://www.genmp3.net/tracks.php?u=https%3A%2F%2Fsoundcloud.com%2Fnirbaankeertan%2Fsets%2Fgiani-amolak-singh-ji&t=https%3A%2F%2Fsoundcloud.com%2Fnirbaankeertan%2Fsets%2Fgiani-amolak-singh-ji"
# downloadPlaylist(link)
# links=getAllSDOlinks()
links=[
    'https://soundcloud.com/harsimransinghlalli/bhai-mohinder-singh-sdo-aree-bayee-gobind-naam-mat-beesrai',
    'https://soundcloud.com/sikhvibes/naam-abias-bhai-jeevan-singh-chaani-ji-bhai-mohinder-singh-sdo-and-bhai-manmohan-singh-la',
    'https://soundcloud.com/essenceofsikhi/bhai-mohinder-singh-jee-sdo',
    'https://soundcloud.com/user-178946015/bhai-mohinder-singh-sdo-and-joginder-singh-talwara-keertan-1970s-with-jaspal-singh-on-tabla',
    'https://soundcloud.com/user-993389194/full-asa-kee-vaar-bhai-mohinder-singh-sdo',
    'https://soundcloud.com/nek-singh-1/bhai-mohinder-singh-sdo-1976-ludhiana-smagam',
    'https://soundcloud.com/nav-singh-2/bhai-mohinder-singh-sdo-sabh-dhan-kahu-gur-satguru',
    'https://soundcloud.com/user-178946015/bhai-mohinder-singh-sdo-rehne-rehe-soyee-sikh-mera-india-1970s',
    'https://soundcloud.com/purathankirtan/giddar-dakh-na-aapparehh-1971-bhai-mohinder-singh-sdo',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-amritvela-naam-abhiyaas-puratan',
    'https://soundcloud.com/user-178946015/bhai-mohinder-singh-sdo-and-chaani-ji-on-tabla-early-70s-bin-ekh-naam',
    'https://soundcloud.com/user-178946015/bhai-mohinder-singh-sdo-and-bibi-harjit-kaur-moga-smagam',
    'https://soundcloud.com/mike-john-256691507/bhai-mohinder-singh-ji-sdo-70s',
    'https://soundcloud.com/tuhikharghdhara/bhai-mohinder-singh-jee-sdo-on-disease-and-illness',
    'https://soundcloud.com/purathankirtan/jo-mann-chitt-thudh-bhai-mohinder-singh-sdo-la-1983',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-alternate-version-2-amritvela-naam-abhiyaas-puratan',
    'https://soundcloud.com/puratan-keertan/bhai-mohinder-singh-ji-sdo',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-amrit-ras-peeaa-gur-shabadee-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-alternate-version-amritvela-naam-abhiyaas-puratan',
    'https://soundcloud.com/naamras/bhai-mohinder-singh-jee-sdo-rehras-sahib',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-man-re-thir-raho-mat-kat-jaahee-jeeo-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-bin-saadhoo-jo-jeevanaa-teto-birathaaree-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-sdo-ji-doojaa-bhram-garr-kattiaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-5th-february-1966-mul-khareedee-laalaa-golaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-1',
    'https://soundcloud.com/sikhvibes/rehras-sahib-with-shabads-bhai-mohinder-singh-sdo',
    'https://soundcloud.com/dsitaly/bhai-mohinder-singh-sdo-maaee',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-aae',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-nit-sant-janaa-kee-sangat-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-sdo-ji-ludhiana-1976-ouh-gur-gobind-hoei-pragattiaa',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-and-bibi-kirpal-kaur-ji-hum-tin-ke-charan-pakhaalade-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-aae-mil-gursikh-aae-mil-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-soote-kau-jaagat-kahai-jaagat-kau-sootaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-1979-laakh-jihavaa-deho-mere-piaare-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-asa',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-5',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-kouoo-jaagai-har-jan-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-taaraa-charriaa-lamaa-kio-nadar-nihaaliaa-raam-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-and',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-har-har-naam-apaar-amolee-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-ous-kai-muh-ddittai-sabh-paapee-tariaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-vin-gur-mukat-n-hovaee-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-un',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-khalsa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-lekha-parreeai-har-naam-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-aisaa-jag-dekhiaa-jooaaree-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-gurbaannee-sunn-mail-gavaae-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-bhaj-man-mere-eko-naam-puratan-kirtan',
    'https://soundcloud.com/harjansingh/bhai-mohinder-singh-sdo-saeh-sonjog-karu-mera-pyaare-jit-rasna-gravesend-oct-1983',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-amrit-bhojan-naam-har-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-paarbraham-tin-kau-santusht-bheiaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-8',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-har',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo',
    'https://soundcloud.com/sikhvibes/sevee-satigur-aapanaa-bhai-mohinder-singh-sdo',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-naa',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-jal-jao-jeevan-naam-binaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-sehaj-kathaa-prabh-kee-at-meettee-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-amrit-har-kaa-naam-saadhsang-raaveeai-jeeo-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-ek',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-sachee-teree-kaar-deh-deiaal-too-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-maaee-khaat-aaeio-ghar-pootaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-bhagat-janaa-kai-muh-ddittai-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-man-rasik-rasan-naam-japat-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-2',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-3',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-6',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-maadho-sadhoo-jan-deho-milaae-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-so-aisaa-har-naam-dhiaaeeai-man-mere-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-eio-kio-kant-piaaree-hovaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-4',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-jo',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-tere-jan-dekhann-paavaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-mil-reheeai-prabh-saadh-janaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-hau',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-mere-raam-torr-bandhan-maaeiaa-puratan-kirtan',
    'https://soundcloud.com/naamras/bikhamo-bikham-akhaarraa-mai-gur-mil-jeethaa-raam-bhai-mohinder-singh-jee-sdo-1',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-beantaa-beant-gun-tere-ketak-gaavaa-raam-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-satgur-aagai-sees-bhet-deo-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-fir',
    'https://soundcloud.com/naamras/bikhamo-bikham-akhaarraa-mai-gur-mil-jeethaa-raam-bhai-mohinder-singh-jee-sdo-1',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-fir',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-sunn-kai-sadh-maahee-daa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-9',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-saaee-naam-amol-keem-n-koee-jaanndo-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-too',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-din-rainn-saas-saas-gunn-gaavaa-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-1983-gurbaannee-sunn-mail-gavaae-puratan-kirtan',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-7',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-atte-pehar-ikatai-livai-puratan-kirtan',
    'https://soundcloud.com/purathankirtan/so-kishh-kar-jit-chhutte-prani-1971-bhai-wohinter-singh-sdo',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-ji-sdo-gur',
    'https://soundcloud.com/tiger-singh-246115537/bhai-mohinder-singh-jii-sdo',
    'https://soundcloud.com/kirtan-sewa-malaysia/asa-di-vaar-bhai-mohinder-singh-ji-sdo',
    'https://soundcloud.com/tiger-singh-246115537/bhai-mohinder-singh-sdo-fatehgarh-korotan-moga-akhand-kirtan-part-2',
    'https://soundcloud.com/user-879440930/bhai-mohinder-singh-jee-sdo',
    'https://soundcloud.com/13naam/aesa-mera-raam-bhai-mohinder',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-624110473',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-388887751',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-681637598',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-541312481',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-913466622',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-920454976',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-698718220',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-705879740',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-60512016',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-125074077',
    'https://soundcloud.com/akjdotorg/akj-37-00-bhai-mohinder-singh',
    'https://soundcloud.com/akjdotorg/akj-39-01-bhai-mohinder-singh',
    'https://soundcloud.com/akjdotorg/akj-34-00-bhai-mohinder-singh',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-424927826',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-185196240',
    'https://soundcloud.com/akjdotorg/akj-36-01-bhai-mohinder-singh',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-182814558',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-914630190',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-43688550',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-40858393',
    'https://soundcloud.com/akjdotorg/akj-41-00-bhai-mohinder-singh',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-380704592',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-552233831',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-338445983',
    'https://soundcloud.com/akjdotorg/akj-35-01-bhai-mohinder-singh',
    'https://soundcloud.com/akjdotorg/akj-42-05-bhai-mohinder-singh',
    'https://soundcloud.com/akjdotorg/akj-36-02-bhai-mohinder-singh',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-397614732',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-54294222',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-160541037',
    'https://soundcloud.com/akjdotorg/akj-35-04-bhai-mohinder-singh',
    'https://soundcloud.com/akjdotorg/akj-44-02-bhai-mohinder-singh',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-137810295',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-566814935',
    'https://soundcloud.com/akjdotorg/akj-35-02-bhai-mohinder-singh',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-943514390',
    'https://soundcloud.com/satnam-singh-b/bhai-mohinder-singh-158871042',
    'https://soundcloud.com/nek-singh-1/1980s-simran-by-mohinder-singh-ji-sdo',
    'https://soundcloud.com/satnam-singh-b/bhai-saheb-bhai-mohinder-singh-ji-simran',
    'https://soundcloud.com/kirtan-ras-singh/mohinder-singh-sdo-akj-awesome-moments',
    'https://soundcloud.com/jagjeevan-singh-643278772/mohinder-singh-sdo-meraa-man-laagaa-hai-raam-piaare',
    'https://soundcloud.com/satnam-singh-b/chaupai-saheb-bhai-saheb-bhai-mohinder-singh-ji',
    'https://soundcloud.com/jaskirat-singh-480802770/mohinder-singh-sdo-akj',
    'https://soundcloud.com/vismaad/aisi-preet-karo-man-mere-raag-asavari-bhia-joginder-singh-ji-bhai-mohinder-singh-ji',
    'https://soundcloud.com/satnam-singh-b/bhai-saheb-bhai-mohinder-singh',
    'https://soundcloud.com/vismaad/aad-sateh-jugad-sateh-bhai',
    'https://soundcloud.com/gs-ss/bajat-basant-bhai-mohinder-singh-ji-hazoor-sahib',
    'https://soundcloud.com/nirbaankeertan/bhai-mohinder-singh-hazoor-sahib-34-rehni-rahe',
    'https://soundcloud.com/sikh2inspire/jaap2015-day11-bhai-mohinder-singh-ji',
    'https://soundcloud.com/sikh2inspire/bhai-mohinder-singh-ji-simran',
    'https://soundcloud.com/nirbaankeertan/bhai-mohinder-singh-hazoor-sahib-65-aval-allah',
    'https://soundcloud.com/satnam-singh-b/bhai-saheb-bhai-mohinder-singh-ji-janam-marann-duhahoo-meh-naahee',
    'https://soundcloud.com/harvinder-singh-3/basantkeevaar',
    'https://soundcloud.com/akjdotorg/akj-26-02-bhai-mohinder-singh',
    'https://soundcloud.com/gurumahimatv/hamari-pyari-raag-bilaskhani-todi-bhai-balbir-singh-g-on-tabla-bhai-mohinder-singhi-never-listen',
    'https://soundcloud.com/sikh2inspire/bhai-mohinder-singh-ji',
    'https://soundcloud.com/nirbaankeertan/bhai-mohinder-singh-hazoor-sahib-24-bajat-basant',
    'https://soundcloud.com/dgnsounds/36-day-3-bhai-mohinder-singh-ji-sagar-america-wale-kirtan',
    'https://soundcloud.com/gs-ss/bhinni-rainarhiye-bhai-mohinder-singh-ji-hazoor-sahib',
    'https://soundcloud.com/akjdotorg/akj-42-01-bhai-mohinder-singh',
    'https://soundcloud.com/nirbaankeertan/bhai-mohinder-singh-hazoor-sahib-44-tu-nijpat-hai',
    'https://soundcloud.com/gs-ss/mati-ko-putra-bhai-mohinder-singh-ji-hazoor-sahib'
]
# downloadLinks(dirr,links)
link='https://soundcloud.com/harsimransinghlalli/bhai-mohinder-singh-sdo-aree-bayee-gobind-naam-mat-beesrai',
downloadLink(dirr,link)
