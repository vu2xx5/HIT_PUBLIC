n = int(input("Nhập số n: "))

for num in range(1, n + 1):
  num_str = str(num)

  tong = 0
  for digit in num_str:
    tong += int(digit) ** 3

  if tong == num:
    print(num)