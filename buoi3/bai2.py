#tạo 1 list a với k phần tử
a=input().split()
a=[int(i)for i in a]
k=len(a)

#số dòng và số cột cảu ma trận
n=int(input("nhập số dòng:"))
m=int(input("nhập số cột:"))

if n*m > k:
  print("NO")
else:
  X=[] #tạo 1 ma trận X(n x m)
  index=0
  for i in range(n):
    row=[]
    for j in range(m):
      row.append(a[index])
      index+=1
    X.append(row)
  print(X)