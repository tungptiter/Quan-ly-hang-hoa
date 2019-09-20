# import re
import os
import csv
print("Tao mat khau manh!")
print("1. It nhat 1 chu cai nan trong [a-z]")
print("2. It nhat 1 chu so nan trong[0-9]")
print("3. It nhat 1 ki tu nan trong [A-Z]")
print("4. It nhat 1 ki tu nan trong [$ # @]")
print("5. Do dai mat khau toi thieu: 6")

danhsach_seller = []
  
def check(password = None):
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
def ham_create_password():
  name_seller = input("Ten dang nhap: ")
  if name_seller in danhsach_seller:
    print("Da ton tai ten dang nhap nay")
    name_seller = input("Ten dang nhap: ")
  password = input("Create Password: ")
  
  kt = ham_create_password (password)

  while kt.check() is False:
    password = input("Create Password: ")
    kt = create_password(password)

  str_to_save = name_seller + "#" + password + "\n"
  with open('danhmuc/password.csv', 'a') as f:
    f.write(str_to_save)
    
def load_password_luckhoidong():
  files = os.listdir('danhmuc')
  if "password.csv" not in files:
    return
  with open('danhmuc/password.csv','r') as f:
    line = f.readline()
    while line:
      str_to_read = line.split("#")
      if len(str_to_read) > 1:
        dangnhap = {}
        dangnhap["name_seller"] = str_to_read[0]
        mat_khau = str_to_read[1]
        if mat_khau.endswith("\n"):
          mat_khau = mat_khau[0 : len(mat_khau) - 1]
        dangnhap["password"] =mat_khau
        danhsach_seller.append(dangnhap)
    line = f.readline()
  print("Danh sach nguoi dung: ",danhsach_seller)

load_password_luckhoidong()

def login(name = None):
  if password == name:
    pass

def view_account(name = None):
  
  ok = False
  while name is None:
    print("Chua ton tai tai khoan nay!")
    print("Nhan Y de tao tai khoan")
    print("Nhan T de dang nhap lai")
    print("Nhan E de thoat")
    choose = input("=> Chon chuc nang: ")
    if choose.upper() == "Y":
      ham_create_password()
    if choose.upper() == "T":
      name = input("Ten dang nhap: ")
      for test in danhsach_seller:
        if test["name_seller"] == name:
          input_password = input("Password: ")
          if test["password"] == input_password:
            ok = True
    if choose.upper() == "E":
      return

  for test in danhsach_seller:
    if test["name_seller"] == name:
      input_password = input("Password: ")
      if test["password"] == input_password:
        ok = True
  return ok

ham_create_password()