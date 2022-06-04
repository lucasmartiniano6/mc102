attr_sarah = input().split()
attr_clone = input().split()
semente = int(input())

ultimo_numero = semente
def geradorAleatorio():
  global ultimo_numero
  x_n = (7*ultimo_numero + 111) % 1024
  ultimo_numero = x_n
  print(f'MENSAGEM DEBUG - número gerado: {x_n}')
  return x_n

class Player:
  def __init__(self, nome, vida, ataque, defesa):
    self.nome = nome
    self.vida = vida
    self.ataque = ataque
    self.defesa = defesa
    self.oponente = 'O clone' if self.nome == 'Sarah' else 'Sarah'
    self.monstro_invoc = False
  def isAlive(self):
    if self.vida > 0:
      return True
    return False
  def soco(self, defesa_oponente):
    m = geradorAleatorio() % 3
    base_dano = self.ataque - defesa_oponente
    if base_dano < 0:
      dano = 0
    else:
      dano = base_dano * m
    print(f'{self.oponente} sofreu {dano} pontos de dano!')
    return dano
  def arremesoDeFacas(self):
    n = geradorAleatorio() % 6
    dano = 0
    for i in range(1,n+1):
      dano += self.ataque // (3**i)
    print(f'{self.oponente} sofreu {dano} pontos de dano!')
    return dano
  def invocaoDeFada(self):
    p = geradorAleatorio() % 100
    q = geradorAleatorio() % 1024

    self.vida += p
    print(f'{self.nome} ganhou {p} pontos de vida!')
    if (q % 2) != 0 and q < 100:
      self.ataque += q
      print(f'{self.nome} ganhou {q} pontos de ataque!')
    elif (q % 2) == 0 and q < 100 and q != 0:
      self.defesa += q
      print(f'{self.nome} ganhou {q} pontos de defesa!')
    elif q >= 1019:
      self.monstro_invoc = True
    
    return self.monstro_invoc

sarah = Player('Sarah', int(attr_sarah[0]), int(attr_sarah[1]), int(attr_sarah[2]))
clone = Player('O clone', int(attr_clone[0]), int(attr_clone[1]), int(attr_clone[2]))

def sarahOk():
  if not sarah.isAlive():
    return False

  acao = input()
  if acao == 'soco':
    clone.vida -= sarah.soco(clone.defesa)
  elif acao == 'facas':
    clone.vida -= sarah.arremesoDeFacas()
  elif acao == 'fada':
    if sarah.invocaoDeFada():
      print('O quê? A fada trouxe um monstro gigante com ela!')
      print('O Clone e o castelo foram destruídos,')
      print('e Sarah agora tem um novo pet.')
      print('FINAL SECRETO - PARABENS???')
      return 'monstro'
  return sarah.isAlive()

def cloneOk():
  if not clone.isAlive():
    return False

  acao = input()
  if acao == 'soco':
    sarah.vida -= clone.soco(sarah.defesa)
  elif acao == 'facas':
    sarah.vida -= clone.arremesoDeFacas()
  elif acao == 'fada':
    if clone.invocaoDeFada():
      print('O quê? A fada trouxe um monstro gigante com ela!')
      print('Sarah foi derrotada...')
      return 'monstro'
  return clone.isAlive()

while True:
  saida = sarahOk()
  if saida == 'monstro':
    break
  elif saida == False:
    print('Sarah foi derrotada...')
    break

  saida = cloneOk()
  if saida == 'monstro':
    break
  elif saida == False:
    print('O clone foi derrotado! Sarah venceu!')
    print('FIM - PARABENS')
    break
