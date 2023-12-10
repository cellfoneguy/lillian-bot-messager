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
			while True:
				msg = input('Message to send (Type "stop" to change bot/recipient): ')
				if msg == 'stop':
					break
				else:
					bot.send_message(recipientID, msg)
	def bmi():
	    height = input("Input your height(cm)：", type=FLOAT)
	    weight = input("Input your weight(kg)：", type=FLOAT)

	    BMI = weight / (height / 100) ** 2

	    top_status = [(16, 'Severely underweight'), (18.5, 'Underweight'),
	                  (25, 'Normal'), (30, 'Overweight'),
	                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]

	    for top, status in top_status:
	        if BMI <= top:
	            put_text('Your BMI: %.1f. Category: %s' % (BMI, status))
	            break
		#call the home function here
	home()

#set the url rule
app.add_url_rule('/', 'webio_view', webio_view(main),methods=['GET','POST'])

if __name__ == "__main__":
	  app.run(debug=False)