import os
import json
import datetime
import hanghoa_real


danhsachhoadon = []
'''HOA DON'''


'''load hang hoa ban va /khach hang luc khoi dong may 
trong file hanghoaban va khachhangthanthiet ban dau khi moi su dung thi se khoi tao cac gia tri la 0 va string'''

def load_hanghoaban_and_khachhang():
  global hanghoaban 
  global khachhang 
  global ngaybanhang
  with open('danhmuc/hanghoaban.json','r') as f1:
    hanghoaban = json.load(f1)
  with open('danhmuc/khachhangthanthiet.json','r') as f2:
    khachhang = json.load(f2)
  with open('danhmuc/ngaybanhang.json','r') as f3:
    ngaybanhang = json.load(f3)
    
load_hanghoaban_and_khachhang()

'''end of load hang hoa ban va khach hang luc khoi dong may '''

def tao_hoadon():
  hoadon = {}
  
  sohoadon = input("Xin moi nhap vao so hoa don: ")
  xem_hoadon(sohoadon)
                  
  hoadon["sohoadon"] = sohoadon
  hoadon["nguoimua"] = input("Nhap nguoi mua: ")
  now = datetime.datetime.now()
  hoadon["ngaymua"] = now.strftime("%d/%m/%Y, %H:%M:%S)")
  hoadon["tongtientruocthue"] = 0
  hoadon["thue"] = 0.1
  hoadon["tongtien"] = 0
  hoadon["danhsachhanghoa"] = []
  
  nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
  while nhaphanghoa.upper() == 'Y':
      hanghoa = {}
      
      hanghoa_id = input("nhap ID hang hoa: ")
      
      tim_id_daco = hanghoa_real.xem_hanghoa(hanghoa_id)
      while tim_id_daco is None:
          chon_ma_hanghoa = input("Ma hang hoa nay Chua ton tai, Xin moi chon ma khac nhan 'Y' ,chon chuc nang khac nhan 'E': ")
          for loai in hanghoa_real.danhsachhanghoa:
              print( loai["id"] + " " + loai["ten"])
          if chon_ma_hanghoa.upper() =="E":
              return 
          if chon_ma_hanghoa.upper() == "Y":
              hanghoa_id = input("nhap ID hang hoa: ")
              tim_id_daco = hanghoa_real.xem_hanghoa(hanghoa_id)   
      hanghoa["id"] = hanghoa_id               
      soluong = input("nhap so luong: ")
      hanghoa["soluong"] = int(soluong)
      for loai in hanghoa_real.danhsachhanghoa:
        if hanghoa["id"] == loai["id"]:
            hanghoa["ten"] = loai["ten"]
            hanghoa["giaban"] = loai["giaban"] 
            hanghoa["thanhtien"] = int(hanghoa["soluong"]) * int(hanghoa["giaban"])
            
            if hanghoa["ten"] in hanghoaban:
                hanghoaban[hanghoa["ten"]]["tongso"] += hanghoa["soluong"]
                hanghoaban[hanghoa["ten"]]["doanhthu"] += int(hanghoa["thanhtien"])
            else:
                hanghoaban[hanghoa["ten"]] = {
                "tongso": hanghoa["soluong"],
                "doanhthu": int(hanghoa["thanhtien"])
                }
            print(hanghoaban)
            break
      hoadon["danhsachhanghoa"].append(hanghoa)
      
      hoadon["tongtientruocthue"] += int(hanghoa["thanhtien"])
      
      nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
      
  hoadon["tongtien"] = hoadon["tongtientruocthue"]*hoadon["thue"] + hoadon["tongtientruocthue"]

  if hoadon["nguoimua"] in khachhang:
    khachhang["tongtien"] +=  hoadon["tongtien"]

  else:
    
    if hoadon["tongtien"] > khachhang["tongtien"]:
      khachhang["tongtien"] = hoadon["tongtien"]
      khachhang["ten"] = hoadon["nguoimua"]
    if hoadon["tongtien"] == khachhang["tongtien"]:
      pass
  
  if ngaybanhang["ngaymua"] in ngaybanhang:
    ngaybanhang["tongtien"] += hoadon["tongtien"]
  else:
    if hoadon["tongtien"] > ngaybanhang["tongtien"]:
      ngaybanhang["ngaymua"] = hoadon["ngaymua"]
      ngaybanhang["tongtien"] = hoadon["tongtien"]
  print(ngaybanhang)    
  print(khachhang)
  danhsachhoadon.append(hoadon)   

  filename = hoadon["sohoadon"] +".json"
  with open('hoadon/' + filename, 'w') as f1:
    json.dump(hoadon, f1)
  with open('danhmuc/hanghoaban.json','w') as f2:
    json.dump(hanghoaban,f2)    
  with open('danhmuc/khachhangthanthiet.json','w') as f3:
    json.dump(khachhang,f3)
  with open('danhmuc/ngaybanhang.json','w') as f4:
    json.dump(ngaybanhang,f4)
  
def xem_hoadon( sohoadon = None):
  file_sohoadon = sohoadon + ".json"
  files = os.listdir("hoadon")
  while file_sohoadon in files:
      chon_sohoadon = input("Da ton tai so hoa don nay! Xin moi chon nhap ma khac nhan 'Y' ,chon Chuc nang khac nhan 'E': ")
      if chon_sohoadon.upper() == "E":
          return 
      elif  chon_sohoadon.upper() == "Y":
          sohoadon = input("Xin moi nhap vao so hoa don: ")
          file_sohoadon = sohoadon + ".json"
    
def kiemtrahoadon():
  sohoadon = input("Nhap so hoa don can kiem tra: ")
  file_sohoadon = sohoadon + ".json"
  files = os.listdir("hoadon")
  while file_sohoadon not in files:
      chon_sohoadon = input("Chua ton tai so hoa don nay! Xin moi chon nhap ma khac nhan 'Y' ,chon Chuc nang khac nhan 'E': ")
      if chon_sohoadon.upper() == "E":
          return 
      elif  chon_sohoadon.upper() == "Y":
          sohoadon = input("Xin moi nhap vao so hoa don: ")
          file_sohoadon = sohoadon + ".json"
  with open('hoadon/' + file_sohoadon, 'r') as infile:
      hoadon = json.load(infile)

      print("\n--------------------VIETNAME LIFE-------------------")
      print("So hoa don: ",hoadon["sohoadon"])
      print("nguoi mua: ",hoadon["nguoimua"])
      print("ngay mua: ",hoadon["ngaymua"])
      print("+----------+----------+----------+----------+----------+")
      print("| STT      |TenHangHoa| Soluong  | DonGia   | ThanhTien|")
      print("+----------+----------+----------+----------+----------+")
      stt = 0
      for hanghoa in hoadon["danhsachhanghoa"]:
        stt += 1
        print("|" + str(stt).rjust(10,' ') + "|" +  str(hanghoa["ten"]).rjust(10,' ') + "|" + str(hanghoa["soluong"]).rjust(10,' ') + "|" + str(hanghoa["giaban"]).rjust(10,' ') + "|" +str(hanghoa["thanhtien"]).rjust(10,' ') + "|")
        print("+----------+----------+----------+----------+----------+")
      print("|                                 Tong tien |" + str(hoadon["tongtien"]).rjust(10,' ') + "|")
      print("+----------+----------+----------+----------+----------+")
'''end of HOADON'''
# tao_hoadon()
# xem = input("Nhap so hoa don can xem: ")
# xem_hoadon(xem)
# kiemtrahoadon()

'''TINH TOAN'''
def hanghoa_banchay_va_itnhat_nhatthang():
  max = 0
  min = 1000
#'''min = 0 thì khi chạy sẽ là nhỏ nhất nên min se luôn = 0'''

  for hanghoa in hanghoa_real.danhsachhanghoa:
    if hanghoa["ten"] in  hanghoaban:
        if(max < hanghoaban[hanghoa["ten"]]["tongso"]):
          max = hanghoaban[hanghoa["ten"]]["tongso"]
          
        if min > hanghoaban[hanghoa["ten"]]["tongso"]:
          min = hanghoaban[hanghoa["ten"]]["tongso"]
        print(max,min)
  print("Hang hoa ban chay nhat va it nhat")
  print("+-----------+-----------+")
  print("| Hanghoa   |  Tongso   |")
  print("+-----------+-----------+")
  for hanghoa in hanghoa_real.danhsachhanghoa:
    if hanghoa["ten"] in  hanghoaban:

      if max == hanghoaban[hanghoa["ten"]]["tongso"]:
        print("|" + str(hanghoa["ten"]).rjust(11,' ') + "|" + str(max).rjust(11,' ') + "|")
        print("+-----------+-----------+")
        
      if min == hanghoaban[hanghoa["ten"]]["tongso"]:
        print("|" + str(hanghoa["ten"]).rjust(11,' ') + "|" + str(min).rjust(11,' ') + "|")
        print("+-----------+-----------+")
        

def tongso_doanhthu_daban():
  tongso_hanghoa = 0
  tong_doanhthu = 0
  print("Tong so va doanh thu hang hoa da ban")
  print("+-----------+-----------+-----------+")
  print("| Hanghoa   |  Tongso   | Doanhthu  |")
  print("+-----------+-----------+-----------+")
  for hanghoa in hanghoa_real.danhsachhanghoa:
    if hanghoa["ten"] in hanghoaban:
      print("|" + str(hanghoa["ten"]).rjust(11,' ') + "|" + str(hanghoaban[hanghoa["ten"]]["tongso"]).rjust(11,' ') + "|" + str(hanghoaban[hanghoa["ten"]]["doanhthu"]).rjust(11,' ') + "|")
      print("+-----------+-----------+-----------+")
      tongso_hanghoa += hanghoaban[hanghoa["ten"]]["tongso"]
      tong_doanhthu += hanghoaban[hanghoa["ten"]]["doanhthu"]
  print("+-----------+-----------+-----------+")    
  print("| Tong cong |" + str(tongso_hanghoa).rjust(11,' ') + "|" +  str(tong_doanhthu).rjust(11, ' ') + "|")
  print("+-----------+-----------+-----------+")

def khachhang_muanhieunhat_thang():
  print("Khach hang mua nhieu nhat")
  print("+--------------------+---------------------+")
  print("|     Khachhang      |      Tongtien       |")
  print("+--------------------+---------------------+")
  print("|" + str(khachhang["ten"]).center(20,' ') + "|" + str(khachhang["tongtien"]).center(21,' ') + "|")
  print("+--------------------+---------------------+")

def ngaybanhang_nhieunhat():
  print("Ngay ban hang nhieu nhat")
  print("+--------------------+---------------------+")
  print("|      Ngayban       |      Tongtien       |")
  print("+--------------------+---------------------+")
  print("|"+ str(ngaybanhang["ngaymua"]).center(20,' ')+ "|" + str(ngaybanhang["tongtien"]).center(21,' ') +"|" )
  print("+--------------------+---------------------+")  
def tongdoanhthu():
  tong_doanhthu = 0
  for hanghoa in hanghoa_real.danhsachhanghoa:
    if hanghoa["ten"] in hanghoaban:
      tong_doanhthu += hanghoaban[hanghoa["ten"]]["doanhthu"]
  print("Tong doanh thu la: ", tong_doanhthu) 
# hanghoa_banchay_va_itnhat_nhatthang()
# tongso_doanhthu_daban()
# khachhang_muanhieunhat_thang()
# ngaybanhang_nhieunhat()
'''END OF TINH TOAN'''