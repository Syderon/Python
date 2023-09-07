
jogador = {}
caixa = []
jogador['Nome'] = str(input("Nome do Jogador: ".upper()))
jogador['Partidas'] = int(input(f"Quantas partidas {jogador['Nome']} jogou?  "))
for k in range(1,jogador['Partidas']+1):
    gol = (int(input(f"Quantos gols na {k}°: ")))
    caixa.append(gol)
    jogador['Total']=sum(caixa)
print('»'*55)
print(jogador)
print('»'*55)

for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']} Partidas!".upper())
print('»'*55)
for p, g in enumerate(caixa):
    print(f'» Na partida {p} fez {g} GOLS! ')