import _sqlite3
# Lớp quản lý khách hàng
# code đã cài tiến
class QuanLy:
    so_thu_tu = 1  # Biến lớp để tự động đánh số thứ tự cho mỗi khách hàng

    def __init__(self, ten, tuoi, mon_an, do_uong, dia_chi, sdt):
        self.stt = QuanLy.so_thu_tu
        QuanLy.so_thu_tu += 1

        self.ten = f"Tên của khách hàng: {ten}"
        self.tuoi = f"Tuổi của khách hàng: {tuoi}"
        self.mon_an = f"Món ăn của khách hàng: {mon_an}"
        self.do_uong = f"Đồ uống của khách hàng: {do_uong}"
        self.dia_chi = f"Địa chỉ của khách hàng: {dia_chi}"
        self.sdt = f"Số điện thoại của khách hàng: {sdt}"

    def xin_chao(self):
        return f"Xin chào  {self.ten}"
    

    def thong_tin(self):
        return self.__dict__  # Trả về tất cả thông tin dưới dạng từ điển


# Tạo danh sách khách hàng
khach_hang_list = [
    QuanLy("Nguyễn Văn A", "20", "Bún bò Huế", "Trà sữa", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn B", "21", "Phở bò", "Cà phê", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn C", "22", "Cơm tấm", "Nước ngọt", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn D", "23", "Bánh mì", "Trà chanh", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn E", "24", "Mì Quảng", "Nước ép", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn F", "25", "Bánh xèo", "Trà đào", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn G", "26", "Bánh cuốn", "Trà xanh", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn H", "27", "Bánh bèo", "Trà sữa", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn A", "20", "Bún bò Huế", "Trà sữa", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn B", "21", "Phở bò", "Cà phê", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn C", "22", "Cơm tấm", "Nước ngọt", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn D", "23", "Bánh mì", "Trà chanh", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn E", "24", "Mì Quảng", "Nước ép", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn F", "25", "Bánh xèo", "Trà đào", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn G", "26", "Bánh cuốn", "Trà xanh", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn H", "27", "Bánh bèo", "Trà sữa", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn A", "20", "Bún bò Huế", "Trà sữa", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn B", "21", "Phở bò", "Cà phê", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn C", "22", "Cơm tấm", "Nước ngọt", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn D", "23", "Bánh mì", "Trà chanh", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn E", "24", "Mì Quảng", "Nước ép", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn F", "25", "Bánh xèo", "Trà đào", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn G", "26", "Bánh cuốn", "Trà xanh", "Hà Nội", "0123456789"),
    QuanLy("Nguyễn Văn H", "27", "Bánh bèo", "Trà sữa", "Hà Nội", "0123456789")
]

# Xuất thông tin cho từng khách

# for khach in khach_hang_list:
#     print(khach.xin_chao())
#     print(f"Số thứ tự của bạn là: {khach.stt}")
#     for key, value in khach.thong_tin().items():
#         print(f"|{key}: {value}|")
#     print("-" * 40)

# xuất thông tin cho khách hàng có số thứ tự là 1
# for khach1 in khach_hang_list:
#     if khach1.stt == 1:
#         print(khach1.xin_chao())
#         print(f"Số thứ tự của bạn là: {khach1.stt}")
#         for key, value in khach1.thong_tin().items():
#             print(f"|{key}: {value}|")
#         print("-" * 40)
        
       
