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

#Setting up SMTP
import smtplib
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("d.degregorio95@gmail.com", "pyvmoz-qudmA1-taggem")

#Sending an Email
smtpObj.sendmail("d.degregorio95@gmail.com", "d.degregorio95@gmail.com", "Subject: Number of available seats in the desired course. /nHello!\nYou wanna know the exact number of available seats in your desired course? Not a problem. There are still {} seats left. \nYours sincerely,\nDaniele".format(int(makerspace_elems[1].getText())))

#Disconnect program from the SMTP server
smtpObj.quit()
