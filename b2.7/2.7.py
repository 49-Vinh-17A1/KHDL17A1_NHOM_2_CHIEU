# p_A :  xác suất số chính phẩm được lấy ra từ máy 
# p_B : xác suất số chính phẩm được lấy ra từ thùng
p_A = 0.98
p_B = 0.6
# p_a : Xác suất số phế phẩm được lấy ra từ máy
# p_b : xác suất số phế phẩm được lấy ra từ thùng
p_a = 1 - p_A
p_b = 1 - p_B
# Nhận thấy số sản phẩm có thể lấy ra được là X = 0,1,2,3,4(máy lấy 2, thùng lấy 2)

 # X = 0 : không lấy được chính phẩm nào từ máy và thùng
p_0 = p_a * p_a * p_b * p_b 
 # X = 1 : lấy được 1 chính phẩm từ máy và thùng
p_1 = 2*(p_A * p_a * p_b * p_b) + 2*(p_a * p_a * p_b * p_B)
        # Th1 : sản phẩm thứ nhất của máy là chính phẩm
        # Th2 : sản phẩm thứ hai của máy là chính phẩm
        # Th3 : sản phẩm thứ nhất của thùng là chính phẩm
        # Th4 : sản phẩm thứ hai của thùng là chính phẩm
 # X = 2 : lấy được 2 chính phẩm từ máy và thùng 
p_2 = 4*(p_A * p_a * p_B * p_b) + (p_A * p_A * p_b * p_b) + (p_a * p_a * p_B * p_B)
        # Th1 : máy - sản phẩm 1, thùng - sản phẩm 1
        # Th2 : máy - sản phẩm 2, thùng - sản phẩm 2
        # Th3 : máy - sản phẩm 1, thùng - sản phẩm 2
        # Th4 : máy - sản phẩm 2, thùng - sản phẩm 1 
        # Th5 : máy - cả hai sản phẩm lấy ra đều là chính phẩm
        # Th6 : thùng - cả hai sản phẩm lấy ra đều là chính phẩm
 # X = 3 : lấy được 3 chính phẩm từ máy và thùng 
p_3 = 2*(p_A * p_a * p_B * p_B) + 2*(p_A * p_A * p_B * p_b)
        # Th1 : máy - 2 sản phẩm, thùng - sản phẩm 1
        # Th2 : máy - 2 sản phẩm, thùng - sản phẩm 2
        # Th3 : máy - sản phẩm 1, thùng - 2 sản phẩm
        # Th4 : máy - sản phẩm 2, thùng - 2 sản phẩm

 # X = 4 : ấy được 4 chính phẩm từ máy và thùng 
p_4 = p_A * p_A * p_B * p_B 
        # Th : máy - 2 chính phẩm, thùng - 2 chính phẩm

print('Bảng phân phối xác suất : ')
print('X | 0       | 1        | 2        | 3        | 4        ')
print(f'P | {round(p_0, 6)} | {round(p_1, 6)} | {round(p_2, 6)} | {round(p_3, 6)} | {round(p_4, 6)}')

# Tính kỳ vọng và phương sai của X
E_X = 0 * p_0 + 1 * p_1 + 2 * p_2 + 3 * p_3 + 4 * p_4
E_X2 = 0**2 * p_0 + 1**2 * p_1 + 2**2 * p_2 + 3**2 * p_3 + 4**2 * p_4
V_X = E_X2 - E_X**2
print(f'kỳ vọng của X là : {round(E_X,4)}, phương sai của X là : {round(V_X,4)}')

# Nhận thấy rằng chỉ khi 2 or 4 sản phẩm chính lấy ra từ máy và thùng thì mới bằng nhau : 
# gọi Z là số chính phẩm bằng nhau : 
p_Z_2 = 2*(p_A * p_a * p_B * p_b) # máy - 1, thùng - 1
p_Z_4 = p_A * p_A * p_B * p_B # máy - 2, thùng - 2
print('xác suất để số sản phẩm tốt do máy sản xuất và số sản phẩm tốt lấy ra từ lô hàng bằng nhau là : ', round(p_Z_2,4), round(p_Z_4,4))