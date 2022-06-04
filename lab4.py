termos = input('').split()
operacao = termos[0]
a = int(termos[1])
b = int(termos[2])

while operacao != '0':
  if operacao == '+':
    print(a+b)
  elif operacao == '-':
    print(a-b)
  elif operacao == '*':
    print(a*b)
  elif operacao == '/':
    print(a // b, a % b)
  elif operacao == ';':
    # a = b + k*x
    div = []
    if a < b:
      a,b = b,a
    if a != b:
      for x in range(1, a-b+1):
        if (a-b) % x == 0:
          div.append(x)
    else:
      div.append(0)
    print(*div)

  termos = input('').split()
  operacao = termos[0]
  a = int(termos[1])
  b = int(termos[2])
