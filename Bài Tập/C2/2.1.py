class ThanhSinh:
    def __init__(self, ho_ten, toan, ly, hoa):
        self.ho_ten = ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.danh_sach= []

    def nhap_thong_tin(self,ho_ten,toan,ly,hoa):
        self.ho_ten=ho_ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        #self.ho_ten=input('Nhập họ và tên thí sinh: ')
        #self.toan = float(input("Điểm môn Toán: "))
        #self.ly = float(input("Điểm môn Lý: "))
        #self.hoa = float(input("Điểm môn Hoá: "))
        self.danh_sach.append({'ho_ten ': ho_ten,'toan ':toan,'ly ':ly,'hoa ':hoa,'tong ':toan+ly+hoa})

    def in_thong_tin(self):
        print('DANH SÁCH THÍ SINH TRÚNG TUYỂN')
        print("{:<20}{:^5}{:^5}{:^5}".format("ho_ten","toan","ly","hoa"))
        self.danh_sach=sorted(self.danh_sach,key=lambda x:x["tong"],reverse=True)
        for ts in self.danh_sach:
            if ts['toan']+ts['ly']+ts['hoa']<20:
                continue
            print("{:<20}{:^5}{:^5}{:^5}".format(ts['toan'],ts['ly'],ts['hoa']))

a=ts(0,0,0,0)
a.nhap_thong_tin()