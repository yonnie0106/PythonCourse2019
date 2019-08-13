# https://polisci.wustl.edu/people/88/

from bs4 import BeautifulSoup
import urllib.request
import random
import time
import os

## Open a web page
web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)

## Parse it
soup = BeautifulSoup(web_page.read())
soup.prettify()

## Find all cases of a certain tag
## Returns a list... remember this!
name = soup.find_all('h3')
name_list = [i.text for i in name]
name_list = name_list[1: len(name_list) -3]

title  = soup.find_all('div', {"class": "dept"})
title_list = [i.text for i in title]


link = soup.find_all('a', {"class": "card"})
link_list = []
for i in range(len(link)):
	link_list.append(link[i]['href'])

full_list = []
for i in range(len(link_list)):
	full_list.append('https://polisci.wustl.edu' + link_list[i])


url = []
html = []
for i in range(len(full_list)) :
	url.append(full_list[i])
	try :
		html.append(urllib.request.urlopen(url[i]))
		print("Succeed")
	except urllib.error.URLError:
		print(f"URL Error")
		pass



h = html[1]
h.find_all('a')



import csv

with open('faculty.csv', 'w') as f:
	writer = csv.DictWriter(f, fieldnames = ("Name", "Title"))
	writer.writeheader()
	for i in range(len(name_list)):
		writer.writerow({"Name":name_list[i], "Title":title_list[i]})
