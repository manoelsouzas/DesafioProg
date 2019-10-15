letras =[]
letra = str(input('insira a letra desejada'))

for i in range(ord('a'), ord(letra)+1):
    letras.append(chr(i))
for g in range (0, len(letras)):
        if g == 0: 
            print(' ' * (int(len(letras))) + letras[g]) 
        else:
            print(' ' * (len(letras)-g) + letras[g] + ' ' * ((g*2)-1) + letras[g])
letrasContrario = list(reversed(letras))
for g in range (len(letras)-1, 0, -1):
        if g == 1: 
            print(' ' * (int(len(letras))) + letrasContrario[g*-1]) 
        else:
            print(' ' * ((len(letras)-g)+1) + letrasContrario[g*-1] + ' ' * ((g*2)-3) + letrasContrario[g*-1])