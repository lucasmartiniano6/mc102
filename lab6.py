class Sala:
  ''' Guarda as informaçãoes de cada sala do mapa'''
  def __init__(self, numero, conexoes, inventario=None):
    ''' Inicializa a sala com seu número, conexão e inventário'''
    self.numero = numero
    self.conexoes = conexoes
    self.inventario = inventario

salas = []
for _ in range(int(input())):
  entrada = input().split()
  num_sala = int(entrada[0])
  conexoes = [int(x) for x in entrada[1:]]
  salas.append(Sala(num_sala, conexoes))

for _ in range(int(input())):
  entrada = input().split()
  num_sala = int(entrada[0])
  salas[num_sala].inventario = entrada[1]

sala_clone = int(input())
sala_bot = int(input())
max_itens = int(input())
itens_bot = []

caminho = [int(x) for x in input().split()]
atual = 0

def game():
  '''
  Loop do jogo, executa até que haja vitória ou derrota do personagem.

  Retorna: False se o jogo acabou, senão, True e a função é chamada novamente.
  '''
  global sala_bot, sala_clone, atual, caminho
  if salas[sala_bot].inventario is not None:
    print('Você está na sala de número {} ela contém um baú com {} e dela você pode ir para as salas {}'.format(sala_bot, salas[sala_bot].inventario, salas[sala_bot].conexoes))
    print('Pegar {}'.format(salas[sala_bot].inventario))
    if len(itens_bot) < max_itens:
      print('{} adicionado ao inventário'.format(salas[sala_bot].inventario))
      if salas[sala_bot].inventario == 'poção':
        print('Você pegou a poção da morte e virou pó instantaneamente. Tente novamente...')
        return False
      itens_bot.append(salas[sala_bot].inventario)
      salas[sala_bot].inventario = None
    else:
      print('Inventário cheio!')
  else:
    print('Você está na sala de número {} e dela você pode ir para as salas {}'.format(sala_bot, salas[sala_bot].conexoes))

  print('Mover para sala {}'.format(caminho[atual]))
  sala_bot = caminho[atual]
  atual += 1

  if sala_bot == sala_clone:
    if 'espada' in itens_bot:
      print('Você derrotou o clone maligno com a espada mágica! Com a Sarah no reino o mundo pode voltar ao equilíbrio.\nPARABÉNS!')
    else:
      print('Infelizmente você encontrou o clone sem a espada das fadas e foi derrotado. Tente novamente...')
    return False
  return True


print("Bem-vindo as Aventuras de Sarah 2.0\nSarah acorda no saguão do antigo castelo de sua família,ela tem a oportunidade única de derrotar o seu clone maligno que se apoderou do reino.\nPara isso ela deve encontrar o baú da sua família que contém a espada mágica que apenas a verdadeira herdeira pode utilizar.\nNa sala onde está Sarah vê várias portas. Qual é a sua próxima ação?")
print('DEBUG - O clone está na sala:', sala_clone)  
while game():
  pass
