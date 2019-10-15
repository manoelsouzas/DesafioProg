tabuleiro = [[0,0,0,0,3,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,2,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
peao = 0
bispo = 0
cavalo = 0
torre = 0
rainha = 0
rei = 0
for i in range (0,8):
    peao = peao + tabuleiro[i].count(1)
    bispo = bispo + tabuleiro[i].count(2)
    cavalo = cavalo + tabuleiro[i].count(3)
    torre = torre + tabuleiro[i].count(4)
    rainha = rainha + tabuleiro[i].count(5)
    rei = rei + tabuleiro[i].count(6)

print ('Peão: {} peças'.format(peao))
print ('Bispo: {} peças'.format(bispo))
print ('Cavalo: {} peças'.format(cavalo))
print ('Torre: {} peças'.format(torre))
print ('Rainha: {} peças'.format(rainha))
print ('Rei: {} peças'.format(rei))
