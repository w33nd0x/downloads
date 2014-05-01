#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup

website = raw_input("Enter website(fully including \"http://\": ")
html = urllib.urlopen(website)

bt = BeautifulSoup(html.read(), 'lxml')

allLinks = bt.find_all('a')

print "\n\n\tEXTRACTED FOLLOWING LINKS: \n\n\t"
for link in allLinks:
	print link['href']

allMetaTags = bt.find_all('meta')

print "\n\n\tEXTRACTED FOLLOWING METATAGS: \n\n\t"
for tag in allMetaTags:
	print tag


print "\n\n\tWEBSITE PARSING COMPLETE!!\n\n"














