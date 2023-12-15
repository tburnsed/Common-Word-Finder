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
    menu = input(print("""
|_______________________________________                                      
|\    / _  ._ _|    _  _   _. ._ _ |_  | 
| \/\/ (_) | (_|   _> (/_ (_| | (_ | | |
---------------------------------------|                                      
            Use tool to 
            - search 1 or more webistes for the most common word 
            - search 1 or more sites for keywords
            Edit the list through the tool or edit the files directly           
            ======================================================
            1. ADD - 1 or more websites to list
            2. PRINT -  Website list           
            3. WIPE -  website list
            -------------------------           
            4. ADD - Keywords to find
            5. PRINT - Keywords to find
            6. WIPE - Key words to find
            --------------------------           
            7. Run the Tool with Keywords
            8. Run the took for every word
            --------------------------           
            10. Exit """))
    if menu == "1":
      addsite_function()
    elif menu == "2":
      printlist_function()
    elif menu == "3":
      wipelist_function()
    elif menu == "4":
      addkeyword_function()
    elif menu == "5":
      printkeywords_function()
    elif menu == "6":
      wipekeywords_function()
    elif menu == "7":
      Findkeywords_function()
    elif menu == "8":
      Findallwords_function()
    elif menu == "9":
       zzzzzzzzzzz()
    elif menu == "10":
      quit()
    else:
      print("Not a Valid Choice")
      menu_function()
    

def addsite_function():
    spaceing_function("Enter URL and press enter for each URL \nPut in full URL \nExample: https://google.com \nWhen Done type EXIT ")
    site = input("Enter URL:")
    if site != "EXIT":
        with open("urls.txt", "a") as urlfile:
            urlfile.write(site)
            urlfile.write('\n')
        print("added")
        addsite_function()
    elif site == "":
        addsite_function()
    else:
        menu_function()
    
    
    
def printlist_function():
    with open("urls.txt", "r") as urlfile:
        sites = urlfile.read()       
        if not sites:
           spaceing_function("List Is Empty!!")
        else:
           print(sites)
    menu_function()

def wipelist_function():
    spaceing_function("Confirm That you want to delete list")
    confirm = input("Wipe List? Y/N").upper()
    if confirm == "Y":
        with open("urls.txt", "r+") as urlfile:
            urlfile.truncate(0)
            spaceing_function("deleted")
    elif confirm == "N":
        menu_function()
    else:
       wipelist_function()
    menu_function()

def addkeyword_function():
    keyword = input("Enter a keyword")
    with open("keywords.txt", "a") as keywords:
        keywords.write('\n')
        keywords.write(keyword)
    spaceing_function("Added List")
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
    
def Findallwords_function():
    #import as list
    websites = open("urls.txt", "r").read()
    websitelist = websites.split("\n") 
    #Loop through to display sites that are being indexed
    spaceing_function("Searching These sites....")
    for url in websitelist:
       print(url)
    #after coverted to List go through each and count
    for url in websitelist:
       #search sites in loop catch error for websites that wont connect
       try:
            err1 = 0
            site = requests.get(url)
            soup = BeautifulSoup(site.content, "html.parser")
            [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
       except:
            err1 = 1
       #if error is found prints out what website it could not connect to
       if err1 == 1:
          print("error connecting to " + url)
       else:
          pass
       #find all text 
       words = soup.findAll(text=True)
       #counts for all text found in "words"
       a = Counter([x.lower() for y in words for x in y.split()])
       #store the counts in this variable
       #need to find out how to reset this after dispalying data
       cnt.update(a.most_common(50))
    findings_function()
    menu_function()
    
def Findkeywords_function():
    #import as list
    websites = open("urls.txt", "r").read()
    websitelist = websites.split("\n") 
    #Loop through to display sites that are being indexed
    print("Searching These sites....")
    for url in websitelist:
       print(url)
    #import as list
    keywords = open("keywords.txt", "r").read()
    keywordlist = keywords.split("\n") 
    #Loop through to display sites that are being indexed
    print("Searching for these keywords....")
    for word in keywordlist:
       print(word)
    #after coverted to List go through each and count
    for url in websitelist:

       #search sites

       site = requests.get(url)
       soup = BeautifulSoup(site.content,"html.parser")
       #remove trash data
       [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
       #find all text 
       words = soup.findAll(text=True)
       #Find values in common and print them
       print(words)
       matches = list(set(keywords) & set(words))
       spaceing_function("I found the following Matches.....")
       for match in matches:
        print(match)
 #   findings_function()
    menu_function()
    
def findings_function():
   #displays the data
   makeaframe = pd.DataFrame(cnt.most_common(50))
   makeaframe.columns = ['Words and count', 'How many sites found on']
   print(makeaframe)
   #sets everthing back to 0
   cnt.update(Counter({'y': 0, 'x': 0}))
   
def spaceing_function(message):
      print("")  
      print("=================")
      print(message)
      print("=================")
      print("")
    

menu_function()