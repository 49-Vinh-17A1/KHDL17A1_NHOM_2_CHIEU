# tính xác suất một khách hàng dừng lại ít nhất là 20 phút
def F(x):
    if x<=0:
        return 0
    elif 0<x<=1:
        return 2*x**3-3*x**2+2*x
    else:
        return 1
it_nhat_20_phut=1-F(20/60)# 20p=1/3h
print("xác suất một khách hàng dừng lại cửa hàng ít nhất 20 phút:",round(it_nhat_20_phut,4))
# hàm mật độ xác suất của x
# hàm F(x)=2x**3-3x**2+2x(hàm gốc)
def F(x):
    return 2*x**3-3*x**2+2*x
# Hàm mật độ=đạ hàm của hàm phân phối
def f(x):
    if 0<x<=1:
     return 6*x**2-6*x+2
    else:
        return 0
print("Hàm mật đo của X:f(x)=6*x**2-6*x+2 : 0<x<=1")
# tính kì vjng phưng sai
def ham_tich_phan(f, a, b, n):
    dx = (b - a) / n 
    tong_dien_tich= 0
    for i in range(n):
        x_i = a + i * dx
        tong_dien_tich += f(x_i) * dx
    return tong_dien_tich
ki_vng = ham_tich_phan(lambda x: x*(6*x**2-6*x+2), 0, 1, 10000)
ki_vng = round(ki_vng,2)
print("kì vọng Ex=:",ki_vng)
phuong_sai=ham_tich_phan(lambda x:(x-ki_vng)**2*(6*x**2-6*x+2),0,1,10000)
print("Phuong sai Vx=:",(round(phuong_sai,4)))