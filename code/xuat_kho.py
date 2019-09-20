import os
import datetime
import loaihanghoa
import hanghoa_real
danhsachhanghoa_xuatkho = []

'''XUAT KHO HANG HOA'''

def load_hanghoa_xuatkho():
  files = os.listdir("danhmuc")
  if "hanghoa_xuatkho.csv" not in files:
     return

  with open('danhmuc/hanghoa_xuatkho.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:

            hanghoaxuat = {}
            hanghoaxuat["id"] = str_to_reads[0]
            hanghoaxuat["soluong"] = str_to_reads[1]
            hanghoaxuat["ngayxuat"] = str_to_reads[2]
            if hanghoaxuat["ngayxuat"].endswith('\n'):
              hanghoaxuat["ngayxuat"] = hanghoaxuat["ngayxuat"][0:len(hanghoaxuat["ngayxuat"])-1]
            
            danhsachhanghoa_xuatkho.append(hanghoaxuat)
        line = f.readline()
  print("danhsachhanghoa xuat kho:", danhsachhanghoa_xuatkho)
	
load_hanghoa_xuatkho()

def tao_hanghoa_xuatkho():
  data = {}
  id = input("xin moi nhap id hang hoa:")
  tim_id_daco = hanghoa_real.xem_hanghoa(id)
  while tim_id_daco is None:
      
      print("Danh sach hang hoa:")
      for loai in hanghoa_real.danhsachhanghoa:
          print(loai["id"] + "  " + loai["ten"])
      chon = input("Ban muon nhap tiep nhan 'Y', chon chuc nang khac nhan 'E': ")
      if chon.upper() == "E":
          return     
      if chon.upper() == "Y": 
          id = input("xin moi nhap id hang hoa:")
          tim_id_daco = hanghoa_real.xem_hanghoa(id)
  ok = False
  if id in danhsachhanghoa_xuatkho:
      ok = True

  data["id"] = id
  data["soluong"] = input("xin moi nhap so luong hang hoa:")
  now = datetime.datetime.now()
  data["ngayxuat"] = now.strftime("%d/%m/%y,%H/%M/%S")
  # now = datetime.datetime.now()
  # data["ngaynhap"] = now.strftime("%d/%m/%y")
  danhsachhanghoa_xuatkho.append(data)

  str_to_save = data["id"] + "#" + data["soluong"] + "#" + data["ngayxuat"] + '\n'
  with open('danhmuc/hanghoa_xuatkho.csv', 'a') as f:
      f.write(str_to_save)
  
def xem_hanghoa_xuatkho(id = None):
  if id is None:
      id = input("xin moi nhap id hang hoa:")
  for loai in danhsachhanghoa_xuatkho:
    if loai["id"] == id:
      print(loai)
      return loai

def sua_hanghoa_xuatkho():
  id_hanghoa = input("Nhap id hang hoa xuat kho can sua: ")
  tim_id_hanghoa_xuatkho_daco = xem_hanghoa_xuatkho(id_hanghoa)

  while tim_id_hanghoa_xuatkho_daco is None:
    print("Khong co thu tuc xuat kho cua id hang hoa nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      id_hanghoa = input("Nhap lai id hang hoa xuat kho can sua: ")
      tim_id_hanghoa_da_co = xem_hanghoa_xuatkho(id_hanghoa)

  count = 0
  with open('danhmuc/hanghoa_xuatkho.csv', 'w') as f:
    for loai in danhsachhanghoa_xuatkho:
      if loai["id"] == id_hanghoa and count == 0:
        # time = input("Thoi gian nhap kho day/month/year la: ")
        time = input("Thoi gian xuat kho day/month/year,hour/minute/second la: ")
        # if time == loai["ngaynhap"][0 : 8]:
        if time == loai["ngayxuat"]:
          del loai["soluong"]
          loai["soluong"] = input("Nhap so luong hang hoa xuat kho thay the: ")
          count = 1
        else :
          print("Khong co thong tin ve hang hoa " + loai["id"] + "xuat kho vao ngay nay")
      str_to_save = loai["id"] + "#" + loai["soluong"] + "#" + loai["ngayxuat"] + "\n"
      f.write(str_to_save)
  print("danh sach hang hoa xuat kho sau khi SUA:",danhsachhanghoa_xuatkho)

def xoa_hanghoa_xuatkho():
  id_hanghoa = input("Nhap id hang hoa xuat kho can xoa: ")
  tim_id_hanghoa_xuatkho_daco = xem_hanghoa_xuatkho(id_hanghoa)

  while tim_id_hanghoa_xuatkho_daco is None:
    print("Khong co thu tuc xuat kho cua id hang hoa nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      id_hanghoa = input("Nhap lai id hang hoa xuat kho can sua: ")
      tim_id_hanghoa_da_co = xem_hanghoa_xuatkho(id_hanghoa)
  count = 0
  with open('danhmuc/hanghoa_xuatkho.csv', 'w') as f:
    for loai in danhsachhanghoa_xuatkho:
      if loai["id"] == id_hanghoa and count == 0:
        # time = input("Thoi gian xuat kho day/month/year la: ")
        time = input("Thoi gian xuat kho day/month/year,hour/minute/second la: ")
        # if time == loai["ngayxuat"][0 : 8]:
        if time == loai["ngayxuat"]:
          del loai["id"]
          del loai["soluong"]
          del loai["ngayxuat"]
          count = 1
          continue
        else :
          print("Khong co thong tin ve hang hoa " + loai["id"] + "xuat kho vao ngay nay")
      str_to_save = loai["id"] + "#" + loai["soluong"] + "#" + loai["ngayxuat"] + "\n"
      f.write(str_to_save)
  print("danh sach hang hoa xuat kho sau khi XOA:",danhsachhanghoa_xuatkho)

'''END OF XUAT KHO HANG HOA'''
# tao_hanghoa_xuatkho()
# sua_hanghoa_xuatkho()
# xoa_hanghoa_xuatkho()