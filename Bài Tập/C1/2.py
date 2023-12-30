class ThanhSinh:
    def __init__(self, hoten, toan, ly, hoa):
        self.hoten = hoten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    
    def in_thong_tin(self):
        print("Họ tên:", self.hoten)
        print("Điểm môn Toán:", self.toan)
        print("Điểm môn Lý:", self.ly)
        print("Điểm môn Hoá:", self.hoa)
    
    def tinh_tong_diem(self):
        return self.toan + self.ly + self.hoa


# Nhập danh sách thí sinh
n = int(input("Nhập số lượng thí sinh: "))
danh_sach = []
for i in range(n):
    print(f"\nNhập thông tin cho thí sinh thứ {i+1}:")
    hoten = input("Họ tên: ")
    toan = float(input("Điểm môn Toán: "))
    ly = float(input("Điểm môn Lý: "))
    hoa = float(input("Điểm môn Hoá: "))
    ts = ThanhSinh(hoten, toan, ly, hoa)
    danh_sach.append(ts)

# In danh sách thí sinh trúng tuyển
diem_chuan = 20.0
print("\nDanh sách thí sinh trúng tuyển:")
danh_sach_trung_tuyen = sorted(danh_sach, key=lambda x: x.tinh_tong_diem(), reverse=True)
for ts in danh_sach_trung_tuyen:
    if ts.tinh_tong_diem() >= diem_chuan:
        ts.in_thong_tin()
        print("Tổng điểm:", ts.tinh_tong_diem())