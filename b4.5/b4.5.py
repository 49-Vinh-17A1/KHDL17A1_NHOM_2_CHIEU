# có fx(x) = fy(y) = 1/(b-a) trong khoảng [a,b]
# Z = X + Y => Y = Z-X
# fz(z) = tích phân từ -vô cùng đến dương vô cùng của fx(x)*fy(z-x) trong khoảng [2a,2b]
# xét 2a <= z <=b thì a <= x <= z-a để Y = Z - X vẫn nằm trong khoảng [a,b]
# fz(z) = tich_phan a đến z-a của (1/(b-a))*(1/(b-a))dx= (z-2a)/[(b-a)**2]
# xét a+b <= z <= 2b thì z-b <= x <= b để Y = Z - X vẫn nằm trong khoảng [a,b]
# fz(z) = tich_phan tu z-b đến b của (1/(b-a))*(1/(b-a))dx = (2b-z)/[(b-a)**2]
def f_Z(z, a, b):
    if 2 * a <= z <= a + b:
        return (z - 2 * a) / (b - a) ** 2
    elif a + b < z <= 2 * b:
        return (2 * b - z) / (b - a) ** 2
    else:
        return 0
#Hàm phân phối Fz(z)
# xét z< 2a: Fz(z) = 0
# xét 2a<=z <=a+b: Fz(z) = tích phân từ 2a đến z của (t-2*a)/[(b-a)**2]dt = [(z - 2*a)**2]/[2*(b-a)**2]
# xét a+b <= z <= 2b: 
#Fz(z) = tích phân từ 2a đến a+b của (t-2*a)/[(b-a)**2]dt + tích phân từ a+b đến z của (2*b - t)/[(b-a)**2] = 1 - [(2*b-z)**2]/[2*(b-a)**2]
# xét z>2b: Fz(z) = 1
def F_Z(z, a, b):
    if z < 2*a:
        return 0
    elif 2*a <= z <= a + b:
        return [(z - 2*a)**2]/[2*(b - a)**2]
    elif a + b < z <= 2*b:
        return 1 - [(2*b - z)**2] /[2*(b - a)**2]
    else:
        return 1
print("             0                             : z < 2*a")
print("Fz(z) = {[(z - 2*a)**2]/[2*(b - a)**2]        : 2*a <= z <= a + b  ")
print("         1 - [(2*b - z)**2] /[2*(b - a)**2]   : a + b < z <= 2*b")
print("             1                             : z > 2b")