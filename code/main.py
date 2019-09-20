import os
import password
import hoadon
import hanghoa_real
import loaihanghoa
import nhap_kho
import xuat_kho

# def next():

#   print("+-------------------------------------+")
#   print("|Nhan T de tiep tuc                   |")
#   print("|Nhan E de thoat                      |")
#   print("+-------------------------------------+")
#   chon = input("=> chon chuc nang: ")
#   if chon.upper() == "E":
#     return False
#   else : 
#     return True

def tai_khoan():
  print("+--------Account-------------+")
  print("|chon C | de Tao tai khoan   |")
  print("|chon S | de Sua tai khoan   |")
  print("|chon X | de Xoa tai khoan   |")
  print("|chon D | de log in          |")
  print("|chon E | de log out         |")
  print("+----------------------------+")
  select = input("=> Chon chuc nang: ")
  while select.upper() != "E":
    if select.upper() == "C":
      password.tao_taikhoan()
    if select.upper() == "S":
      password.sua_taikhoan()
    if select.upper() == "X":
      password.xoa_taikhoan()
      # while next
    if select.upper() == "D":
      temp = password.login()
      if temp is True:
        bang_thongtin()
    if select.upper() == "E":
      print("Bye Bye! Hen gap lai!")
      break
    select = input("=> Chon chuc nang: ")
    print("=> ban da chon chuc nang:",select)


def bang_thongtin():
  print("+-----------------------------MENU------------------------------+")
  print("|Chon TLH | de Tao loai hang hoa                                 |")
  print("|Chon XLH | de Xem loai hang hoa                                 |")
  print("|Chon SLH | de Sua loai hang hoa                                 |")
  print("|Chon DLH | de Xoa loai hang hoa                                 |")
  print("|Chon THH | de Tao hang hoa                                      |")
  print("|Chon XHH | de Xem hang hoa                                      |")
  print("|Chon SHH | de Sua hang hoa                                      |")
  print("|Chon DHH | de Xoa hang hoa                                      |")
  print("|Chon C   | de Tao hoa don                                       |")
  print("|Chon R   | de Xem thong tin hoa don                             |")
  print("|Chon T   | de Tinh tong doanh thu                               |")
  print("|chon G   | de Xem hang hoa ban Chay nhat va It nhat trong thang |") # thieu thuat toan
  print("|chon M   | de Xem Ai mua nhieu tien nhat thang                  |")
  print("|chon N   | de Xem Tong so va Doanh thu cua tung hang hoa        |")
  print("|chon D   | de Xem Ngay mua nhieu tien nhat thang                |")
  print("|Chon E   | de Thoat                                             |")
  print("+----------------------------------------------------------------+")
  print("\n\n")
  while True:
      
      x=input("=> chon chuc nang:")
      print("=> ban da chon chuc nang:",x)
      # if x.upper() == 'TLH':
      #   h = loaihanghoa.tao_loaihanghoa()
      #   t = next()
      #   while True:
      #     t
      #     h

      # loai hang hoa
      if x.upper() == "TLH":
        loaihanghoa.tao_loaihanghoa()  
      if x.upper() == 'XLH':
        loaihanghoa.xem_loaihanghoa()
      if x.upper() == 'SLH':
        loaihanghoa.sua_loaihanghoa()
      if x.upper() == 'DLH':
      # '''end of loai hang hoa'''

      # '''hang hoa'''
        loaihanghoa.xoa_loaihanghoa()    
      if x.upper() == 'THH':
        hanghoa_real.tao_hanghoa()
      if x.upper() == 'XHH':
        hanghoa_real.xem_hanghoa()
      if x.upper() == "SHH":
        hanghoa_real.sua_hanghoa()
      if x.upper() == "DHH":
        hanghoa_real.xoa_hanghoa()
      # '''end of hang hoa'''
      
      # '''hoa don'''
      if x.upper() == 'C':
        print("moi ban tao hoa don")
        hoadon.tao_hoadon()
      if x.upper() == 'R':
        hoadon.kiemtrahoadon()
    #  ''' end of hoa don'''

      if x.upper() == 'T':
        hoadon.tongdoanhthu()
      if x.upper() == 'G':
        hoadon.hanghoa_banchay_va_itnhat_nhatthang()
      if x.upper() == "M":
        hoadon.khachhang_muanhieunhat_thang()
      if x.upper() == 'N':
        hoadon.tongso_doanhthu_daban()
      if x.upper() == "D":
        hoadon.ngaybanhang_nhieunhat()
      if x.upper() == 'E':
          print("Tam biet! Hen gap lai")
          break

tai_khoan()
