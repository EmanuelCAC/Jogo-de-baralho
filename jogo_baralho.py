from requests import get
from PIL import Image
from matplotlib import pyplot as plt
from pprint import pprint
from random import randint

api_url = "http://deckofcardsapi.com/api/deck/"
api_point = "new/shuffle/?deck_count=1"
baralho = get(f'{api_url}{api_point}')

if baralho.status_code != 200:
  print(f'Erro de acesso (código: {baralho.status_code})')
else:
  baralho = baralho.json()
  id = baralho.get('deck_id', None)

class criar_jogador():
  _mao = []
  _nome = None

  def __init__ (self, nome, mao=[]):
    self._nome = nome
    self._mao = mao

    cartas = get(f'{api_url}{id}/draw/?count=10')
    if cartas.status_code != 200:
      print(f'Erro de acesso (código: {cartas.status_code})')
    else:
      cartas = cartas.json().get('cards', None)
      empilhar = []
      for carta in cartas:
        code = carta.get('code', None)
        empilhar.append(code)
        codigos = ','.join(empilhar)
      self._mao = empilhar

    pilha = get(f'{api_url}{id}/pile/{self._nome}/add/?cards={codigos}')
    if pilha.status_code != 200:
      print(f'Erro de acesso (código: {pilha.status_code})')
    else:
      pilha = pilha.json()
      pprint(pilha)
  
  def nome(self):
    return self._nome

  def mao(self):
    return self._mao

jogador1 = criar_jogador('Emanuel')

jogador2 = criar_jogador('Tiago')

start = randint(1, 2)
r = 1
empate = []
pilha1 = []
pilha2 = []
x = 0

while r <= 10:
  print(f"rodada = {r}°")
  v1 = 0
  v2 = 0

#Jogador1 começa
  if start == 1:
    print(jogador1.mao())
    while v1 < 1:
      carta_escolhida = input(f"{jogador1.nome()} escolha uma carta: ")
      if carta_escolhida in jogador1.mao():
        index = jogador1.mao().index(carta_escolhida)
        code1 = jogador1.mao().pop(index)
        valor = code1[0]
        if valor == 'A': valor = 1
        if valor == '0': valor = 10
        if valor == 'J': valor = 11
        if valor == 'Q': valor = 12
        if valor == 'K': valor = 13
        valor = int(valor)
        carta1 = valor
        v1 = 1
        r = r + 1
        print()
        print()
      else:
        print("carta escolhida invalida")
        print()

    print(jogador2.mao())
    while v2 < 1:
      carta_escolhida = input(f"{jogador2.nome()} escolha uma carta: ")
      if carta_escolhida in jogador2.mao():
        index = jogador2.mao().index(carta_escolhida)
        code2 = jogador2.mao().pop(index)
        valor = code2[0]
        if valor == 'A': valor = 1
        if valor == '0': valor = 10
        if valor == 'J': valor = 11
        if valor == 'Q': valor = 12
        if valor == 'K': valor = 13
        valor = int(valor)
        carta2 = valor
        v2 = 1
      else:
        print("carta escolhida invalida")
        print()

# Jogador2 começa
  if start == 2:
    print(jogador2.mao())
    while v2 < 1:
      carta_escolhida = input(f"{jogador2.nome()} escolha uma carta: ")
      if carta_escolhida in jogador2.mao():
        index = jogador2.mao().index(carta_escolhida)
        code1 = jogador2.mao().pop(index)
        valor = code1[0]
        if valor == 'A': valor = 1
        if valor == '0': valor = 10
        if valor == 'J': valor = 11
        if valor == 'Q': valor = 12
        if valor == 'K': valor = 13
        valor = int(valor)
        carta1 = valor
        v2 = 1
        r = r + 1
        print()
        print()
      else:
        print("carta escolhida invalida")
        print()

    print(jogador1.mao())
    while v1 < 1:
      carta_escolhida = input(f"{jogador1.nome()} escolha uma carta: ")
      if carta_escolhida in jogador1.mao():
        index = jogador1.mao().index(carta_escolhida)
        code2 = jogador1.mao().pop(index)
        valor = code2[0]
        if valor == 'A': valor = 1
        if valor == '0': valor = 10
        if valor == 'J': valor = 11
        if valor == 'Q': valor = 12
        if valor == 'K': valor = 13
        valor = int(valor)
        carta2 = valor
        v1 = 1
      else:
        print("carta escolhida invalida")
        print()

  #Pontos
  print(carta1, ' x ', carta2)
  if carta1 > carta2:
    if start == 1:
        print(f"{jogador1.nome()} venceu")
        print()
        print()
        start = 1
        if empate != []:
          while x in range(len(empate)):
            carta = empate.pop()
            pilha1.append(carta)
          empate = []

        pilha1.append(code1)
        pilha1.append(code2)
    else:
        print(f"{jogador2.nome()} venceu")
        print()
        print()
        start = 2
        if empate != []:
          while x in range(len(empate)):
            carta = empate.pop()
            pilha2.append(carta)
          empate = []

        pilha2.append(code1)
        pilha2.append(code2)

  elif carta1 < carta2:
    if start == 1:
        print(f"{jogador2.nome()} venceu")
        print()
        print()
        start = 2
        if empate != []:
          while x in range(len(empate)):
            carta = empate.pop()
            pilha2.append(carta)
          empate = []

        pilha2.append(code1)
        pilha2.append(code2)
    else:
        print(f"{jogador1.nome()} venceu")
        print()
        print()
        start = 1
        if empate != []:
          while x in range(len(empate)):
            carta = empate.pop()
            pilha1.append(carta)
          empate = []

        pilha1.append(code1)
        pilha1.append(code2)

  else:
    print("empate")
    print()
    print()
    empate.append(code1)
    empate.append(code2)

print()
print()
print()
print()
print()

if len(pilha1) > len(pilha2):
  print(f"Pilha do {jogador1.nome()}: {pilha1}")
  print(f"Pilha do {jogador2.nome()}: {pilha2}")
  print()
  print(f"{jogador1.nome()} é o vencedor")
  print()
  print()

  codigos1 = ','.join(pilha1)
  codigos2 = ','.join(pilha2)
  pilha = get(f'{api_url}{id}/pile/{jogador1.nome()}/add/?cards={codigos1},{codigos2}')
  if pilha.status_code != 200:
    print(f'Erro de acesso (código: {pilha.status_code})')
  else:
    pilha = pilha.json()
    pprint(pilha)

elif len(pilha1) < len(pilha2):
  print(f"Pilha do {jogador1.nome()}: {pilha1}")
  print(f"Pilha do {jogador2.nome()}: {pilha2}")
  print()
  print(f"{jogador2.nome()} é o vencedor")
  print()
  print()

  codigos1 = ','.join(pilha1)
  codigos2 = ','.join(pilha2)
  pilha = get(f'{api_url}{id}/pile/{jogador2.nome()}/add/?cards={codigos1},{codigos2}')
  if pilha.status_code != 200:
    print(f'Erro de acesso (código: {pilha.status_code})')
  else:
    pilha = pilha.json()
    pprint(pilha)

else:
  print("empate")
  print()
  print(f"Pilha do {jogador1.nome()}: {pilha1}")
  print(f"Pilha do {jogador2.nome()}: {pilha2}")