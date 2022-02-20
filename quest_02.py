min_caracter = 6          # minimo 6 caracteres 
min_dig = 0               # minimo 1 digito numeral
min_letra_minuscula = 0   # minimo 1 letra minuscula
min_letra_maiuscula = 0   # minimo 1 maiuscula
min_caracter_especial = 0 # minimo 1 caracter especial

senha = input('Digite senha :')

if len(senha) >= min_caracter:
    for i in senha:
        if i.islower():
            min_letra_minuscula += 1
        if i.isupper():
            min_letra_maiuscula += 1
        if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*' or i == '(' or i == ')' or i == '-' or i == '+':
            min_caracter_especial += 1
        if i.isdigit():
            min_dig += 1
    if min_dig >= 1 and min_letra_maiuscula >= 1 and min_letra_minuscula >= 1 and min_caracter_especial >= 1:
        print('Senha valida')
    else:
        if min_dig == 0:
            print('Faltou 1 numero ')
        if min_letra_minuscula == 0:
            print('Faltou 1 letra minuscula ')
        if min_letra_maiuscula == 0:
            print('Faltou 1 letra maiuscula ')
        if min_caracter_especial == 0:
            print('Faltou caracter especial ')
else:
    print('Senha precisa ter minimo 6 caracteres ... ')
