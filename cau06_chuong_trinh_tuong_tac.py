
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất (W): "))
so_phut = float(input("Nhập số phút sử dụng: "))
don_gia = float(input("Nhập đơn giá: "))


dien_nang = (cong_suat * so_phut) / 60000
chi_phi = dien_nang * don_gia


print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang}")
print(f"Chi phí: {chi_phi}")