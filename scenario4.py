from fbchat import Client
from fbchat.models import *
import datetime
import time
import os

# TEST group ID : 4368034386542182
# apéro: 3958740187499522

email = os.environ.get("FB_EMAIL")
password = os.environ.get("FB_PASSWORD")

client = Client(email, password)

#print("Own id: {}".format(client.uid))
'''
users = client.searchForGroups('test')
user = users[0]
print("User's ID: {}".format(user.uid))
print("User's name: {}".format(user.name))
'''

text1 = """♪┏(・o・)┛♪"""
text2 = """♪┗ ( ・o・) ┓♪"""
i = 0
while True:
	client.send(Message(text=text1), thread_id=3958740187499522, thread_type=ThreadType.GROUP)
	client.send(Message(text=text1), thread_id=4368034386542182, thread_type=ThreadType.GROUP)
	time.sleep(10)
	client.send(Message(text=text2), thread_id=3958740187499522, thread_type=ThreadType.GROUP)
	client.send(Message(text=text2), thread_id=4368034386542182, thread_type=ThreadType.GROUP)
	time.sleep(10)
	i=i+1
	if i > 100:
		break