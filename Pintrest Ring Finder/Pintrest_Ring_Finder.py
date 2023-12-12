#imports
from gettext import find
import requests
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
import numpy as np

#variables 
cnt = Counter()

def GetData(url):
 Website1 = requests.get(url)
 soup = BeautifulSoup(Website1.content)
 [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
 #visible_text = soup.getText()
 texts = soup.findAll(text=True)

 exclusion_list = 'up 3 5 7 9'.split()
 
 a = Counter([x.lower() for y in texts for x in y.split()])
 cnt.update(a.most_common(50))
 


#menu


def menu_function():
    menu = input(print("""What would you Like to do? 
            1. Add 1 or more websites to list
            2. Print Website list
            3. Wipe website list
            4. Add Key words to find
            5. Print Key words to find
            6. wipe Key words to find
            7. Print Websites
            8. Run the Tool with Keywords
            9. Run the took for every word
            10. Exit """))
    if menu == "1":
      print("running 1")
      addsite_function()
    elif menu == "2":
      print("Runing 2")
      printlist_function()
    elif menu == "3":
      print("Runing 3")
      wipelist_function()
    elif menu == "4":
      print("Runing 4")
      addkeyword_function()
    elif menu == "5":
      print("Runing 5")
    elif menu == "6":
      print("Runing 6")
    else:
      print("Not a Valid Choice")
      menu_function()

def addsite_function():
    site = input("Enter URL")
    with open("urls.txt", "a") as urlfile:
        urlfile.write('\n')
        urlfile.write(site)
    print("added")
    menu_function()
    
def printlist_function():
    with open("urls.txt", "r") as urlfile:
        sites = urlfile.read()
        print(sites)
    menu_function()

def wipelist_function():
    with open("urls.txt", "r+") as urlfile:
        urlfile.truncate(0)
    menu_function()

def addkeyword_function():
    keyword = input("Enter a keyword")
    with open("keywords.txt", "a") as keywords:
        keywords.write('\n')
        keywords.write(keyword)
    print("added")
    menu_function()

'''
 

websites = [
             'https://www.pinterest.com/pin/495888608981206761/?mt=login',
             'https://www.pinterest.com/pin/495888608981201114/',
             'https://www.pinterest.com/pin/495888608981047497/',
             'https://www.pinterest.com/pin/495888608981047433/',
             'https://www.pinterest.com/pin/495888608981045976/',
             'https://www.pinterest.com/pin/495888608980613712/',
             'https://www.pinterest.com/pin/495888608980569223/',
             'https://www.pinterest.com/pin/495888608980569227/',
             'https://www.pinterest.com/pin/495888608980569170/',
             'https://www.pinterest.com/pin/495888608980540049/',
             'https://www.pinterest.com/pin/pear-shaped-morganite-engagement-ring-set-rose-gold-art-deco--495888608980519686/',
             'https://www.pinterest.com/pin/495888608980515607/',
             'https://www.pinterest.com/pin/495888608980515490/',
             'https://www.pinterest.com/pin/495888608980470566/',
             'https://www.pinterest.com/pin/495888608980518981/',
             'https://www.pinterest.com/pin/495888608980479765/',
             'https://www.pinterest.com/pin/495888608980470909/',
             'https://www.pinterest.com/pin/495888608980356018/',
             'https://www.pinterest.com/pin/495888608980318779/',
             'https://www.pinterest.com/pin/495888608980313828/',
             'https://www.pinterest.com/pin/495888608980405803/',
             'https://www.pinterest.com/pin/495888608980305845/',
             'https://www.pinterest.com/pin/495888608980312917/',
             'https://www.pinterest.com/pin/495888608980302592/',
             'https://www.pinterest.com/pin/495888608980305816/',
             'https://www.pinterest.com/pin/495888608980304284/',
             'https://www.pinterest.com/pin/495888608980304343/',
             'https://www.pinterest.com/pin/495888608980282281/',
             'https://www.pinterest.com/pin/leandra-mint-sapphire-engagement-ring-with-diamond-clusters-in-2022--495888608980250145/',
             'https://www.pinterest.com/pin/495888608980287295/',
             'https://www.pinterest.com/pin/495888608980282301/',
             'https://www.pinterest.com/pin/495888608980287633/',
             'https://www.pinterest.com/pin/495888608980287637/',
             'https://www.pinterest.com/pin/495888608980296814/',
             'https://www.pinterest.com/pin/495888608980109885/',
             'https://www.pinterest.com/pin/495888608980162996/',
             'https://www.pinterest.com/pin/495888608980224245/',
             'https://www.pinterest.com/pin/495888608977140982/',
             'https://www.pinterest.com/pin/495888608971402561/',
             'https://www.pinterest.com/pin/495888608978395085/',
             'https://www.pinterest.com/pin/495888608978386632/',
             'https://www.pinterest.com/pin/495888608978174676/',
             'https://www.pinterest.com/pin/495888608978070525/',
             'https://www.pinterest.com/pin/495888608978520227/',
             'https://www.pinterest.com/pin/495888608978270190/'
              ]
#print(websites2)
for url in websites:
 GetData(url)

makeaframe = pd.DataFrame(cnt.most_common(50))
makeaframe.columns = ['Words', 'Frequency']
print(makeaframe)
'''

menu_function()