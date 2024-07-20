sohoanhao=[]
n=int(input())
for i in range(1,n+1):
  a=0
  for j in range(1,i):
    if i%j==0:
      a+=i
  if a==i:
    sohoanhao.append(i)
print(sohoanhao)        