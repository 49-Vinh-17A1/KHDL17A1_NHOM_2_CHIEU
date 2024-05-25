p = 1 - (0.10 + 0.05 + 0.05 + 0.10 + 0.20 + 0.05 + 0.05 + 0.35)
p= round(p,4)
bang_pp = [
    [0.10, 0.05, 0.05],
    [0.10, 0.20, 0.05],
    [0.05, p, 0.35]  
]
P_X = [sum(hang) for hang in bang_pp]
P_Y = [sum(bang_pp[i][j] for i in range(3)) for j in range(3)]
gia_tri_X = [10, 15, 20]
gia_tri_Y = [0, 5, 10]
# Tính kỳ vọng E[X] và E[Y]
E_X = sum(gia_tri_X[i] * P_X[i] for i in range(3))
E_Y = sum(gia_tri_Y[j] * P_Y[j] for j in range(3))
# Tính E[XY]
E_XY = sum(gia_tri_X[i] * gia_tri_Y[j] * bang_pp[i][j] for i in range(3) for j in range(3))
# Tính hiệp phương sai
Hiep_phuong_sai_XY = E_XY - E_X * E_Y
# Tính phương sai
E_X2 = sum(gia_tri_X[i]**2 * P_X[i] for i in range(3))
E_Y2 = sum(gia_tri_Y[j]**2 * P_Y[j] for j in range(3))
Phuong_sai_X = E_X2 - E_X**2
Phuong_sai_Y = E_Y2 - E_Y**2
# Tính hệ số tương quan
std_X = Phuong_sai_X**0.5
std_Y = Phuong_sai_Y**0.5
Tuong_quan_XY = Hiep_phuong_sai_XY / (std_X * std_Y)
# Kỳ vọng và phương sai có điều kiện của X khi Y=5
P_X_given_Y5 = [bang_pp[i][1] / P_Y[1] for i in range(3)]
E_X_given_Y5 = sum(gia_tri_X[i] * P_X_given_Y5[i] for i in range(3))
E_X2_given_Y5 = sum(gia_tri_X[i]**2 * P_X_given_Y5[i] for i in range(3))
Phuong_sai_X_given_Y5 = E_X2_given_Y5 - E_X_given_Y5**2
# Kỳ vọng, phương sai và độ lệch chuẩn của Z = X + Y
E_Z = E_X + E_Y
Phuong_sai_Z = Phuong_sai_X + Phuong_sai_Y + 2 * Hiep_phuong_sai_XY
std_Z = Phuong_sai_Z**0.5
print("p =", round(p, 4))
print("Phân phối xác suất biên của X:", [round(px, 4) for px in P_X])
print("Phân phối xác suất biên của Y:", [round(py, 4) for py in P_Y])
print("E[X] =", round(E_X, 4))
print("E[Y] =", round(E_Y, 4))
print("E[XY] =", round(E_XY, 4))
print("Hiệp phương sai (X, Y) =", round(Hiep_phuong_sai_XY, 4))
print("Phương sai của X =", round(Phuong_sai_X, 4))
print("Phương sai của Y =", round(Phuong_sai_Y, 4))
print("Hệ số tương quan (X, Y) =", round(Tuong_quan_XY, 4))
print("E[X|Y=5] =", round(E_X_given_Y5, 4))
print("Phương sai (X|Y=5) =", round(Phuong_sai_X_given_Y5, 4))
print("E[Z] =", round(E_Z, 4))
print("Phương sai của Z =", round(Phuong_sai_Z, 4))
print("Độ lệch chuẩn của Z =", round(std_Z, 4))
