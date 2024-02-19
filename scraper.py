import requests 
# from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://dndtools.net/spells/players-handbook-v35--6/air-walk--2772/"

response = requests.get(url)
baseString = response.text
array = []
i = 0
while i < 900:
    firstTagEnd = baseString.index('>')
    secondTagEnd = baseString.index('<', firstTagEnd)
    if (secondTagEnd == -1 or firstTagEnd == -1):
         i = 10000
    else:
        x = slice(firstTagEnd+1, secondTagEnd-1)
        string = baseString[x]
        y = slice(secondTagEnd, len(baseString)-1)
        baseString = baseString[y]
        if (string != "" and string != ","):
            array.append(string)
        i+=1
        print(i)
    
print(array)

# response = requests.get(url)
# baseString = response.text
# array = []
# i = 0
# while i < 300:
#     firstTagEnd = baseString.index('>')
#     secondTagEnd = baseString.index('<', firstTagEnd)
#     x = slice(firstTagEnd+1, secondTagEnd-1)
#     string = baseString[x]
#     y = slice(secondTagEnd, len(baseString)-1)
#     baseString = baseString[y]
#     if string != "":
#         array.append(string)
#     print(firstTagEnd, secondTagEnd, string)
#     if (secondTagEnd == -1 or firstTagEnd == -1):
#          i = 300
#     else:
#         i+=1
# print(array)

# soup = BeautifulSoup(response.content, 'html.parser').text
# alphabetSoup = soup.split('')

# do = True
# while do == True:
#     firstTagEnd = soup.index('>')
#     secondTagEnd = soup.index('<', firstTagEnd)
#     slice(firstTagEnd+1, secondTagEnd-1)
#     string = soup[slice]
#     print(string)

# spells = []
# rows = soup.select('tr')
# # print(rows)

# for row in rows:
#     tdList = row.find_all('td')
#     if(len(tdList) > 0):
#         spellName = tdList[0].find('a')
#     # print('spell name', spellName)
#     # print('tdList', tdList)
#     # spells.append([spellName])
#     # print(row)
# print(spells)

# df = pd.DataFrame(spells, columns=['Spell Name', 'Spell School', 'Rulebook'])

time.sleep(1)

# df.to_csv('spells.csv', index=False)