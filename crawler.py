# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
# print soup

for a in soup.find_all('a', href=True):
    print "Found the URL:", a['href']

 # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below