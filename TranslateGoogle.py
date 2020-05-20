from googletrans import Translator

f = open('text','r')
mytext=[]

for line in f:
    mytext.append(line.strip())

la=''
for line in mytext:
    print(line)

    trans=Translator()
    t=trans.translate(
         line,src='en', dest='hu'
    )
    print(f'Source:{t.src}')
    print(f'Destination:{t.dest}')
    print(f'{t.origin} -> {t.text}')