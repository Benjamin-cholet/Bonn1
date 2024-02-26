from fbchat import Client
from fbchat.models import *
import datetime
import logging

# TEST group ID : 4368034386542182
# apéro: 3958740187499522

email = os.environ.get("FB_EMAIL")
password = os.environ.get("FB_PASSWORD")

client = Client(email, password, logging_level=logging.DEBUG)

print("Own id: {}".format(client.uid))
#print(client.getSession())
'''
users = client.searchForGroups("C'est l'heure de l'apero")
user = users[0]
print("User's ID: {}".format(user.uid))
print("User's name: {}".format(user.name))
'''

client.send(Message(text=f"{datetime.datetime.now()} - pas de résultat"), thread_id=4368034386542182, thread_type=ThreadType.GROUP)
