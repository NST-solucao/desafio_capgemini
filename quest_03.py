palavra = input('Digite uma palavra : ')

anagramas = sorted(palavra)
t = len(anagramas)
count = 0
contnum = 0

for i in palavra:
    if anagramas[count-1] == anagramas[count]: 
        # print(f'A lista de todos os anagramas com 1 letra é:[{anagramas[count-1]} , {anagramas[count]}] que estão nas posições : ')
        contnum += 1
    if sorted(palavra[count:count+2]) == sorted(palavra[count+1:count+3]):
        # print(f'A lista de todos os anagramas com 2 letras são: [{palavra[count:count+2]},{palavra[count+1:count+3]}] que estão nas posições : ')
        contnum += 1
    if sorted(palavra[count:count+3]) == sorted(palavra[count+1:count+4]):
        # print(f'A lista de todos os anagramas com 3 letras são: [{palavra[count:count+3]},{palavra[count+1:count+4]}] que estão nas posições :')
        contnum += 1
    count += 1

print(f'Foi encontrado {contnum} pares de anagramas na palavra {palavra} ')
