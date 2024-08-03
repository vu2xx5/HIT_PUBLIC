
n = int(input("Nhập số phần tử của mảng: "))

a = []
for i in range(n):
    x = input(f"Nhập phần tử thứ {i + 1}: ")
    a.append(x)

b = tuple(a)

print(b)

dem_phan_tu_dang_so = 0
for phan_tu in b:
    if phan_tu.isdigit():
        dem_phan_tu_dang_so += 1

print(dem_phan_tu_dang_so)
