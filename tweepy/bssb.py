from bs4 import BeautifulSoup

text = '''
<td><a href="http://www.irit.fr/SC">Signal et Communication</a>
<br/><a href="http://www.irit.fr/IRT">Ingénierie Réseaux et Télécommunications</a>
</td>
'''
soup = BeautifulSoup(text)

print(soup.get_text())