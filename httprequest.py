from urllib.request import urlopen

connection = urlopen('http://ciprianturcu.com')
print(connection.read())