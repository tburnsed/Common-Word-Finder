#imports
from gettext import find
import requests
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
import numpy as np

#variables 
cnt = Counter()

 


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
      Findkeywords_function()
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
    #import as list
    websites = open("urls.txt", "r").read()
    websitelist = websites.split("\n") 
    print(websitelist)
    #after coverted to List go through each and count
    for url in websitelist:
       print(url)
       #search sites
       site = requests.get(url)
       soup = BeautifulSoup(site.content, "html.parser")
       #remove trash data
       [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title', "@", "html"])]
       #find all text 
       words = soup.findAll(text=True)
       #start a cound for all text found in "words"
       a = Counter([x.lower() for y in words for x in y.split()])
       #store the counts in this variable
       #need to find out how to reset this after dispalying data
       cnt.update(a.most_common(50))
    findings_function()
    menu_function()
  
def findings_function():
   #displays the data
   makeaframe = pd.DataFrame(cnt.most_common(50))
   makeaframe.columns = ['Words', 'Frequency']
   print(makeaframe)
   #sets everthing back to 0
   a = 0

  

 #   with open('urls.txt') as urls:
 #      url = urls.txt.read().splitlines()
 #   soup = BeautifulSoup(url.content)
 #   [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
 #   texts = soup.findAll(text=True)
 #   exclusion_list = 'up 3 5 7 9'.split()
 #   a = Counter([x.lower() for y in texts for x in y.split()])
 #   cnt.update(a.most_common(50))

menu_function()