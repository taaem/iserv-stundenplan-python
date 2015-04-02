from html.parser import HTMLParser
import httplib2
import urllib.parse
f = open('cache', 'w', encoding='latin-1')
url = 'https://ohmoor.de/idesk/'
body = {"login_act": "username", "login_pwd": "password"}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
http = httplib2.Http()
response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))

headers['Cookie'] = response['set-cookie']
url = 'https://ohmoor.de/idesk/plan/index.php/Vertretungsplan/'   
response, content = http.request(url, 'GET', headers=headers)

f.write(content.decode('latin-1'))

f = open('cache', 'r', encoding='latin-1')

liste = []
list = []
info = []
counter = 0
endfile = 0
parseData = 0

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global parseData
        if attrs == [('class', 'mon_title')]:
            parseData = 1
            pass
        pass

    def handle_data(self, data):
        if parseData == 1 and data != '\n':
            liste.append(data)
            pass
        

parser = MyHTMLParser()

for line in f:
    parser.feed(line)
    list.append(liste)
    liste = []
    counter = counter + 1
    pass

for item in list:
    print(item)
    pass

