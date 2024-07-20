def fibonacci(n):
  day_fibonacci = []

  for i in range(n):
    if i == 0:
      day_fibonacci.append(0)
    elif i == 1:
      day_fibonacci.append(1)
    else:
      so_fibonacci_moi = day_fibonacci[i - 1] + day_fibonacci[i - 2]
      day_fibonacci.append(so_fibonacci_moi)

  return day_fibonacci


n = 10
day_fibonacci = fibonacci(n)
print(day_fibonacci)