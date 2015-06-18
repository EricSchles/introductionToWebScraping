#to install pip, download the following script: https://bootstrap.pypa.io/get-pip.py
#run: sudo python get-pip.py
#to install type sudo pip install requests
import requests

#downloading html:
response = requests.get("https://www.google.com")
print response.text

