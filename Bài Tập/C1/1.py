class hinh_chu_nhat:
    def __init__(self,chieu_dai,chieu_rong):
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong

    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong)*2
    def tinh_dien_tich(self):
        return (self.chieu_dai * self.chieu_rong)
    def display(self):
        print("Thông tin hình chữ nhật ...")
        print("Chiều dài HCN là :",self.chieu_dai)
        print("Chiều rộng HCN là :",self.chieu_rong)
        print("Chu vi HCN là :",self.tinh_chu_vi())
        print("Diện tích HCN là :",self.tinh_dien_tich())

chieu_dai=float(input("nhập chiều dài HCN :"))
chieu_rong=float(input("nhập chiều rộng của HCN :"))

HCN=hinh_chu_nhat(chieu_dai,chieu_rong)
HCN.display()
