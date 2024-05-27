from datetime import date

ano = int(input('Digite um ano => 0 - para o ano atual:  '))

if(ano==0):
    ano = date.today().year

isBissexto = (ano%4 == 0 and ano%100 != 0) or (ano%100 == 0 and ano%400 == 0)

print('{}{} e um ano bissexto'.format(ano,'' if isBissexto else ' nao'))