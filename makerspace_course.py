#! python3 
# makerspace_course.py

import requests	# importing requests module for downloading HTML files
import bs4	# importing BeautifulSoup module for parsing downloaded HTML files

# Downloads HTML file from url.
res = requests.get("https://www.maker-space.de/course/cnc-fraesen-mit-der-haas-vf-2-fuer-einsteiger.html")
# Raises an exception if there was an error downloading the file and will do nothing if the download succeeded.
res.raise_for_status()
# Creating BeautifulSoup object
makerspace = bs4.BeautifulSoup(res.text, features="lxml")
# Once you have a BeautifulSoub object, you can use its methods to locate specific parts of an HTML document.

makerspace_elems = makerspace.findAll("div", {"class": "TerminCol TerminColPlaces"})
print(makerspace_elems[0].getText(), makerspace_elems[1].getText())
