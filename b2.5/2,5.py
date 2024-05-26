# p_A : xác suất người thứ nhất ném trúng  
# p_B : xác suất người thứ hai ném trúng 
p_A = 0.7
p_B = 0.8
# p_a : xác suất người thứ nhất không ném trúng
# p_b : xác suất người thứ hai không ném trúng 
p_a = 1 - p_A
p_b = 1 - p_B
# nhận thấy số bóng mà hai người có thể ném được vào rổ là X = 0,1,2,3,4 (mỗi người ném 2 quả) : 

 # X = 0 : cả hai người không ném trúng được quả nào vào rổ
p_0 = p_a * p_a * p_b * p_b 
 # X = 1 : cả hai người ném trúng được 1 quả vào rổ
p_1 = (p_A * p_a * p_b * p_b) + (p_a * p_A * p_b * p_b) + (p_A * p_A * p_b * p_B) + (p_A * p_A * p_B * p_b)
        # Th1 : người thứ nhất ném trúng quả thứ nhất
        # Th2 : người thứ nhất ném trúng quả thứ hai
        # Th3 : người thứ hia ném trúng quả thứ hai 
        # Th4 : người thứ hai ném trúng quả thứ nhất
 # X = 2 : cả hai người ném trúng được 2 quả vào rổ 
p_2 = 4*(p_A * p_a * p_B * p_b) + (p_A * p_A * p_b * p_b) + (p_a * p_a * p_B * p_B)
        # Th1 : người 1 - trúng quả thứ 1, người 2 - trúng quả thứ 1
        # Th2 : người 1 - trúng quả thứ 1, người 2 - trúng quả thứ 2 
        # Th3 : người 1 - trúng quả thứ 2, người 2 - trúng quả thứ 1
        # Th4 : người 1 - trúng quả thứ 2, người 2 - trúng quả thứ 2
        # Th5 : người 1 - trúng cả hai quả, người 2 - khong trúng quả nào 
        # Th6 : người 1 - khong trúng quả nào, người 2 - trúng cả hai quả 
 # X = 3 : cả hai người ném trúng được 3 quả vào rổ 
p_3 = 2*(p_A * p_a * p_B * p_B) + 2*(p_A * p_A * p_B * p_b)
        # Th1 : người 1 - trúng quả thứ nhất, người 2 - trúng hai quả
        # Th2 : người 1 - trúng quả thứ hai, người 2 - trúng hai quả
        # Th3 : người 1 - trúng hai quả, người 2 - trúng quả thứ nhất 
        # Th4 : người 1 - trúng hai quả, người 2 - trúng quả thứ 2

 # X = 4 : cả hai người ném trúng được 4 quả vào rổ 
p_4 = p_A * p_A * p_B * p_B 
        # Th : người 1 - trúng hai quả, người 2 - trúng hai quả

print('Bảng phân phối xác suất : ')
print('X | 0      | 1      | 2      | 3      | 4      ')
print(f'P | {round(p_0, 4)} | {round(p_1, 4)} | {round(p_2, 4)} | {round(p_3, 4)} | {round(p_4, 4)}')

# Nhận thấy rằng chỉ khi 2 or 4 quả vào rổ thì cả hai mơi có số quả ném trúng rổ bằng nhau
# gọi Z là số quả ném trúng rổ bằng nhau : 
p_Z_2 = 2*(p_A * p_a * p_B * p_b) # hai người mỗi người ném được một quả vào rổ
p_Z_4 = p_A * p_A * p_B * p_B # cả hai người đều ném được cả hai quả vào rổ 
print('Xác suất để hai người ném vào rổ có số quả bằng nhau là : ', p_Z_2 + p_Z_4)

# Tính kỳ vọng và phương sai của X
E_X = 0 * p_0 + 1 * p_1 + 2 * p_2 + 3 * p_3 + 4 * p_4
E_X2 = 0**2 * p_0 + 1**2 * p_1 + 2**2 * p_2 + 3**2 * p_3 + 4**2 * p_4
V_X = E_X2 - E_X**2

# Tính kỳ vọng và phương sai của Y = 2X - 5
E_Y = 2 * E_X - 5
V_Y = 2 * V_X # phương sai của hằng số thì bằng 0 

print(f'Kỳ vọng của Y là: {round(E_Y, 4)}, phương sai của Y là: {round(V_Y, 4)}')