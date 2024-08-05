my_tp = tuple(map(int, input().split()))
danhsach1 = list(set(my_tp))

danhsach2 = []

for i in my_tp:
  count = my_tp.count(i)
  if count % 5 == 0 and count % 10 != 0:
    danhsach2.append(i)

neww = set(danhsach2)
print(neww)


