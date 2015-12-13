# MyIP
Pyton script that get's you public IP and saves it into Pastebin, in casa your DDNS fails

Install:

1. pip install Pastebin

2. Go to http://pastebin.com/api and get you api key

3. Edit myip.py and insert your api key, pastebin username and password

4. Run 'python MyIP.py'


The script will run every 90 minutes, deleting the previous paste and creating a new one, containing the current timestamp
and your public (Internet) IP
