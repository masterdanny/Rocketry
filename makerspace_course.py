#! python3 
# makerspace_course.py - Checks the number of available places left in a Makerspace course and sends an email to everybody, who is interested in it.
 
# import requests module for downloading HTML files
import requests	
# import BeautifulSoup module for parsing downloaded HTML files
import bs4	
# import SMTP module in order to send emails
import smtplib
import schedule
import time

def makerspace_places(course_website):
	"""Checks and sends the number of available course places"""  
	# Downloads HTML file from url.
	res = requests.get(course_website)
	# Raises an exception if there was an error downloading the file and will do nothing if the download succeeded.
	res.raise_for_status()
	makerspace = bs4.BeautifulSoup(res.text, features="lxml")
	# Once you have a BeautifulSoub object, you can use its methods to locate specific parts of an HTML document.
	show_places = makerspace.findAll("div", {"class": "TerminCol TerminColPlaces"})
	# print(show_places[0].getText(), show_places[1].getText())
	# Connect to an SMTP Server
	smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login("d.degregorio95@gmail.com", "pyvmoz-qudmA1-taggem")
	smtpObj.sendmail("d.degregorio95@gmail.com", "d.degregorio95@gmail.com", "Subject: Number of free slots in the desired course. \nHello!\nYou'd like to know the number of free slots in your Makerspace course of interest? Not a problem. There are still {} slots left. \nYours sincerely,\nDaniele".format(int(show_places[1].getText())))
	smtpObj.quit()


schedule.every().hour.do(makerspace_places, "https://www.maker-space.de/course/cnc-fraesen-mit-der-haas-vf-2-fuer-einsteiger.html")

while True:
	schedule.run_pending()
	time.sleep(1)

