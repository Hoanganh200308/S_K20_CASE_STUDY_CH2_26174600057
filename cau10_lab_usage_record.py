from datetime import datetime

# 1. Nhap du lieu dau vao
ma_phien = input("Nhap ma phien: ")
ma_may = input("Nhap ma may: ")
cong_suat = float(input("Nhap cong suat thiet bi (W): "))
thoi_gian = float(input("Nhap thoi gian su dung (phut): "))
don_gia = float(input("Nhap don gia dien (VND/kWh): "))

# 2. Tinh toan cac gia tri (Khong dung if)
# Dien nang (kWh) = (Cong suat W / 1000) * (Thoi gian phut / 60)
dien_nang = (cong_suat / 1000) * (thoi_gian / 60)
chi_phi = dien_nang * don_gia

# Dung toan tu so sanh de tra ve True/False cho gia tri Boolean
tren_60_phut = thoi_gian > 60

# Lay thoi diem ghi nhan hien tai
thoi_diem_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Xuat ket qua ra man hinh theo dinh dang
print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat:.2f} W")
print(f"Thoi luong: {thoi_gian:.0f} phut")
print(f"Dien nang: {dien_nang:.3f} kWh")
print(f"Chi phi: {chi_phi:.2f} VND")
print(f"Tren 60 phut: {tren_60_phut}")
print(f"Thoi diem ghi nhan: {thoi_diem_text}")
