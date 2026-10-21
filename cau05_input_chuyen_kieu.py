

ma_may = input("Nhập mã máy: ")
print("Kiểu dữ liệu mã máy:", type(ma_may))

cong_suat_raw = input("Nhập công suất W: ")
print("Kiểu dữ liệu công suất (chưa chuyển):", type(cong_suat_raw))

so_phut_raw = input("Nhập số phút sử dụng: ")
print("Kiểu dữ liệu số phút (chưa chuyển):", type(so_phut_raw))

don_gia_raw = input("Nhập đơn giá điện/kWh: ")
print("Kiểu dữ liệu đơn giá (chưa chuyển):", type(don_gia_raw))



print("\n--- BƯỚC 18: CHUYỂN ĐỔI KIỂU ---")
cong_suat = float(cong_suat_raw)  # Chuyển sang float
so_phut = int(so_phut_raw)        # Chuyển sang int
don_gia = float(don_gia_raw)      # Chuyển sang float

print("Kiểu dữ liệu công suất (sau khi chuyển):", type(cong_suat))
print("Kiểu dữ liệu số phút (sau khi chuyển):", type(so_phut))
print("Kiểu dữ liệu đơn giá (sau khi chuyển):", type(don_gia))



print("\n--- BƯỚC 19: TÍNH TOÁN ĐIỆN NĂNG VÀ CHI PHÍ ---")
# Đổi công suất từ W -> kW (chia 1000) và số phút -> giờ (chia 60)
dien_nang = (cong_suat / 1000) * (so_phut / 60)
chi_phi = dien_nang * don_gia

print(f"Điện năng tiêu thụ: {dien_nang} kWh")
print(f"Chi phí điện: {chi_phi} VNĐ")