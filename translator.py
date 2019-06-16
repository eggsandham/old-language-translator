import pickle
from trans import Translator
lang = Translator()

f_name = input("File? ")
with open(f_name,'rb') as f:
    lang = pickle.load(f)

wtow = input('a to b (1) or b to a (2)? ') 
while True:
    inp = input('>>> ')
    if wtow == '1':
        inp = inp.split(' ')
        out = ''
        for word in inp:
            if word in lang.atob.keys():
                out = out + lang.atob[word]+' '
            else:
                out = out + '"'+word+'"'+' '

    else:
        inp = inp.split(' ')
        out = ''
        for word in inp:
            if word in lang.btoa.keys():
                out = out + lang.btoa[word]+' '
            else:
                out = out + '"'+word+'"'+' '
    
    print(out)
