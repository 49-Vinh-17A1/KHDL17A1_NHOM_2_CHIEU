bang_xs_dong_thoi = [{'X': 1, 'Y': 100, 'P': 0.15},
                     {'X': 1, 'Y': 200, 'P': 0.10},
                     {'X': 1, 'Y': 300, 'P': 0.14},
                     {'X': 1.5, 'Y': 100, 'P': 0.05},
                     {'X': 1.5, 'Y': 200, 'P': 0.20},
                     {'X': 1.5, 'Y': 300, 'P': 0.15},
                     {'X': 2, 'Y': 100, 'P': 0.01},
                     {'X': 2, 'Y': 200, 'P': 0.05},
                     {'X': 2, 'Y': 300, 'P': 0.15}]

# 1. Tính kỳ vọng và phương sai của Y
E_Y = sum(i['Y'] * i['P'] for i in bang_xs_dong_thoi) # E(Y) = tổng của (yi.pi) (dùng imprehension)
E_Y2 = sum((i['Y'] ** 2) * i['P'] for i in bang_xs_dong_thoi) # E(Y^2) = tổng của (yi^2.pi)
V_Y = E_Y2 - E_Y ** 2 # V(Y) = E(Y^2) - [E(Y)]^2

print(f"Kỳ vọng của Y: {round(E_Y,2)}") # kỳ vọng được làm tròn đến số thập phân thứ hai
print(f"Phương sai của Y: {round(V_Y,2)}")

# 2. Tính xác suất P(Y = 300 | X = 2)
P_X_2 = sum(i['P'] for i in bang_xs_dong_thoi if i['X'] == 2) # Xác suất của X = 2
P_Y_300_condition_X_2 = next(i['P'] for i in bang_xs_dong_thoi if i['X'] == 2 and i['Y'] == 300) / P_X_2 # xác suất cảu P(Y=300|X=2) = P(y=300,x=2)/P(X=2)

print(f"Xác suất P(Y = 300 | X = 2): {round(P_Y_300_condition_X_2,2)}")

# 3. Tính hiệp phương sai và hệ số tương quan giữa X và Y
E_X = sum(i['X'] * i['P'] for i in bang_xs_dong_thoi) # Kỳ vọng của X 
E_X2 = sum((i['X'] ** 2) * i['P'] for i in bang_xs_dong_thoi) # E(X^2)
V_X = E_X2 - E_X ** 2 # Phương sai của X

E_XY = sum(i['X'] * i['Y'] * i['P'] for i in bang_xs_dong_thoi) # E(X.Y)
Cov_XY = E_XY - E_X * E_Y # Hiệp phương sai của X và Y 
p_XY = Cov_XY / ((V_X ** 0.5) * (V_Y ** 0.5)) # hệ số tương quan của X và Y 

print(f"Hiệp phương sai giữa X và Y: {round(Cov_XY,2)}")
print(f"Hệ số tương quan giữa X và Y: {round(p_XY,2)}")

# 4. Tính kỳ vọng và phương sai khi X = 1.5
E_X_1_5 = sum(i['P'] * i['X'] for i in bang_xs_dong_thoi if i['X'] == 1.5) # E(X = 1.5)
E_X_1_5_2 = sum(i['X']**2 * i['P'] for i in bang_xs_dong_thoi if i['X'] == 1.5) # E(X^2 = 1.5^2)
V_X_1_5 = E_X_1_5_2 - E_X_1_5 ** 2 # V(X = 1.5)

print(f"Kỳ vọng của X khi X = 1.5: {round(E_X_1_5, 2)}")
print(f"Phương sai của X khi X = 1.5: {round(V_X_1_5, 2)}")
