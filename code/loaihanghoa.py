import os
import json
danhsachloaihanghoa = []
def load_loaihanghoa_luckhoidong():
  files = os.listdir("danhmuc")
  if "loaihanghoa.csv" not in files:
     return
  
  with open('danhmuc/loaihanghoa.csv', 'r') as f:
    line = f.readline()
    while line:

        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:
            loaihanghoa = {}
            loaihanghoa["id"] = str_to_reads[0]
            tenloai = str_to_reads[1]
            if tenloai.endswith('\n'):
                tenloai = tenloai[0:len(tenloai)-1]
            loaihanghoa["ten"] = tenloai
            danhsachloaihanghoa.append(loaihanghoa)
        line = f.readline()
        
  print("danhsachloaihanghoa:", danhsachloaihanghoa)
load_loaihanghoa_luckhoidong()
	
def tao_loaihanghoa():
  data = {}
  id = input("xin moi nhap id loai hang hoa:")
  tim_id_daco = xem_loaihanghoa(id)

  if tim_id_daco is not None:
    print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
    return

  data["id"] = id
  data["ten"] = input("xin moi nhap ten loai hang hoa:")
  danhsachloaihanghoa.append(data)
  print("danh sach loai hang hoa: ",danhsachloaihanghoa)
  str_to_save = data["id"] + "#" + data["ten"] + '\n'
  with open('danhmuc/loaihanghoa.csv', 'a') as f:
	    data = f.write(str_to_save)



def xem_loaihanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id loai hang hoa:")
  for loai in danhsachloaihanghoa:
    if loai["id"] == id:
      print("loai hang hoa: ", loai)
      return loai

def sua_loaihanghoa():
  id_loai = input("Nhap id loai hang hoa can sua: ")
  tim_id_loai_daco = xem_loaihanghoa(id_loai)

  while tim_id_loai_daco is None:
    print("Khong ton tai id loai hang hoa nay! ")
    choose = input("Nhan Y de nhap lai id, nhan E de thoat: ")
    if choose.upper() == 'E':
      return
    if choose.upper() == "Y":
      id_loai = input("Nhap lai id loai hang hoa can sua: ")
      tim_id_loai_daco = xem_loaihanghoa(id_loai)

  with open('danhmuc/loaihanghoa.csv', 'w') as f:
    for loai in danhsachloaihanghoa:
      if loai["id"] == id_loai:
          del loai["ten"]
          loai["ten"] = input("Nhap ten loai hang hoa moi: ")
      str_to_save = loai["id"] + "#" + loai["ten"] + '\n'
      f.write(str_to_save)
  print("danhsachloaihanghoa sau khi sua:", danhsachloaihanghoa)



def xoa_loaihanghoa():
  id_loai = input("Nhap id loai hang hoa can xoa: ")
  tim_id_loai_daco = xem_loaihanghoa(id_loai)

  while tim_id_loai_daco is None:
    print("Khong ton tai id loai hang hoa nay! ")
    choose = input("Nhan Y de nhap lai id, nhan E de thoat: ")
    if choose.upper() == 'E':
      return
    if choose.upper() == "Y":
      id_loai = input("Nhap id loai hang hoa can sua: ")
      tim_id_loai_daco = xem_loaihanghoa(id_loai)

  with open('danhmuc/loaihanghoa.csv', 'w') as f:
    for loai in danhsachloaihanghoa:
      if loai["id"] == id_loai:
        del loai["id"]
        del loai["ten"]
        continue
      str_to_save = loai["id"] + "#" + loai["ten"] + '\n'
      f.write(str_to_save)
  print("danhsachloaihanghoa sau khi Xoa:", danhsachloaihanghoa)

# tao_loaihanghoa()
# sua_loaihanghoa()
# xoa_loaihanghoa()
