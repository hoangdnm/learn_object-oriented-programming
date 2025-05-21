from Buổi_2 import QuanLy

QuanLy.so_thu_tu = 1  # Đặt lại số thứ tự bắt đầu từ 1
# Tạo danh sách khách hàng
khach_hang_2_list = [
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

for khach1 in khach_hang_2_list:
    if khach1.stt == 2:
        print(khach1.xin_chao())
        print(f"Số thứ tự của bạn là: {khach1.stt}")
        for key, value in khach1.thong_tin().items():
            print(f"|{key}: {value}|")
        print("-" * 40)