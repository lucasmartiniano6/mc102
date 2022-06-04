class Imagem:
  def __init__(self, l, a, img):
    self.largura = l
    self.altura = a
    self.img = img
    self.selecao = {'x': 0, 'y': 0, 'largura': self.largura, 'altura': self.altura}

  def __repr__(self):
    for l in self.img:
      for c in l:
        print(str(c), '', end='') 
      print()
    return ''

  def getSelect(self):
    mat_sel = []
    idx = 0
    for l in self.img[self.selecao['y']:self.selecao['y']+self.selecao['largura']]:
      mat_sel.append([])
      for c in l[self.selecao['x']:self.selecao['x']+self.selecao['largura']]:
        mat_sel[idx].append(c)
      idx+=1
    return mat_sel
 
  def rotate(self):
    mat_sel = getSelect()
    for l in range(len(mat_sel)):
      for c in range(len(line)):
                    


matriz = [[1, 0, 1],
          [1, 1, 1],
          [0, 1, 0]]

#select  [[1,0],
#         [1,1]]

#        [[1, 1, 1],
#         [1, 0, 1],
#         [0, 1, 0]]

img = Imagem(3,3,matriz)
