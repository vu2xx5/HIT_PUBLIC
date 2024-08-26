class Tam_thuc():
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def __str__(self):
    return f"Tam thức bậc 2: {self.a}x**2+{self.b}x+c"
  def get_str(self):
    return self.__str__()
  def __add__(self, other):
    return Tam_thuc(self.a + other.a, self.b + other.b, self.c + other.c)
  def __sub__(self, other):
    return Tam_thuc(self.a - other.a, self.b - other.b, self.c - other.c)
  def daodau(self):
    return Tam_thuc(-self.a, -self.b, -self.c)

tamthuc1=Tam_thuc(1, 2, 3 )
tamthuc2=Tam_thuc(4, 5, 6)

tamthuc1_new=tamthuc1.daodau()
tamthuc2_new=tamthuc2.daodau()
print(tamthuc1+tamthuc2)
print(tamthuc1-tamthuc2)