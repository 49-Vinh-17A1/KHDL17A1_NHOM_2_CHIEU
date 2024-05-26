#B2.25
def integrate_rectangular(f, a, b, n):
    delta_x = (b - a) / n
    integral = 0
    for i in range(n):
        x_left = a + i * delta_x
        x_right = a + (i + 1) * delta_x
        integral += f((x_left + x_right) / 2) * delta_x
    return integral
# 1)
# goi x la tiền chi cho kinh tế
# xác suất P(x)>3) = 1 - P(x<=3) = 1- (P(0<x<=2) + P(2<x<=3))
# P(0<x<=2)
I1 = integrate_rectangular(lambda x: x/4, 0, 2, 100000)
# P(2<x<=3)
I2 = integrate_rectangular(lambda x: 4/(x**3), 2, 3, 100000)
I = 1 - (I1 + I2)
# 2)
# E(X) = tích phân từ âm vô cùng đến dương vô cùng của x*f(x)dx
E =0
E1= integrate_rectangular(lambda x: (x*x)/4,0, 2,100000)
E2= integrate_rectangular(lambda x: (x*4)/(x**3),2, 99999,100000)
#E(X) = E1 + E2
E = E1 + E2
#V(X)= E(x**2)- [E(X)]**2
V1 = integrate_rectangular(lambda x: (x*x*x)/4,0,2, 100000)
V2 = integrate_rectangular(lambda x: (x*x*4)/(x**3),2,99999, 100000)
# E(x**2) = V1 + V2
V=0
V= (V1 + V2) - E**2
print("xác suất chi cho y tế trong năm trên 3 triệu đồng là",I)
print("kỳ vọng của chi cho y tế hàng năm là",E)
print("Phương sai của y tế hàng năm là",V)