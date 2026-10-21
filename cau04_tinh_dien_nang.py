
cong_suat_w = 250
don_gia_kwh = 3000

print("--- Truong hop so_phut = 90 ---")
so_phut = 90

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Dien nang:", dien_nang_kwh, "-", type(dien_nang_kwh))
print("Chi phi:", chi_phi, "-", type(chi_phi))


print("\n--- Truong hop so_phut = 60 ---")
so_phut = 60

dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh

print("Dien nang moi:", dien_nang_kwh_moi, "-", type(dien_nang_kwh_moi))
print("Chi phi moi:", chi_phi_moi, "-", type(chi_phi_moi))

print("\nSo sanh: Khi giam thoi gian tu 90 phut xuong 60 phut, dien nang va chi phi deu giam di 1.5 lan.")
# Du doan ket qua
#--- Truong hop so_phut = 90 ---
#Dien nang: 0.375 - <class 'float'>
#Chi phi: 1125.0 - <class 'float'>

#--- Truong hop so_phut = 60 ---
#Dien nang moi: 0.25 - <class 'float'>
#Chi phi moi: 750.0 - <class 'float'>

#So sanh: Khi giam thoi gian tu 90 phut xuong 60 phut, dien nang va chi phi deu giam di 1.5 lan.
