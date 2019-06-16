import pickle as pk
from trans import Translator
go = True

old_lang = Translator()
print('''
+++++++++++++++++++++++COMMANDS+++++++++++++++++++++++
Single word input (1)
Auto define(2)
Dump(3)
View(4)
Import(5)
Exit(6)
''')
while go == True:
    comm = str(input('>>> '))
    if comm == '1':
        word = input("Word? ")
        defi = input("deffinition (1 word)? ")
        old_lang.atob[word] = defi
        old_lang.btoa[defi] = word

    elif comm == '2':
        phrase = input('phrase? ')
        deff = input('def (word by word)? ')
        phrase = phrase.split(' ')
        deff = deff.split(' ')
        for i in phrase:
            index = phrase.index(i)
            old_lang.atob[phrase[index]] = deff[index]
            old_lang.btoa[deff[index]] = phrase[index]
    
    elif comm == '3':
        f_name = input('File name? ')
        with open(f_name, 'wb') as f:
            pk.dump(old_lang,f)

    elif comm == '4':
        print(old_lang)

    elif comm == '5':
        f_name = input('File name? ')
        with open(f_name, 'rb') as f:
            old_lang = pk.load(f)
        
    elif comm == '6':
        go = "Clang"
            

    
