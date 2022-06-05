class Imagem:
  def __init__(self, l, a, img):
    self.largura = l
    self.altura = a
    self.img = img
    self.selecao = {'x': 0, 'y': 0, 'largura': self.largura, 'altura': self.altura}

  def getSelect(self):
    mat_sel = []
    idx = 0
    for l in self.img[self.selecao['y']:self.selecao['y']+self.selecao['altura']]:
      mat_sel.append([])
      for c in l[self.selecao['x']:self.selecao['x']+self.selecao['largura']]:
        mat_sel[idx].append(c)
      idx+=1
    return mat_sel
 
  def rotate(self):
    mat_sel = self.getSelect()
    transposed = []
    line_trans, col_trans = len(mat_sel[0]), len(mat_sel)
    for i in range(line_trans):
        transposed.append([])
        for j in range(col_trans):
            transposed[i].append(0)

    idx = len(mat_sel)-1
    for i in range(len(mat_sel)):
      for j in range(len(mat_sel[i])):
        transposed[j][idx] = mat_sel[i][j]
      idx -= 1

    start_line = self.selecao['y']
    end_line = start_line + len(transposed)
    start_col = self.selecao['x']
    end_col = start_col + len(mat_sel[0])
    for l in range(start_line, end_line):
        for c in range(start_col, end_col):
            if c > len(transposed[0])-1 and l < self.selecao['y']+len(mat_sel): 
                #bug here - add offset!
                self.img[l][c] = 0
            elif l > self.selecao['y']+len(transposed)-1 or c > len(transposed[0])-1:
                pass
            else:
                self.img[l][c] = transposed[l-self.selecao['y']][c-self.selecao['x']]
    
  def copia(self, x, y):
    mat_sel = self.getSelect()
    start_line = y
    end_line = y+self.selecao['altura']
    start_col = x
    end_col = x + self.selecao['largura']
    for l in range(start_line, end_line):
        for c in range(start_col, end_col):
            self.img[l][c] = mat_sel[l-y][c-x]
  
  def recorte(self, x, y):
    self.copia(x,y)
    for l in range(self.selecao['y'],self.selecao['y']+self.selecao['altura']):
        for c in range(self.selecao['x'],self.selecao['x']+self.selecao['largura']):
            self.img[l][c] = 0   
  def espHoriz(self):
    start_line = self.selecao['y']
    end_line = start_line+self.selecao['altura']
    start_col = self.selecao['x']
    end_col = start_col + self.selecao['largura']
    for l in range(start_line, end_line):
        idx = 0
        for c in range((end_col-start_col)//2):
            self.img[l][c+start_col], self.img[l][c+end_col-1-idx] = self.img[l][c+end_col-1-idx], self.img[l][c+start_col]
            idx +=1 

  def espVert(self):
    start_line = self.selecao['y']
    end_line = start_line + self.selecao['altura']
    start_col = self.selecao['x']
    end_col = start_col + self.selecao['largura']
    idx = 0
    for l in range(start_line, (self.selecao['altura']//2)+1):
      self.img[l][start_col:end_col], self.img[end_line-1-idx][start_col:end_col] = self.img[end_line-1-idx][start_col:end_col], self.img[l][start_col:end_col]
      idx += 1

largura, altura = [int(x) for x in input().split()]
n_op = int(input())
matriz = []
for l in range(altura):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
img = Imagem(largura,altura,matriz)

for _ in range(n_op):
    operacao = input().split()
    if operacao[0] == 'selecao':
        img.selecao['x'] = int(operacao[1])
        img.selecao['y'] = int(operacao[2])
        img.selecao['largura'] = int(operacao[3])
        img.selecao['altura'] = int(operacao[4])
    elif operacao[0] == 'recorte':
        dest_x = int(operacao[1])
        dest_y = int(operacao[2])
        img.recorte(dest_x, dest_y)
    elif operacao[0] == 'copia':
        dest_x = int(operacao[1])
        dest_y = int(operacao[2])
        img.copia(dest_x, dest_y)
    elif operacao[0] == 'rotacao':
        img.rotate()
    elif operacao[0] == 'espelhamento':
        if operacao[1] == 'h':
            img.espHoriz()
        else:
            img.espVert()

for l in img.img:
  line = l
  for c in range(len(l)):
    line[c] = '{:03}'.format(l[c])
  print(*line)
