from fbchat import Client
from fbchat.models import *
import datetime

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

text = """**scenario 3**
PUTAIN AGATHE T'ES TROP UNE BGGGGGGGGGGGG !!!!!!!!!!!!
(DISCLAIMER: BOBO n'a pas mangé depuis longtemps et s'est peut être trompé)
"""


client.send(Message(text=text), thread_id=3958740187499522, thread_type=ThreadType.GROUP)
client.send(Message(text=text), thread_id=4368034386542182, thread_type=ThreadType.GROUP)
