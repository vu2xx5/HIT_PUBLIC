#nhập mã sinh viên đk ở 2 bàn
masvb1=input("nhập vào mã sinh viên bàn 1:")
masvb2=input("nhập vào mã sinh viên bàn 2:")
A=set(masvb1.split())
B=set(masvb2.split())

print(A & B)
print(A | B)
print(A - B)