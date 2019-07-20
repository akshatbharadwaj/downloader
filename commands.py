import requests
import os
from bs4 import BeautifulSoup
import urllib.request

def get_list(website_name):
	site = urllib.request.urlopen(website_name).read()
	site_soup = BeautifulSoup(site)
	print(site_soup.find_all('a'))

def god():
	print("Don't exist")