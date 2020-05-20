from googletrans import Translator

trans=Translator()
t=trans.translate(
    'Bom dia',src='pt', dest='hu'
)
print(f'Source:{t.src}')
print(f'Destination:{t.dest}')
print(f'{t.origin} -> {t.text}')