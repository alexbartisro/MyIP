from pastebin import PastebinAPI
from xml.etree import ElementTree
from datetime import datetime
import requests, time

myDevKey = '#insert dev key here http://pastebin.com/api'
pasteName = 'paste name'

def requester():
        f = requests.request('GET', 'http://myip.dnsomatic.com')
        return f.text

def parseXML(response):
        root = ElementTree.fromstring('<list>' + response + '</list>')
        result = root.findall(".//paste[paste_title='currentIp']/paste_key")
        if len(result) is not 0:
                return result[0].text
        else:
                return None

if __name__ == "__main__":
        while 1:
                myUserKey = PastebinAPI().generate_user_key(myDevKey, 'pastebin username', 'pastebin password')
                oldPasteKey = parseXML(PastebinAPI().pastes_by_user(myDevKey, myUserKey))
                try:
                        PastebinAPI().delete_paste(myDevKey, myUserKey, oldPasteKey)
                except Exception, e:
                        print "Nothing to delete"

                ipString = datetime.now().strftime('%m/%d/%Y - %H:%M:%S') + '\n' + requester()
                try:
                        PastebinAPI().paste(myDevKey, ipString, api_user_key = myUserKey, paste_name = pasteName, paste_format = None, paste_private = None, paste_expire_date = None)
                except Exception, e:
                        print e
                time.sleep(5400)