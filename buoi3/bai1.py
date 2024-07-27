#tạo 1 list
n=int(input("nhập số lượng phần tử:"))
a=[]
for i in range (n):
  b=int(input())
  a.append(b)

y=int(input("nhập 1 số y:"))
x=int(input("nhập 1 số x:"))
print(a.count(x))

a[1:7]=[8, 5, 4, 0, 1, 3]
print(a)

print(max(a))
print(min(a))

a.insert(0,y)
print(a)

if a==sorted(a):
  print("TĂNG")
elif a==sorted(a,reverse=True):
  print("GIẢM")
else:
  print("KHÔNG")

new_list = [sum(a[:i+1]) for i in range(n)]
print("List mới với tổng i phần tử đầu tiên:", new_list)

new_list1=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print(sorted(new_list1))
print(sorted(new_list1, key=abs))