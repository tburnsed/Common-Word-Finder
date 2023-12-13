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

 


#menu


def menu_function():
    menu = input(print("""What would you Like to do? 
            1. Add 1 or more websites to list
            2. Print Website list
            3. Wipe website list
            4. Add Key words to find
            5. Print Key words to find
            6. wipe Key words to find
            7. Run the Tool with Keywords
            8. Run the took for every word
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
      printkeywords_function()
    elif menu == "6":
      print("Runing 6")
      wipekeywords_function()
    elif menu == "7":
      print("Runing 7")
    elif menu == "8":
      print("Runing 8")
    elif menu == "9":
      print("Runing 9")
    elif menu == "10":
      quit()
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
    
def printkeywords_function():
     with open("keywords.txt", "r") as keywords:
        keywords = keywords.read()
        print(keywords)
     menu_function()

def wipekeywords_function():
    with open("keywords.txt", "r+") as keywords:
        keywords.truncate(0)
    menu_function()
    
def Findkeywords_function():
 Website1 = requests.get(url)
 soup = BeautifulSoup(Website1.content)
 [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
 #visible_text = soup.getText()
 texts = soup.findAll(text=True)

 exclusion_list = 'up 3 5 7 9'.split()
 
 a = Counter([x.lower() for y in texts for x in y.split()])
 cnt.update(a.most_common(50))

'''
 
#print(websites2)
for url in websites:
 GetData(url)

makeaframe = pd.DataFrame(cnt.most_common(50))
makeaframe.columns = ['Words', 'Frequency']
print(makeaframe)
'''

menu_function()