import urllib2
from bs4 import BeautifulSoup
import requests
import shutil
import os 

website = raw_input("Enter the site:")
##path = raw_input("Enter path to save files to:")
url = urllib2.urlopen(website).read()
soup = BeautifulSoup(url, "html.parser")
list_of_links = soup.find_all('a')
#for link in list_of_links:
#	if website.endswith('/'):
#		print website + link['href']
#	else:
#		print website + '/' + link['href']
##for link in list_of_links:
##	if website.endswith('/'):
r =  requests.get("https://privatepages.co.uk/PlayBoy/Playboy%20Special%20Collector%e2%80%99s%20Edition%202015%2001%20-%20Wet%20&%20Wild.pdf", stream = True);
##if not os.path.exists(path):
##	os.makedirs(path) 
with open("bac", 'wb') as file:
	for chunk in r.iter_content(1024):
		file.write(chunk)
#	else:
#		print website + '/' + link['href']


