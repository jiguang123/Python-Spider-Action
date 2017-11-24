 # -*- coding: utf-8 -*-
"""
Created on 2017-11-23
@author: jiguang123
"""

import requests
from bs4 import BeautifulSoup


def requests_html(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}	
	html = requests.get(url, headers=headers)
	return html.text

if __name__ == '__main__':
#	headers = {'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
	start_url = 'https://movie.douban.com/chart'
	html_doc = requests_html(start_url)
	soup = BeautifulSoup(html_doc, "html.parser")
	target1s = soup.find_all("div", class_="pl2")

	movies = []
	movie_urls = []
	for each in target1s:
		movies.append(each.a.text.split()[0])
		movie_urls.append(each.a['href'])
	target2s = soup.find_all("span", class_="rating_nums")
	
	ranks = []
	for each in target2s:
		ranks.append(each.text)		
	for i  in range(len(movies)):
		print(movies[i],ranks[i], movie_urls[i])	