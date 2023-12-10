import pywebio
import telebot


from flask import Flask
from pywebio.platform.flask import webio_view 
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *



app = Flask(__name__)
app.secret_key = "your_secret_key" 


def main():
	def home(): 
		send_message()
	def send_message():
		while True:
			botID = input('Bot ID: ')
			recipientID = input('Recipient ID: ')
			bot = telebot.TeleBot(botID)
			msg = input('Message to send: ')
			bot.send_message(recipientID, msg)
	#call the home function here
	home()

#set the url rule
app.add_url_rule('/', 'webio_view', webio_view(main),methods=['GET','POST'])

if __name__ == "__main__":
	  app.run(debug=False)