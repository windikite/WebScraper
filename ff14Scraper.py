import requests
from bs4 import BeautifulSoup
import json
from PIL import Image
import os.path

# empty array
gearList = []

def getGearlists(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    weaponDivs = soup.find_all('div', id="sys_shop_currency_no_0")
    armorDivs = soup.find_all('div', id="sys_shop_currency_no_1")
    accessoryDivs = soup.find_all('div', id="sys_shop_currency_no_2")
    def scrapeDivs(divs):
        for div in divs:
            table = div.find('table')
            tbody = table.find('tbody')
            rows = tbody.find_all('tr')
            for row in rows:
                tds = row.find_all('td')
                names = []
                costs = []
                gear = []
                materials = []
                images = []
                for td in tds:
                    uls = td.find_all('ul')
                    for ul in uls:
                        lis = ul.find_all('li')
                        for li in lis:
                            divs = li.find_all('div')
                            for div in divs:
                                h4s = div.find_all('h4')
                                spans = div.find_all('span')
                                imgs = div.find_all('img')
                                for img in imgs:
                                    url = img['src']
                                    images.append(url)
                                    id_last_slash = url.rindex('/')
                                    first_cut = url[id_last_slash+1:-1]
                                    id_dot = first_cut.index('.')
                                    img_ID = first_cut[0:id_dot]
                                    img_name = img_ID+'.png'
                                    img_path = './ff14assets/' + img_name
                                    file_check = os.path.isfile(img_path)
                                    if file_check == False:
                                        img = Image.open(requests.get(url, stream = True).raw)
                                        img.save(img_path)
                                        print('downloaded', img_name)
                                    elif file_check == True:
                                        print('skipped', img_name)
                                for h4 in h4s:
                                    if(h4.text):
                                        names.append(h4.text)
                                    else:
                                        a = h4.find('a')
                                        names.append(a.text)
                                for span in spans:
                                    costs.append(int(span.text))

                if(len(names) == 2):
                    gear.append([names[0], images[0], costs[0]])
                    materials.append([names[1], images[1], costs[1]])
                elif(len(names) == 3):
                    gear.append([names[0], images[0], costs[0]])
                    materials.append([names[1], images[1], costs[1]])
                    materials.append([names[2], images[2], costs[2]])
                elif(len(names) == 5):
                    gear.append([names[0], images[0], costs[0]])
                    gear.append([names[1], images[1], costs[1]])
                    materials.append([names[2], images[2], costs[2]])
                    materials.append([names[3], images[3], costs[3]])
                    materials.append([names[4], images[4], costs[4]])
                item = {
                    "name": gear,
                    "materials": materials
                }
                if(len(names) > 0):
                    gearList.append(item)
    scrapeDivs(weaponDivs)
    scrapeDivs(armorDivs)
    scrapeDivs(accessoryDivs)

getGearlists("https://na.finalfantasyxiv.com/lodestone/playguide/db/shop/d649f9d035b/")
getGearlists("https://na.finalfantasyxiv.com/lodestone/playguide/db/shop/36748686d6a/")
getGearlists("https://na.finalfantasyxiv.com/lodestone/playguide/db/shop/cd5d8791533/")

print('done!', len(gearList), 'items scraped and convered to json')
    
with open("ff14gear.json", "w") as f:
    json.dump(gearList, f, indent=4)
    
