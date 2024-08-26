n = int(input())
count = 0
number = 1
listt = []
while count < n:
  sum_chuso = 0
  for i in str(number):
    sum_chuso += int(i)
  if sum_chuso == 10:
    listt.append(number)
    count += 1
  number += 1

print(max(listt))