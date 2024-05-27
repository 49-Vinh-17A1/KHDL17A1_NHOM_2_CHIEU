def f_xy(x, y):
    if 0 < x <= y < 1:
        return 8 * x * y
    else:
        return 0

# Tích phân của hàm f(x,y) theo y từ x đến 1
def f_x(x):
    if 0 < x < 1:
        return 4 * x * (1 - x**2)
    else:
        return 0
# Tích phân của hàm f(x,y) the0 x từ 0 đến y
def f_y(y):
    if 0 < y < 1:
        return 4 * y **3
    else:
        return 0
print("1) Hàm mật độ biên của X, Y:")
print("f_X(x) =4*x*1-x**2, x thuoc (0,1)")
print("f_Y(y) =4*y**3,  y thuoc (0,1)")
# hàm mat d0 c0 dieu kien
def f_x_given_y(x, y):
    if 0 < x <= y < 1:
        return (2 * x) /  y**2
    else:
        return 0
def f_y_given_x(y, x):
    if 0 < x <= y < 1:
        return (2 * y) / (1 - x**2)
    else:
        return 0
print("\n2) Hàm mật độ có điều kiện:")
print("f_{X|Y}(x|y) =(2*x)/y**2,voi 0<x<=y<1")
print("f_{Y|X}(y|x) =(2*y)/1-x**2 0<x<=y<1" )
# hàm tích phân
def integral(f, a, b, n=1000):
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(n)) * h
    return result
# tích phân kép
def double_integral(f, x_min, x_max, y_min, y_max, n=1000):
    dx = (x_max - x_min) / n
    dy = (y_max - y_min) / n
    result = 0
    for i in range(n):
        for j in range(n):
            x = x_min + i * dx
            y = y_min + j * dy
            result += f(x, y) * dx * dy
    return result

# Kỳ vọng và phương sai
EX = double_integral(lambda x, y: x * f_xy(x, y), 0, 1, 0, 1)
EY = double_integral(lambda x, y: y * f_xy(x, y), 0, 1, 0, 1)
EX2 = double_integral(lambda x, y: x**2 * f_xy(x, y), 0, 1, 0, 1)
EY2 = double_integral(lambda x, y: y**2 * f_xy(x, y), 0, 1, 0, 1)
VX = EX2 - EX**2
VY = EY2 - EY**2
print("\n3) Kỳ vọng và phương sai:")
print("E(X) =",round( EX,2))
print("E(Y) =", round (EY,2))
print("V(X) =", round(VX,2))
print("V(Y) =", round (VY,2))
# Kỳ vọng có điều kiện
def E_X_given_y(y):
    return integral(lambda x: x * f_x_given_y(x, y), 0, y)
def E_Y_given_x(x):
    return integral(lambda y: y * f_y_given_x(y, x), x, 1)
print("\n4) Kỳ vọng có điều kiện:")
# E(X|Y) = tích phân từ 0 đén 1 của x*(2x/y**2)dx = (1/y**2)*tich_phan từ 0 đến 1 của 2x**2dx
EX_Y = integral(lambda x: 2*(x**2),0,1,100000)
EX_Y = round(EX_Y,4)
print(f"E(X|Y) = 1/(y**2)*{EX_Y} ")
# E(Y|X) = tích phân từ 0 đến 1 của y*(2y/(1-x**2))dy= 1/(1-x**2)*tich_phan tu 0 den 1 cua 2y**2dy
EY_X = integral(lambda y: 2*(y**2),0,1,100000)
EY_X = round(EY_X,4)
print(f"E(Y|X) = 1/(1-x**2)*{EY_X} ")
# Hiệp phương sai và hệ số tương quan
EXY = double_integral(lambda x, y: x * y * f_xy(x, y), 0, 1, 0, 1)
covXY = EXY - EX * EY
rhoXY = covXY / (VX**0.5 * VY**0.5)
print("\n5) Hiệp phương sai và hệ số tương quan:")
print("Cov(X, Y) =", covXY)
print("rho(X, Y) =", rhoXY)