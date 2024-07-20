'''def tinhtong(n):
  tong=0
  for i in range(1,2*n+2):
    if i % 2 ==0:
      tong -= i
    else:
      tong += i
  return tong
tinhtong(5)



def tinhtong(n):
  tong=0
  for i in range(1,n+1):
    tong += 1/i
  return tong
tinhtong(2)




import math

a=int(input())
b=int(input())
c=int(input())
delta = b**2 - 4*a*c
if delta >0:
  x1 = (-b + math.sqrt(delta)) / (2 * a)
  x2 = (-b - math.sqrt(delta)) / (2 * a)
  print("Phương trình có 2 nghiệm phân biệt là:", x1, x2)
elif delta ==0:
  x= -b / (2*a)
  print("Phương trình có 1 nghiệm", x)
else:
  print("phương trình vô nghiệm")'''