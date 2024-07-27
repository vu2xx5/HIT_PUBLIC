s1=input()
s2=input()
print(s1[::-1])
a=int(input())
b=int(input())
# điều kiện 2 số a và b: 1 <=a < b <= len(s2)
s2_new=s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
print(s2_new)

for i in range(len(s1)):
  if i % 2 != 0:
    s3=' '.join(s1[i])
    print(s3)

min_len=min(len(s1), len(s2))
s4=''
for j in range(min_len):
  s4+=s1[j]+s2[j]
s4+=s1[min_len:]+s2[min_len:]
print(s4)

if len(s1) > 1 and len(s2) > 1:
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]
    print("s1:", new_s1)
    print("s2:", new_s2)
else:
    print("Chuỗi s1 hoặc s2 không đủ độ dài để đổi chỗ 2 ký tự đầu tiên")