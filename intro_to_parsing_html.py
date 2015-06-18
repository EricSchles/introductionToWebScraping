#to install pip, download the following script: https://bootstrap.pypa.io/get-pip.py
#run: sudo python get-pip.py
#to install type sudo pip install requests

#Project: How connected is the web today?  Write a script that traverses a number of web pages and counts the number of links per page.  How many links go back to the hosts url?  How many go to other websites?
#Questions you can answer: How connected is google to the rest of the internet?  However connected is techmeme.com?  How connected is github.com?  How connected is tech crunch?  How connected is hacker news? How connected is pando daily?  How connected is the new york times?  How connected is the wall street journal?

#how to go about doing this:  Count the number of links on each website.  Try to traverse as many pages of the website as you can.  How many links go to the website?  How many go else where?  Give counts and visualize each.

import requests
import unidecode
from bs4 import BeautifulSoup
#downloading html:
base_url = "https://www.google.com"
response = requests.get(base_url)
soup = BeautifulSoup(response.text)

#a simple crawler
print "showing you all the links.."
for i in soup.find_all("a"):
    if "http" in i["href"]:
        print i["href"]
    else:
        print base_url+i["href"]

print "traversing all the links.."
links = []
for i in soup.find_all("a"):
    if "http" in i["href"]:
        links.append(i["href"])
    else:
        links.append(base_url+i["href"])

        
for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    for i in soup.find_all("a"):
        print unidecode.unidecode(i.getText())
