armazenamento = {}
saldo = 0
while True:
  entrada = int(input())
  if entrada == 0:
    import datetime
    dia_atual = datetime.datetime.strptime(input(), '%d%m%Y') 
    print('* ESTOQUE')
    rep = []
    for cat in sorted(armazenamento.keys()):
      nomes = {}
      for prod in armazenamento[cat]:
        if int(prod[2]) <= 0:
          rep.append(prod[1])
        else:
          nomes[prod[1]] = prod[2]
      if len(nomes) > 0:
        print(f'- {cat}')
        for n in sorted(nomes.keys()):
          print(n, nomes[n])
    print('* SALDO {:.2f}'.format(saldo))

    if len(rep) > 0:
      print('* REPOSICAO')
      for n in rep:
        print(n)
    
    promo = []
    for cat in armazenamento.keys():
      for prod in armazenamento[cat]:
        prod_date = datetime.datetime.strptime(prod[5], '%d%m%Y') 
        d = datetime.timedelta(days=7) 
        if dia_atual + d >= prod_date:
          if prod[2] > 0:
            promo.append(prod[1])
    if len(promo)>0:
      print('* PROMOCAO')
      sorted(promo)
      for p in promo:
        print(p)
    break

  if entrada == 1:
    #estoque
    n_op = int(input())
    for n in range(n_op):
      produto = input().split()
      produto[2] = int(produto[2])
      modo = int(produto[0])
      if modo == 0:
        #insercao
        if produto[3] not in armazenamento.keys():
          armazenamento[produto[3]] = []
        for prod in armazenamento[produto[3]]:
          if prod[1] == produto[1]:
            #ja tem
            armazenamento[produto[3]].remove(prod)
        armazenamento[produto[3]].append(produto)
      else:
        #remocao
        for cat in armazenamento.keys():
          for prod in armazenamento[cat]:
            if prod[1] == produto[1]:
              if int(prod[2]) >= int(produto[2]):
                print('SUCCESS')
                prod[2] -= int(produto[2])
                break
              else:
                print('ERROR')
                break
  else:
    #caixa
    n_op = int(input()) 
    for _ in range(n_op):
      produto = input().split()
      for cat in armazenamento.keys():
        for prod in armazenamento[cat]:
          if prod[1] == produto[0]:
            saldo += float(produto[1]) * float(prod[4])
            prod[2] -= int(produto[1])
            break
