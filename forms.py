class Par:
  def __init__(self, x ,y):
    self._x = x
    self._y = y
  def __str__(self):
    return '(' + str(self._x) + ', ' + str(self._y) + ')'

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    self._x = x

  @property
  def y(self):
    self._y = x

  @y.setter
  def y(self, y):
    self._y = y

def modifica(x):
  x = 10

x = 1
modifica(x)
print(x)

