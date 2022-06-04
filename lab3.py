q = int(input())
T = float(input())
C = int(input())
n = int(input())

vp = 0
for frasco in range(1,q+1):
  vi = T * frasco + T * C
  vp += vi
  print('{} {:.2f} {:.2f}'.format(frasco, vi, vp))
print('{:.2f}'.format(vp)) # =vt

m = 0
sum_n = n
while sum_n <= vp:
  print(sum_n)
  sum_n += n
  m += 1
print(m)

print('BATERIA DE TESTES TERMINADA')
