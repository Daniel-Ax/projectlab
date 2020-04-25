from urllib.request import urlopen 

html_data = urlopen('http://www.google.com')
print(html_data.read())