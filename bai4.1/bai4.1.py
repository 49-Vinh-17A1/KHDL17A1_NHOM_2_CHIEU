import math
# Định nghĩa hàm phân phối xác suất đồng thời Fxy(x, y)
#1)
def Fxy(x, y):
    if 0 <= x <= math.pi/2 and 0 <= y <= math.pi/2:
        return math.sin(x) + math.sin(y)
    else:
        return 0

# Fx(x) = Fxy(x,+ vô cùng) = sin(x) + 1
def Fx(x):
    return math.sin(x) + 1

#fx(x) bằng đạo hàm của Fx(x)dx
def fx(x):
    return math.cos(x)
# Fy(y) = F(+vô cùng,y) = sin(y) + 1 
def Fx(x):
    return math.sin(x) + 1

# fy(y) bằng đạo hàm của Fy(y)dy
def fy(y):
    return math.cos(y)
print("fx(x) = cos(x) : 0<=x <= pi/2 \n          0    : x khác")
print("fy(y) = cos(y) : 0<=y <= pi/2 \n          0    : y khác")
# 2)
P = Fxy(math.pi/2,math.pi/3) - Fxy(math.pi/2,math.pi/4) - Fxy(math.pi/6,math.pi/3) + Fxy(math.pi/6,math.pi/4)
print("P(pi/6< X <pi/2, pi/4 < Y < pi/2) =",P)