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

text = """**scenario 2**
DING DING DING
LES resultats d'admission à l'agreg d'espagnol sont disponibles a l'adresse suivante:
http://publinetce2.education.fr/publinet/Servlet/PublinetServlet?_page=LISTE_RES&_concours=EAE&_section=7603&_acad=FRANCE&_type=ADMISSION
(enfin je crois, le md5 de la page à changé et n'est plus 597b6be)
"""


client.send(Message(text=text), thread_id=3958740187499522, thread_type=ThreadType.GROUP)
client.send(Message(text=text), thread_id=4368034386542182, thread_type=ThreadType.GROUP)
