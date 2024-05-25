import math
def giai_thua(x):
    if x ==0:
        return 1
    else:
        return x*giai_thua(x-1)
def to_hop(n,k):
    C = giai_thua(n)/(giai_thua(k)*giai_thua(n-k))
    return C
# xac suat mo duoc cua la
p = 1/4
# X = 0,1,2,3,4  X~B(n=4,p=0.25)
X0 = to_hop(4,0)*(p**0)*((1-p)**4)
X1 = to_hop(4,1)*p*((1-p)**3)
X2 = to_hop(4,2)*(p**2)*((1-p)**2)
X3 = to_hop(4,3)*(p**3)*(1-p)
X4 = to_hop(4,4)*(p**4)*((1-p)**0)
X= [0,1,2,3,4]
bang= [X0,X1,X2,X3,X4]
bang_phan_phoi_sx=[]
bang_phan_phoi_sx.append(X)
bang_phan_phoi_sx.append(bang)
print(bang_phan_phoi_sx)
E=0
for i in bang_phan_phoi_sx[0]:
    E = E + i*bang_phan_phoi_sx[1][i]
print("Kì vọng của X là: ", E)
V = 0
for i in bang_phan_phoi_sx[0]:
    V = V + (X[i] - E)**2 * bang[i]
print("Phương sai của X là: ", V)
F_X = []
xac_suat = 0
for i in bang_phan_phoi_sx[0]:
    xac_suat += bang[i]
    F_X.append(xac_suat)

print("Hàm phân phối xác suất: ")
for i in bang_phan_phoi_sx[0]:
    print(f"F(X <= {X[i]}) = {F_X[i]}")

max = bang.index(max(bang))
mode = max
print("Mốt của X là: ", mode)