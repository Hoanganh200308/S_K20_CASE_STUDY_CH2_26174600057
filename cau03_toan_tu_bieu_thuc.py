
tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("So gio tron ven:", so_gio)
print("So phut con lai:", so_phut_con_lai)

su_dung_lau = tong_phut > 60
print("Su dung lau:", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Du lieu hop le:", du_lieu_hop_le)

bieu_thuc_1 = 100 + 20 * 3    # Nhan truoc, cong sau: 100 + 60 = 160
bieu_thuc_2 = (100 + 20) * 3  # Ngoac truoc, nhan sau: 120 * 3 = 360
print("Ket qua bieu thuc 1 (100 + 20 * 3):", bieu_thuc_1)
print("Ket qua bieu thuc 2 ((100 + 20) * 3):", bieu_thuc_2)
# Du doan ket qua
# So gio: 2
# So phut con lai: 15
# Su dung lau: True
# Du lieu hop le: True
# Ket qua bieu thuc 1: 160
# Ket qua bieu thuc 2: 360