n=int(input())
a=[]
for i in range (n):
  pt1=str(input().split())
  pt2=str(input().split())
  a.append([pt1,pt2])

diem = [diem for ten,diem in a]

diem2 = sorted(list(set(diem)))[1]

for ten,diem in a:
    if diem == diem2:
        print(ten)
