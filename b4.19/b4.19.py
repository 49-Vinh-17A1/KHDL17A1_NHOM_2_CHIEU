def integral_rectangular(f, a, b, n):
    delta_x = (b - a) / n
    integral = 0
    for i in range(n):
        x_left = a + i * delta_x
        x_right = a + (i + 1) * delta_x
        integral += f((x_left + x_right) / 2) * delta_x
    return integral
# a)
# f(x,y,z) = kxyz dxdydz = 1
integral_z = integral_rectangular(lambda z: z,0,1,10000)
integral_z = round(integral_z,4)
integral_y = integral_rectangular(lambda y: y,0,1,10000)
integral_y = round(integral_y,4)
integral_x = integral_rectangular(lambda x: x,0,1,10000)
integral_x = round(integral_x,4)
integral_xyz = integral_x*integral_y*integral_z
k = 1/integral_xyz
print("k =",k)
#b)
#fxy(x,y)= tich_phan tu 0 den 1 cua xyzdz= xy*tich_phan tu 0 den 1 cua zdz
ham_mat_do_xy = integral_rectangular(lambda z: z,0,1,10000)
ham_mat_do_xy = round(ham_mat_do_xy,4)
print(f"fxy(x,y) = xy*{ham_mat_do_xy} : 0<= x <=1,0<= y <=1 \n            0     : (x<0 or x>1) or (y<0 or y>1)")          
#fxz(x,z)= tich_phan tu 0 den 1 cua xyzdy= xz*tich_phan tu 0 den 1 cua ydy
ham_mat_do_xz = integral_rectangular(lambda y: y,0,1,10000)
ham_mat_do_xz = round(ham_mat_do_xz,4)
print(f"fxz(x,z) = xz*{ham_mat_do_xz} : 0<= x <=1,0<= z <=1 \n            0     : (x<0 or x>1) or (z<0 or z>1)")  
#fyz(y,z)= tich_phan tu 0 den 1 cua xyzdx= yz*tich_phan tu 0 den 1 cua xdx
ham_mat_do_yz = integral_rectangular(lambda x: x,0,1,10000)
ham_mat_do_yz = round(ham_mat_do_yz,4)
print(f"fyz(y,z) = yz*{ham_mat_do_yz} : 0<= y <=1,0<= z <=1 \n            0     : (y<0 or y>1) or (z<0 or z>1)")  
#fx(x)= tich_phan tu 0 den 1 cua fxy(x,y)dy= x*tich_phan tu 0 den 1 cua y*0.5dy
ham_mat_do_x = integral_rectangular(lambda y: y/2,0,1,10000)
ham_mat_do_x = round(ham_mat_do_x,4)
print(f"fx(x) = x*{ham_mat_do_x} : 0<= x <=1 \n        0      : x<0 or x>1")  
#fy(y)= tich_phan tu 0 den 1 cua fxy(x,y)dx= y*tich_phan tu 0 den 1 cua x*0.5dx
ham_mat_do_y = integral_rectangular(lambda x: x/2,0,1,10000)
ham_mat_do_y = round(ham_mat_do_y,4)
print(f"fy(y) = y*{ham_mat_do_y} : 0<= y <=1 \n        0      : y<0 or y>1")  
#fz(z)= tich_phan tu 0 den 1 cua fxz(x,z)dx= z*tich_phan tu 0 den 1 cua x*0.5dx
ham_mat_do_z = integral_rectangular(lambda x: x/2,0,1,10000)
ham_mat_do_z = round(ham_mat_do_z,4)
print(f"fz(z) = z*{ham_mat_do_z} : 0<= z <=1 \n        0      : z<0 or z>1")  
#c)
# fx/y= fxy(x,y)/fy(y) = (xy*0.5)/y*(0.25)=x*(0.5/0.25)
x_voi_dieu_kien_y = 0.5/0.25
print(f"fx|y = x*{x_voi_dieu_kien_y}")
#fy/xz = f(x,y,z)/fxz(x,z)= (xyz)/(xz*0.5) = y*(1/0.5)
y_voi_dieu_kien_xz = 1/0.5
print(f"fy|xz = y*{y_voi_dieu_kien_xz}")






