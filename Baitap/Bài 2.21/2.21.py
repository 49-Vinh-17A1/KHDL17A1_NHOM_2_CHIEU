import math
# có y = e**x => x= ln(y)
# fy(y) = [(d/dy)*ln(y)]*fx(ln(y))= (1/y)*(1/b-a) với a<ln(y)<b => e**a < y <e**b
# 
def fy(y,a,b):
    if math.e**a < y < math.e**b:
        return 1/[y*(b-a)]
    else:
        return 0
# z = ln(x) => x = e**z
# fz(z) = [(d/dz)*(e**z)]*fx(e**z) = (e**z)*(1/b-a)  với   a < e**z <b => ln(a) < z < ln(b)
def fz(z,a,b):
    if math.log(a,math.e) < z < math.log(b,math.e):
        return math.e**z/(b-a)
    else:
        return 0
print("fy(y) = 1/[y*(b-a)] : e**a < y < e**b  \n          0         : y khác")
print("fz(z) = e**z/(b-a)  : ln(a) < z < ln(b) \n          0         : z khác ")