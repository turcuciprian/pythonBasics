from urllib.request import urlopen

connection = urlopen('http://ciprianturcu.com')
content = connection.read()
print(content)