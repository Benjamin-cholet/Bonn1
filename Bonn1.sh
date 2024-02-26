#!/bin/bash

while true
do

md5 <<< $(curl -s "http://publinetce2.education.fr/publinet/Servlet/PublinetServlet?_page=LISTE_RES&_concours=EAE&_section=7603&_acad=FRANCE&_type=ADMISSION") | grep -v 597b6be

if [ $? -eq 0 ]
then
echo "launching scenario2 !!!"
python scenario2.py


curl -s "http://publinetce2.education.fr/publinet/Servlet/PublinetServlet?_page=LISTE_RES&_concours=EAE&_section=7603&_acad=FRANCE&_type=ADMISSION&_lettre=b" | grep -i BONNIN
if [ $? -eq 0 ]
then
	echo "YESSSSS"
	python scenario3.py
	python scenario4.py
	exit 0
else
	echo "snif"
	exit 0
fi

fi

sleep 10

minutes=$(date +%M)
if [ $minutes -eq 00 ]
then
	echo "launching scenario1"
	python scenario1.py
	sleep 60
fi

echo "..."
done
