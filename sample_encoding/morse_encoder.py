morse={'a':'._','b':'_...','c':'_._.','d':'_..','e':'.','f':'.._.','g':'_ _.','h':'.....','i':'..','j':'._ _ _',
'k':'_._','l':'._..','m':'_ _','n':'_.','o':'_ _ _','p':'._ _.','q':'_ _._','r':'._.','s':'...','t':'_',
'u':'.._','v':'..._','w':'._ _','x':'_.._','y':'_._ _','z':'_ _..'}

str="tapan manu"
ls=str.split(' ')
code=[morse[i] for i in str if i in morse.keys()]
print('  '.join(code))
