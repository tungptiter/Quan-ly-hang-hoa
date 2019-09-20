import os
# import csv
import loaihanghoa
import re
danhsach_seller = []

'''TAI KHOAN'''
def condition():
  print("1. It nhat 1 chu cai nan trong [a-z]")
  print("2. It nhat 1 chu so nan trong[0-9]")
  print("3. It nhat 1 ki tu nan trong [A-Z]")
  print("4. It nhat 1 ki tu nan trong [$ # @]")
  print("5. Do dai mat khau toi thieu: 6")

  
def check_password(password = None):
  count = 5
  ok = False
  if len(password)>6 or len(password)<12:
    count -= 1
  if re.search("[a-z]",password):
    count -= 1
  if re.search("[0-9]",password):
    count -= 1
  if re.search("[A-Z]",password):
    count -= 1
  if re.search("[$#@]",password):
    count -= 1
  if count == 0:
    ok =True
  #print(self.ok)
  return ok   

def load_taikhoan_luckhoidong():
  files = os.listdir("danhmuc")
  if "password.csv" not in files:
     return

  with open('danhmuc/password.csv', 'r') as f:
    line = f.readline()
    while line:

        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:
            data = {}
            data["ten"] = str_to_reads[0]
            data["password"] = str_to_reads[1]
            
            if data["password"].endswith('\n'):
              data["password"] = data["password"][0:len(data["password"])-1]
            danhsach_seller.append(data)
        line = f.readline()
        
  print("danhsach seller:", danhsach_seller)
	
load_taikhoan_luckhoidong()

def tao_taikhoan():
  data = {}
  ten = input("xin moi nhap ten tai khoan dang nhap:")
  tim_ten_daco = xem_taikhoan(ten)
  if tim_ten_daco is not None:
     print("Da ton tai Ten tai khoan nay. Xin moi ban thu hien chuc nang khac")
     return
  data["ten"] = ten
  temp = condition()
  test_password = input("Password:")
  value = check_password(test_password)
  while value is False:
    temp
    test_password = input("Password:")
    value = check_password(test_password)
    print(value)
  danhsach_seller.append(data)
  data["password"] = test_password
  str_to_save = data["ten"] + "#" + data["password"] + '\n'
  with open('danhmuc/password.csv', 'a') as f:
      data = f.write(str_to_save)
  
def xem_taikhoan(ten = None):
  if ten is None:
      ten = input("xin moi nhap lai Ten tai khoan:")
  for loai in danhsach_seller:
    if loai["ten"] ==ten:
      print(loai)
      return loai

def sua_taikhoan():
  ten = input("Nhap id hang hoa can sua: ")
  tim_ten_da_co = xem_taikhoan(ten)

  while tim_ten_da_co is None:
    print("Khong ton tai Ten tai khoan nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      ten = input("Nhap lai Ten tai khoan can sua: ")
      tim_ten_da_co = xem_taikhoan(ten)

  with open('danhmuc/password.csv', 'w') as f:
    for loai in danhsach_seller:
      if loai["ten"] == ten:

        print("+-----------------------------------------------+")
        print("|Nhan T de thay the Ten tai khoan               |")
        print("|Nhan P de thay password tai khoan              |")
        print("|Nhan A de thay the ca Ten va Password tai khoan|")
        print("+-----------------------------------------------+")
        chon = input("=> Chon chuc nang: ")
        if chon.upper() == "T":
          del loai["ten"]
          loai["ten"] = input("Nhap Ten tai khoan thay the: ")
        elif chon.upper() == "P":
          del loai["password"]
          loai["password"] = input("Nhap password thay the:")
        else:
          del loai["ten"]
          del loai["password"]
          loai["ten"] = input("Nhap Ten tai khoan thay the: ")
          loai["password"] = input("Nhap Password thay the:")

      str_to_save = loai["ten"] + "#" + loai["password"] +  "\n"
      f.write(str_to_save)
  # print("danh sach seller sau khi Sua:",danhsach_seller)

def xoa_taikhoan():
  ten = input("Nhap id hang hoa can xoa: ")
  tim_ten_da_co = xem_taikhoan(ten)

  while tim_ten_da_co is None:
    print("Khong ton tai Ten tai khoan nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      ten = input("Nhap lai Ten tai khoan can xoa: ")
      tim_ten_da_co = xem_taikhoan(ten)

  with open('danhmuc/password.csv', 'w') as f:
    for loai in danhsach_seller:
      if loai["ten"] == ten:

        print("+-----------------------------------------------+")
        print("|Nhan T de xoa Ten tai khoan                    |")
        print("|Nhan P de xoa password tai khoan               |")
        print("|Nhan A de xoa ca Ten va Password tai khoan     |")
        print("+-----------------------------------------------+")
        chon = input("=> Chon chuc nang: ")
        if chon.upper() == "T":
          del loai["ten"]
          continue
        elif chon.upper() == "P":
          del loai["password"]
          continue
        else:
          del loai["ten"]
          del loai["password"]
          continue
      str_to_save = loai["ten"] + "#" + loai["password"] +  "\n"
      f.write(str_to_save)
  # print("danh sach seller sau khi Sua:",danhsach_seller)
def login():
  ok = False
  ten = input("Ten tai khoan: ")
  tim_ten_da_co = xem_taikhoan(ten)

  while tim_ten_da_co is None:
    print("Khong ton tai Ten tai khoan nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      ten = input("Nhap lai Ten tai khoan: ")
      tim_ten_da_co = xem_taikhoan(ten)
  for loai in danhsach_seller:
    if loai["ten"] == ten:
      test_password = input("Password: ")
      if loai["password"] == test_password:
        ok = True
    return ok
'''END OF TAI KHOAN'''
# tao_taikhoan()
# sua_taikhoan()
# xoa_taikhoan()
# g = login()
# print(g)