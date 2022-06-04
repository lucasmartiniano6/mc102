def count_max(elementos):
  best, cnt = 0, 0
  best_class = ''
  prev = elementos[0]
  for idx in range(1, len(elementos)):
    if elementos[idx] == prev:
      cnt +=1  
    else:
      cnt = 0
    if cnt+1 > best:
      best = cnt+1
      best_class = elementos[idx]
    prev = elementos[idx] 
  return best_class, best

def unico(elementos):
  classes = []
  for el in elementos:
    if el not in classes:
      classes.append(el)
  return len(classes)

def separarClasses(elementos, titulo):
  HA, CR, CC = [], [], []  
  for el in elementos:
    if el in HA or el in CR or el in CC:
      continue
    if 'HA_' in el:
      HA.append(el)
    elif 'CR_' in el:
      CR.append(el)
    elif el not in titulo:
      CC.append(el)
  HA = [el.replace(' ','-').lower().replace('ha_','HA_') for el in HA]
  CR = [el.replace(' ','-').lower().replace('cr_','CR_') for el in CR]
  CC = [el.replace(' ','-').lower().replace('cc_','CC_') for el in CC]
  
  return HA, CR, CC

def main():
  ent = input().split('/')
  titulo = ent[1]
  elementos = ent[0].split(', ')
  nome_max, num_max = count_max(elementos)
  print(nome_max, num_max)
  num_unico = unico(elementos)
  print(num_unico)
  HA, CR, CC = separarClasses(elementos, titulo)
  print(HA, CR, CC, sep='\n')

if __name__ == '__main__':
  main()
