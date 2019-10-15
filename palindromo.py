numeroinicial = int(input("insira o primeiro número:"))
numerofinal = int(input("insira o primeiro número:"))
palindromos = []
for numerotestado in range(numeroinicial, numerofinal):
    if str(numerotestado) == str(numerotestado)[::-1]:
        palindromos.append(str(numerotestado))
print('São Palindromos: {}'.format(', '.join(palindromos)))