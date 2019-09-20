import os
import datetime
import loaihanghoa
import hanghoa_real
danhsachhanghoa_nhapkho = []

'''NHAP KHO HANG HOA'''

def load_hanghoa_nhapkho():
  files = os.listdir("danhmuc")
  if "hanghoa_nhapkho.csv" not in files:
     return

  with open('danhmuc/hanghoa_nhapkho.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:

            hanghoanhap = {}
            hanghoanhap["id"] = str_to_reads[0]
            hanghoanhap["soluong"] = str_to_reads[1]
            hanghoanhap["ngaynhap"] = str_to_reads[2]
            if hanghoanhap["ngaynhap"].endswith('\n'):
              hanghoanhap["ngaynhap"] = hanghoanhap["ngaynhap"][0:len(hanghoanhap["ngaynhap"])-1]
            
            danhsachhanghoa_nhapkho.append(hanghoanhap)
        line = f.readline()
  print("danhsachhanghoa nhap kho:", danhsachhanghoa_nhapkho)
	
load_hanghoa_nhapkho()

def tao_hanghoa_nhapkho():
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
  if id in danhsachhanghoa_nhapkho:
      ok = True

  data["id"] = id
  data["soluong"] = input("xin moi nhap so luong hang hoa:")
  now = datetime.datetime.now()
  data["ngaynhap"] = now.strftime("%d/%m/%y,%H/%M/%S")
  # now = datetime.datetime.now()
  # data["ngaynhap"] = now.strftime("%d/%m/%y")
  danhsachhanghoa_nhapkho.append(data)

  str_to_save = data["id"] + "#" + data["soluong"] + "#" + data["ngaynhap"] + '\n'
  with open('danhmuc/hanghoa_nhapkho.csv', 'a') as f:
      f.write(str_to_save)
  
def xem_hanghoa_nhapkho(id = None):
  if id is None:
      id = input("xin moi nhap id hang hoa:")
  for loai in danhsachhanghoa_nhapkho:
    if loai["id"] == id:
      print(loai)
      return loai

def sua_hanghoa_nhapkho():
  id_hanghoa = input("Nhap id hang hoa nhap kho can sua: ")
  tim_id_hanghoa_nhapkho_daco = xem_hanghoa_nhapkho(id_hanghoa)

  while tim_id_hanghoa_nhapkho_daco is None:
    print("Khong co thu tuc nhap kho cua id hang hoa nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      id_hanghoa = input("Nhap lai id hang hoa nhap kho can sua: ")
      tim_id_hanghoa_da_co = xem_hanghoa_nhapkho(id_hanghoa)

  count = 0
  with open('danhmuc/hanghoa_nhapkho.csv', 'w') as f:
    for loai in danhsachhanghoa_nhapkho:
      if loai["id"] == id_hanghoa and count == 0:
        # time = input("Thoi gian nhap kho day/month/year la: ")
        time = input("Thoi gian nhap kho day/month/year,hour/minute/second la: ")
        # if time == loai["ngaynhap"][0 : 8]:
        if time == loai["ngaynhap"]:
          del loai["soluong"]
          loai["soluong"] = input("Nhap so luong hang hoa nhap kho thay the: ")
          count = 1
        else :
          print("Khong co thong tin ve hang hoa " + loai["id"] + "nhap kho vao ngay nay")
      str_to_save = loai["id"] + "#" + loai["soluong"] + "#" + loai["ngaynhap"] + "\n"
      f.write(str_to_save)
  print("danh sach hang hoa nhap kho sau khi SUA:",danhsachhanghoa_nhapkho)

def xoa_hanghoa_nhapkho():
  id_hanghoa = input("Nhap id hang hoa nhap kho can xoa: ")
  tim_id_hanghoa_nhapkho_daco = xem_hanghoa_nhapkho(id_hanghoa)

  while tim_id_hanghoa_nhapkho_daco is None:
    print("Khong co thu tuc nhap kho cua id hang hoa nay!")
    choose = input("Nhan Y de tiep tuc, nhan E de thoat: ")
    if choose.upper() == "E":
      return
    if choose.upper() == "Y":
      id_hanghoa = input("Nhap lai id hang hoa nhap kho can sua: ")
      tim_id_hanghoa_da_co = xem_hanghoa_nhapkho(id_hanghoa)
  count = 0
  with open('danhmuc/hanghoa_nhapkho.csv', 'w') as f:
    for loai in danhsachhanghoa_nhapkho:
      if loai["id"] == id_hanghoa and count == 0:
        # time = input("Thoi gian nhap kho day/month/year la: ")
        time = input("Thoi gian nhap kho day/month/year,hour/minute/second la: ")
        # if time == loai["ngaynhap"][0 : 8]:
        if time == loai["ngaynhap"]:
          del loai["id"]
          del loai["soluong"]
          del loai["ngaynhap"]
          count = 1
          continue
        else :
          print("Khong co thong tin ve hang hoa " + loai["id"] + "nhap kho vao ngay nay")
      str_to_save = loai["id"] + "#" + loai["soluong"] + "#" + loai["ngaynhap"] + "\n"
      f.write(str_to_save)
  print("danh sach hang hoa nhap kho sau khi XOA:",danhsachhanghoa_nhapkho)

'''END OF NHAP KHO HANG HOA'''
# tao_hanghoa_nhapkho()
# sua_hanghoa_nhapkho()
# xoa_hanghoa_nhapkho()