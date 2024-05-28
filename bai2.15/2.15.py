#Bai 2.15
import math
#Tham số của phân phối mũ
lam = 0.01

#Xác suất bóng đèn hoạt động trước 10 giờ
t = 10
probability = 1 - math.exp(-lam * t)
print(f"Xác suất bóng đèn hoạt động tốt trước {t} giờ: {probability}")

#Tính kỳ vọng của thời gian hoạt động tốt
expected_value = 1 / lam
print(f"Kỳ vọng của thời gian hoạt động tốt: {expected_value} giờ")