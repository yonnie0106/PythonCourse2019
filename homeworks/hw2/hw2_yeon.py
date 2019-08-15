from bs4 import BeautifulSoup
import urllib.request
import random
import time
import os
import csv



with open('hw2_yeon.csv', 'w', encoding='utf-8') as f:
	w = csv.DictWriter(f, fieldnames = ("Title", "Date", "Issues", "Number_of_signitures"))
	w.writeheader()
	url = 'https://petitions.whitehouse.gov/petitions'
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html.read())
	petition={}
	tags = soup.select('h3 > a')
	for tag in tags:
		try:
			petition_page = urllib.request.urlopen('https://petitions.whitehouse.gov' + tag.get('href'))
		except:
			print(Error)
			continue
		petition_html = BeautifulSoup(petition_page.read())
		petition["Title"] = petition_html.find('h1').get_text()
		petition["Date"] = petition_html.find('h4').get_text()
		petition["Issues"] = ', '.join(map(str, [i.text for i in petition_html.find('div', {'class' : 'content'}).find_all('h6')]))
		petition["Number_of_signitures"] = petition_html.find('span', {'class' : 'signatures-number'}).get_text()
		w.writerow(petition)

	for i in range(1, 5):
		try:
			more_html = urllib.request.urlopen('https://petitions.whitehouse.gov/?page=' + str(i))
			more_soup = BeautifulSoup(more_html.read())
		except:
			print(Error)
		more_tags = more_soup.select('h3 > a')
		for tag in more_tags: 
			try: 
				more_petition_page = urllib.request.urlopen('https://petitions.whitehouse.gov' + tag.get('href'))
				print
			except:
				print(Error)
				continue
			more_petition_html = BeautifulSoup(more_petition_page.read())
			petition["Title"] = more_petition_html.find('h1').get_text()
			petition["Date"] = more_petition_html.find('h4').get_text()
			petition["Issues"] = ', '.join(map(str, [i.text for i in more_petition_html.find('div', {'class' : 'content'}).find_all('h6')]))
			petition["Number_of_signitures"] = more_petition_html.find('span', {'class' : 'signatures-number'}).get_text()
			w.writerow(petition)

