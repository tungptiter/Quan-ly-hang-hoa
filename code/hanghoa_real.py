import os
# import csv
import loaihanghoa
danhsachhanghoa = []

'''HANG HOA'''

def load_hanghoa_luckhoidong():
  files = os.listdir("danhmuc")
  if "hanghoa.csv" not in files:
     return

  with open('danhmuc/hanghoa.csv', 'r') as f:
    line = f.readline()
    while line:

        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:
            hanghoa = {}
            hanghoa["id"] = str_to_reads[0]
            hanghoa["ten"] = str_to_reads[1]
            hanghoa["giaban"] = str_to_reads[2]
            hanghoa["loaihanghoa_id"] = str_to_reads[3]
            
            if hanghoa["loaihanghoa_id"].endswith('\n'):
              hanghoa["loaihanghoa_id"] = hanghoa["loaihanghoa_id"][0:len(hanghoa["loaihanghoa_id"])-1]
            danhsachhanghoa.append(hanghoa)
        line = f.readline()
        
  print("danhsachhanghoa:", danhsachhanghoa)
	
load_hanghoa_luckhoidong()

def tao_hanghoa():
  data = {}
  id = input("xin moi nhap id hang hoa:")
  tim_id_daco = xem_hanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chuc nang khac")
     return
  data["id"] = id
  data["ten"] = input("xin moi nhap ten hang hoa:")
  data["giaban"] = input("xin moi nhap gia ban:")
  loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
  tim_idloai_daco = loaihanghoa.xem_loaihanghoa(loaihanghoa_id)
  
  while tim_idloai_daco is None:
    print("Danh sach loai hang hoa:")
    for loai in loaihanghoa.danhsachloaihanghoa:
        print(loai["id"] + "  " + loai["ten"])
    chon = input("Ban muon nhap tiep nhan 'Y', chon chuc nang khac nhan 'E': ")
    if chon.upper() == "E":
      return     
    if chon.upper() == "Y": 
      loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
      tim_idloai_daco = loaihanghoa.xem_loaihanghoa(loaihanghoa_id)
	
  data["loaihanghoa_id"] = loaihanghoa_id
  danhsachhanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["loaihanghoa_id"] + '\n'
  with open('danhmuc/hanghoa.csv', 'a') as f:
      data = f.write(str_to_save)
  
def xem_hanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id hang hoa:")
  for hanghoa in danhsachhanghoa:
    if hanghoa["id"] == id:
      print(hanghoa)
      return hanghoa

def sua_hanghoa():
  id_hanghoa = input("Nhap id hang hoa can sua: ")
  tim_id_hanghoa_da_co = xem_hanghoa(id_hanghoa)

  while tim_id_hanghoa_da_co is None:
    print("Khong ton tai id hang hoa nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      id_hanghoa = input("Nhap lai id hang hoa can sua: ")
      tim_id_hanghoa_da_co = xem_hanghoa(id_hanghoa)

  with open('danhmuc/hanghoa.csv', 'w') as f:
    for loai in danhsachhanghoa:
      if loai["id"] == id_hanghoa:

        print("+-----------------------------------------+")
        print("|Nhan T de thay the Ten hang hoa          |")
        print("|Nhan G de thay the Gia hang hoa          |")
        print("|Nhan A de thay the ca Ten va Gia hang hoa|")
        print("+-----------------------------------------+")
        chon = input("=> Chon chuc nang: ")
        if chon.upper() == "T":
          del loai["ten"]
          loai["ten"] = input("Nhap ten hang hoa thay the: ")
        elif chon.upper() == "G":
          del loai["giaban"]
          loai["giaban"] = input("Nhap gia ban hang hoa thay the:")
        else:
          del loai["ten"]
          del loai["giaban"]
          loai["ten"] = input("Nhap ten hang hoa thay the: ")
          loai["giaban"] = input("Nhap gia ban hang hoa thay the:")

      str_to_save = loai["id"] + "#" + loai["ten"] + "#" + loai["giaban"] + "#" + loai["loaihanghoa_id"] + "\n"
      f.write(str_to_save)
  print("danh sach hang hoa sau khi Sua:",danhsachhanghoa)

def xoa_hanghoa():
  id_hanghoa = input("Nhap id hang hoa can xoa: ")
  tim_id_hanghoa_da_co = xem_hanghoa(id_hanghoa)

  while tim_id_hanghoa_da_co is None:
    print("Khong ton tai id hang hoa nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      id_hanghoa = input("Xin moi nhap lai id hang hoa can xoa: ")
      tim_id_hanghoa_da_co = xem_hanghoa(id_hanghoa)

  with open('danhmuc/hanghoa.csv', 'w') as f:
    for loai in danhsachhanghoa:
      if loai["id"] == id_hanghoa:
        del loai["id"] 
        del loai["ten"]
        del loai["giaban"]
        continue
      str_to_save = loai["id"] + "#" + loai["ten"] + "#" + loai["giaban"] +"#" + loai["loaihanghoa_id"] + "\n"
      f.write(str_to_save)
  print("danh sach hang hoa sau khi XOA: ",danhsachhanghoa)
'''END OF HANG HOA'''
# tao_hanghoa()
# sua_hanghoa()
# xoa_hanghoa()