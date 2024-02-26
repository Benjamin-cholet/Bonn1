#!/bin/bash

while true
do

curl -ks "http://publinetce2.education.fr/publinet/Servlet/PublinetServlet?_page=DERN_RES&_type=ADMISSIBILITE" | grep -i ESP

if [ $? -eq 0 ]
then

while true
do
tput bel
afplay /System/Library/Sounds/Ping.aiff
#say beep
done

else
echo "..."
fi

md5 <<< $(curl -s "http://publinetce2.education.fr/publinet/Servlet/PublinetServlet?_page=LISTE_RES&_concours=EAE&_section=7603&_acad=FRANCE&_type=ADMISSIBILITE") | grep -v 9356

if [ $? -eq 0 ]
then

while true
do
tput bel
afplay /System/Library/Sounds/Ping.aiff
#say beep
done


fi

sleep 10

done
