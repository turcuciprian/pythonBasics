from urllib.request import urlopen
# //connecting to a site
connection = urlopen('http://ciprianturcu.com')
# reading the contents of the site
content = connection.read()
# printing the read content
print(content)