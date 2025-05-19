# lớp Khởi tạo
class quanly:
    stt=1
    so_thu_tu=1
    so_luong_khach=100
    
    def __init__(self, ten, tuoi,Mon_an,Do_uong,Dia_chi,SDT):
        self.ten="tên của khách hàng: "+ten 
        self.tuoi="tuổi của khách hàng: "+tuoi
        self.Mon_an="món ăn của khách hàng: "+Mon_an
        self.Do_uong="đồ uống của khách hàng: "+Do_uong
        self.Dia_chi="địa chỉ của khách hàng: "+Dia_chi
        self.SDT="số điện thoại của khách hàng: "+SDT
        self.stt=quanly.so_thu_tu
        quanly.so_thu_tu +=1

    def xin_chao(self):
        return "Xin chào bạn " + self.ten
# add các đối tượng vào lớp 
khach1=quanly("Nguyễn Văn A","20","Bún bò Huế","Trà sữa","Hà Nội","0123456789")
khach2=quanly("Nguyễn Văn B","21","Phở bò","Cà phê","Hà Nội","0123456789")
khach3=quanly("Nguyễn Văn C","22","Cơm tấm","Nước ngọt","Hà Nội","0123456789")
khach4=quanly("Nguyễn Văn D","23","Bánh mì","Trà chanh","Hà Nội","0123456789")
khach5=quanly("Nguyễn Văn E","24","Mì Quảng","Nước ép","Hà Nội","0123456789")
khach6=quanly("Nguyễn Văn F","25","Bánh xèo","Trà đào","Hà Nội","0123456789")
khach7=quanly("Nguyễn Văn G","26","Bánh cuốn","Trà xanh","Hà Nội","0123456789")
khach8=quanly("Nguyễn Văn H","27","Bánh bèo","Trà sữa","Hà Nội","0123456789")
#xuất thông tin của đối tượng
# print(khach1.xin_chao())
# for key,value in khach1.__dict__.items():
#     print(f"{key}: {value}")

# xuất ra stt của từng đối tượng
# print(khach1.stt)
# print(khach2.stt)
# print(khach3.stt)
# print(khach4.stt)
# print(khach5.stt)
# print(khach6.stt)
# print(khach7.stt)
# print(khach8.stt)