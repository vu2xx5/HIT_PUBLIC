my_dict={"SV001": 3.2,
    "SV002": 2.8,
    "SV003": 3.7,
    "SV004": 3.0,
    "SV005": 1.9,
    "SV006": 3.5
}
count=0
for diem in my_dict.values(): #đếm số sv có điểm trong khoảng [3.0,3.5]
  if 3.0 <= diem <= 3.5:
    count += 1
print(count)

my_dict["SV007"]=4.0 #thêm sv có mã SV007 và điểm 4.0 vào dict
print(my_dict)

my_list=[]
for i,j in my_dict.items():
  if j < 2.0:
    my_list.append(i)

for k in my_list:
  del my_dict[k]
print(my_dict)
