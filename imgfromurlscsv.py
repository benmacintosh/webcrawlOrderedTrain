
import csv

#from google_pagerank.page_rank import GetPR

import urllib.parse
import urllib.request

from selenium import webdriver
from PIL import Image
from io import BytesIO


import hmac
import hashlib
import urllib



#IMPORT LINKS
links = []
with open('crawlout.csv', 'r') as csvfile:
    thisreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in thisreader:
        if(row):
            links.append(row)


#CLEAN LINKS
cleanlinks = []
values = {'name' : 'Bens Book'}
for i in range(len(links)):
    nextlink = links[i][0]
    print("cleaning links index",i)
    try:
        req = urllib.request.Request(nextlink)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(nextlink)
            cleanlinks.append(nextlink)
    except (ValueError, urllib.error.HTTPError):
        pass


#RANK BY INVERSE GOOGLE RANK

def lenhttpfetch(link):
    # data = urllib.parse.urlencode(values)
    # data = data.encode('ascii') # data should be bytes
    req = urllib.request.Request(link)#,data
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(len(the_page))
    return(len(the_page))

sortedlinks = sorted(cleanlinks,key = lenhttpfetch)


print(links)
print('hh')
print(sortedlinks)







#FETCH SCREENSHOTS FROM LINKS


DRIVER = 'C:/Users/benma/Downloads/chromedriver'
driver = webdriver.Chrome(DRIVER)
#driver.set_window_size(100,100)
newsquare=512

for i in range(len(sortedlinks)):
    driver.get(sortedlinks[i])
    #driver.save_screenshot(str(i)+'.png')

    png = driver.get_screenshot_as_png()

    #convert to 3 channel, crop and save
    img = Image.open(BytesIO(png))
    thiswidth, thisheight = img.size
    if(thiswidth<thisheight):
        img = img.crop((0,0,thiswidth,thiswidth))
        img = img.resize((newsquare,newsquare))
    else:
        img = img.crop((0,0,thisheight,thisheight))
        img = img.resize((newsquare,newsquare))
    img = img.convert('RGB')
    img.save(str(i)+'.png')

driver.quit()

#make sure correct form out

# depot = DepotManager.get()
# driver = webdriver.PhantomJS()
# driver.set_window_size(1024, 768) # set the window size that you need 
# driver.get('https://github.com')
# driver.save_screenshot('github.png')




 
# def screenshotlayer(access_key, secret_keyword, url, args):
    
#     # encode URL
#     query = urllib.parse.urlencode(dict(url=url, **args))
 
#     # generate md5 secret key
#     urlbytes=url.encode('utf-8')
#     seckeywbytes = secret_keyword.encode('utf-8')
#     secret_key = hashlib.md5('{}{}'.format(urlbytes, seckeywbytes)).hexdigest()
 
#     return "https://api.screenshotlayer.com/api/capture?access_key=%s&secret_key=%s&%s" % (access_key, secret_key, query)
 


# # set your access key, secret keyword and target URL 
# access_key = "0b0c686fabd2a6ca8319645fc8827cad"
# secret_keyword = "Badooka123"

# # set optional parameters (leave blank if unused)
# params = {
#     'fullpage': '',
#     'width': '',
#     'viewport': '512x512',
#     'format': 'PNG',
#     'css_url': '',
#     'delay': '',
#     'ttl': '',
#     'force': '',
#     'placeholder': '',
#     'user_agent': '',
#     'accept_lang': '',
#     'export': ''
# };

# for link in sortedlinks:
#   #save
#   print(link)
#   print(screenshotlayer (access_key, secret_keyword, link, params))