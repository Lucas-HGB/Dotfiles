#/usr/bin/env python3

import imaplib
import os


class EmailHandler():

	def __init__(self):
		self.__init_gmail()


	def __init_gmail(self):
		username = "Lucas.hgb2@gmail.com"
		password = "Lucas40215007"
		self.gmail = imaplib.IMAP4_SSL("imap.gmail.com")
		self.gmail.login(username, password)


	def select(self, text):
		return self.gmail.select(text)[1]


	def fetch_email(self, id):
		return self.gmail.fetch(str(id), "(RFC822)")





if __name__ == "__main__":
	h = EmailHandler()
	shopping = h.select("Shopping")
	
	print(h.fetch_email(1))