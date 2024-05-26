import math
def integral_rectangular(f, a, b, n):
    delta_x = (b - a) / n
    integral = 0
    for i in range(n):
        x_left = a + i * delta_x
        x_right = a + (i + 1) * delta_x
        integral += f((x_left + x_right) / 2) * delta_x
    return integral
#1)
# fxy(x,y) phải thỏa mãn hai điều kiện: fxy(x,y) >= 0 với mọi x,y và tích phân kép của fxy(xy)dxdy =1
def ktra_lon_hon_hoac_bang_0(x,y):
    s= math.e**(-x-y)
    return s
# tích phân kép của fxy(x,y)dxdy = tích phân từ 0 đến vô cùng của(e**-y)*[tích phân từ 0 đến vô cùng của e**(-x)dx]dy
tich_phan1 = integral_rectangular(lambda x: math.e**-x,0,99999,1000000)
tich_phan1 = round(tich_phan1,3)
tich_phan2 = integral_rectangular(lambda y: math.e**-y,0,99999,1000000)
tich_phan2 = round(tich_phan2,3)
ticn_phan_kep = tich_phan1*tich_phan2
print("tích phân kép của fxy(x,y)dxdy=",ticn_phan_kep)
#2)
# do f(x,y) =0 khi x<0, y<0 nên ta chỉ cần xét x>0, y>0
# Fxy(x,y)= [tích phân từ 0 đến x của (tích phân từ 0 đến y của e**(-x-y)dy)]dx = [1-(e**-x)]*[(1-e**-y)]
print("Fxy(xy) = [1-(e**-x)]*[(1-e**-y)] : x > 0, y > 0\n             0                    : x<=0 , y<=0")
#3)
#fx(x) = (e**-x)*tich_phan từ 0 đến vô cùng của e**-ydy
tich_phan_fx = integral_rectangular(lambda y: math.e**-y,0,99999,1000000)
tich_phan_fx = round(tich_phan_fx,3)
def fx(x):
    if x>0:
        return (math.e**-x)*tich_phan_fx
    else:
        return 0
print(f"fx(x)  = (e**-x)*{tich_phan_fx}  : x>0 \n             0        : x<=0")
#fy(y) = (e**-y)*tich_phan từ 0 đến vô cùng của e**-xdx
tich_phan_fy = integral_rectangular(lambda x: math.e**-x,0,99999,1000000)
tich_phan_fy = round(tich_phan_fy,3)
def fy(y):
    if y>0:
        return (math.e**-y)*tich_phan_fy
    else:
        return 0
print(f"fy(y)  = (e**-y)*{tich_phan_fy}  : y>0 \n             0        : y<=0")
# với x >0 Fx(x) = P(X<=x) = tich_phan tu 0 den x của e**-xdx = 1 - e**-x
# với x <0 Fx(x) = 0
def Fx(x):
    if x>0:
        return 1-math.e**-x
    else:
        return 0
print(f"Fx(x)  = 1- (e**-x)  : x>0 \n             0        : x<=0")
# với y >0 Fy(y) = P(Y<=y) = tich_phan tu 0 den y của e**-ydx = 1 - e**-y
def Fy(y):
    if y>0:
        return 1-math.e**-y
    else:
        return 0
print(f"Fy(y)  = 1- (e**-y)  : y>0 \n             0        : y<=0")
#4)
# fx|y(x|y) = fxy(x,y)/fy(y) = e**(-x-y)/e**-y = e*-x với x>0
print("fx|y(x|y) = e**-x  : x>0")
# fy|x(y|x) = fxy(x,y)/fx(x) = e**(-x-y)/e**-x = e*-y với y>0
print("fy|x(y|x) = e**-y  : y>0")
#5)
# P(X<= Y <= c) với c= ln2 = tích phân từ 0 đến ln(2) của[tích phân từ 0 đến y e**(-x-y)dx]dy
# <=> P(X<=Y<=ln2) =  tích phân từ 0 đến ln(2) của e**(-y) - e**(-2y)dy
P1 = integral_rectangular(lambda y: math.e**(-y) - math.e**(-2*y),0,math.log(2,math.e),100000)
P1 = round(P1,4)
print("P(X<= Y <= c) =",P1)
#6)
# P(X<Y)= tích phân từ 0 đến vô cùng của[tích phân từ x đến vô cùng của e**(-x-y)dy]dx
# P(X<Y)= tích phân từ 0 đến vô cùng của e**(-2*x)dx
P2 = integral_rectangular(lambda x: math.e**(-2*x),0,99999,1000000)
P2= round(P2,3)
print("P(X<Y)= ",P2)
# P(X+Y<=3) = tích phân từ 0 đến 3 của[tích phân từ 0 đến 3-x của e**(-x-y  )dy]dx
# P(X+Y<=3) = tích phân từ 0 đến 3 của [e**(-x)]*(1-e**(-3+x))
P3 = integral_rectangular(lambda x: (math.e**-x)*(1-math.e**(-3+x)),0,3,100000)
P3 = round(P3,4)
print("P(X+y<=3) =",P3)