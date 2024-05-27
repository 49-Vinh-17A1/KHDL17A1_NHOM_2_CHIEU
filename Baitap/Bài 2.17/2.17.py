#2.17
# ý a)
def ham_tich_phan(f, a, b, n):
    dx = (b - a) / n 
    tong_dien_tich= 0
    for i in range(n):
        x_i = a + i * dx
        tong_dien_tich += f(x_i) * dx
    return tong_dien_tich
# tich phan tu 0 den 1 cua f(x) = a dx = a*tich_phan tu 0 den 1 cua 1 = 1
tich_phan = ham_tich_phan(lambda x: 1, 0, 1, 10000)
tich_phan = round(tich_phan,2)
a = 1/tich_phan
print("Gia ti a can tim :",a)
# ý b)
Y=ham_tich_phan(lambda x:a,1/4,1/2,10000)
print(f"P(1/4<X<1/2)={round(Y,4)}")
# ý c
#Do ta có hàm mật độ xác suất của X là f(x)={1  : x thuộc [0,1]
#                                            0  : x k thuộc [0,1]
# mà hàm mật độ là đạo hàm của hàm phân phối xác suất =>1=(x)'=>F(x)=x
def F(x):
    if x<0:
        return 0
    elif 0<=x<=1:
        return x
    else:
        return 1
print("hàm phân phối xác suất của X:")
print("F(x)=x,nếu 0<=x<=1")
print("F(x)=0,nếu x<0")
print("F(x)=1,nếu x>1")