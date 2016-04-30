from datetime import datetime, timedelta
import Cookie

class CookieStorage(object):

	def __init__(self):
		self.cookies = []

	#Check if cookie is stored in server.
	#TODO comprobar que se eliminan correctamente.
	def check_cookie( self, cookie ):
		for c in self.cookies:
			if(c[0]["cookietemp"].value == cookie["cookietemp"].value):
				return True
			else: #Check if cookie is alive
				if( c[1] < datetime.now()):
					self.cookies.remove(c)
		return False

	#Store cookie in server when a correct login is perform.
	def store_cookie( self, cookie ):
		self.cookies.append(( cookie, datetime.now() + timedelta(0, int(cookie['cookietemp']['expires']))))