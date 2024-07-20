'''a=int(input())
c=[]
while a>0:
  b=a%10
  a=a//10
  c.append(b)
print(sum(c))


a=int(input())
c=[]
for i in range(1,a+1):
  for j in range(1,i):
   if i%j==0:
    c.append(j)
print(sum(c))


a=int(input())
b=int(input())
c=int(input())
d=False
if a + b > c and a + c > b and b + c > a:
  d=True
else:
  print("không tạo thành 1 tam giác")

while d==True:
  if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("tam giác vuông")
  elif a == b == c:
    print("tam giác đều")
  elif a == b or a == c or b == c:
    print("tam giác cân")
  else:
      if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("tam giác nhọn")
      else:
        print("tam giác tù")
  break

'''