print("*Que página de meme do Instagram você é?*")

idade = int(input("Qual a sua idade?\n"))

if idade < 0 or idade > 125:
  print(idade)
  print("Erro: entrada inválida")
elif idade < 25:
  print(idade)
  segundos = int(input("Quantos segundos são necessários para saber se um vídeo é bom?\n"))
  print(segundos)
  if segundos < 0:
    print("Erro: entrada inválida")
  elif segundos <= 5:
    print("RESULTADO")
    print("Você deveria estar no TikTok")
  else:
    print("RESULTADO")
    print("Sua página de memes é: @meltmemes")
elif 25 <= idade <= 40:
  print(idade)
  banda = input("Qual banda você gosta mais?\n")
  if banda == "A": 
    print("A) Matanza")
    print("RESULTADO")
    print("Sua página de memes é: @badrockistamemes")
  elif banda == "B":
    print("B) Iron Maiden")
    print("RESULTADO")
    print("Sua página de memes é: @badrockistamemes")
  elif banda == "C" or banda == "D":
    if banda == "C":
      print("C) Imagine Dragons")
    else:
      print("D) BlackPink")
    capivara = input("São as capivaras os melhores animais da Terra?\n")
    print(capivara)
    if capivara == "Sim":
      print("RESULTADO")
      print("Sua página de memes é: @genteboamemes")
    elif capivara == "Não":
      print("RESULTADO")
      print("Sua página de memes é: @wrongchoicememes")
    else:
      print("Erro: entrada inválida")
elif idade > 40:
  print(idade)
  imagem = input("Que imagem de bom dia você manda no grupo da família?\n")
  if imagem == "A" :
    print("A) Bebê em roupa de flor")
    print("RESULTADO")
    print("Sua página de memes é: @bomdiabebe")
  elif imagem == "B":
    print("B) Gato")
    print("RESULTADO")
    print("Sua página de memes é: @kittykatmsgs")
  elif imagem == "C":
    print("C) Coração e rosas")
    print("RESULTADO")
    print("Sua página de memes é: @bomdiaflordodia")
  else:
    print("NADA")
    print("Erro: entrada inválida")

