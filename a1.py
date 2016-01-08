#use of python2.7 done as I'm familiar with the use of beautiful soup and urllib in python2.7
#there are changes that have taken place with which I'm not totally familiar with and hence use of python2.7
#You'd also require an active internet connection to execute the same
#The results are not very tidy and cleaned up 

import re
import urllib
import urllib2
import json
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def process(string):
	text =set(nltk.wordpunct_tokenize(string))
	common_text =set(stopwords.words('english1')) #Self created list of stopwords
	key_term =text-common_text
	search_for = " ".join(map(str,list(key_term)))
	return search_for

def think(find):
	query =urllib.urlencode({'q':find})
	url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s"%query
	search_response =urllib2.urlopen(url).read()
	result =json.loads(search_response)
	data =result['responseData']['results'][0]
	soup =BeautifulSoup(data['content'])
	print("ChatBot:")
	print(soup.get_text())
	print("In case you wish to know more about it, you can go to the following link: %s" %data['url'])

while(True):
	print("User:")
	input_str =raw_input()
	find=process(input_str)
	think(find)