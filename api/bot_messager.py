from flask import Flask
from pywebio.platform.flask import webio_view 


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
			while True:
				msg = input('Message to send (Type "stop" to change bot/recipient): ')
				if msg == 'stop':
					break
				else:
					bot.send_message(recipientID, msg)
	#call the home function here
	home()

#set the url rule
app.add_url_rule('/', 'webio_view', webio_view(main),methods=['GET','POST'])

if __name__ == "__main__":
	  app.run(debug=False)