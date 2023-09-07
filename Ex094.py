dados = dict()
lista_dados = []
tot_idade = 0
tot_pessoas = 0
while True:
    dados['Nome'] = str(input("Seu nome: ")).upper()
    dados['idade'] = int(input("Sua idade: "))
    tot_idade += dados['idade']
    tot_pessoas += 1
    while True:
        dados['Sexo'] = str(input("Seu sexo?\n[M/F]: ")).upper()
        lista_dados.append(dados.copy())
        if dados['Sexo'] in 'MF':
            break
        print('Sexo inválido use apenas [M ou F]!!!')
    while True:
        resp = str(input("Quer continuar?\n[S/N]: "))
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N!. ')
    if resp == 'N':
        break
media = tot_idade / tot_pessoas
print(lista_dados)
print(f'A) O total de pessoa cadastradas é {tot_pessoas}.')
print(f'B) A média total de idade é {media}.')
print(f'C) As mulheres cadastradas foran: ',end='')
for p in lista_dados:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ',end=';')
print()
print(f'D) Lista de pessoa que estão acima da MÉDIA: ')
if dados['idade'] > media:
    for c, k in dados.items():
        print(f'»» {c} = {k}',end='; ')