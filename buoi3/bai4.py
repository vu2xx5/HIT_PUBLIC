def chuan_hoa_ho_ten(ho_ten):
  ho_ten=ho_ten.strip().lower()
  tu=ho_ten.split()
  tu=[i.capitalize() for i in tu]
  ho_ten_chuan=' '.join(tu)
  return ho_ten_chuan

chuan_hoa_ho_ten(input()) 