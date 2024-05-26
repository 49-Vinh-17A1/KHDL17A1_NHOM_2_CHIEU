# ta có bảng phân phối xác suất đồng thời
bang = {
    (1,1) : 0.15 , (1,2) : 0.35,
    (2,1) : 0.20 , (2,2) : 0.05,
    (3,1):0.10   , (3,2) : 0.15

}
# tính đại lượng X và Y có đọc lập hay ko
if bang[(1,1)] == (bang[(1,1)] + bang[(1,2)])*(bang[(1,1)]+bang[(1,2)]+bang[(3,1)]):
    print("X và Y là hai biến độc lập ")
else:
    print("X và Y ko độc lập")

# tính hàm  khối lượng ác suất cs điều kiện P(X=1|Y=2)
py2 = bang[(1,2)]+bang[(2,2)]+bang[(3,2)]
p12 = bang[(1,2)]/py2
print("P(X=1|Y=2)=",p12)
# Xác định hàm phân phối xác suất đồng thời của X và Y
print("Ta co ham phan phoi xac suat dong thoi của X va Y")
# x <1 , y<1
Fxy = 0
print(" x <1 , y<1=",Fxy)
#1<=x<2 , 1<=y<2  
Fxy1 = bang[(1,1)]
print("1<=x<2,1<=y<2=",Fxy1)
#2<=x<3,1<=1<2 
Fxy2 = bang[(1,1)]+bang[(2,1)]
print("2<=x<3,1<=1<2=",Fxy2)
#x>3 , 1<=y<2 
Fxy3 = bang[(1,1)]+bang[(2,1)]+bang[(3,1)]
print("x>3 , 1<=y<2 =",Fxy3)
#1<=x<2 , y >2 
Fxy4 = bang[(1,1)]+bang[(1,2)]
print("1<=x<2 , y >2 =",Fxy4)
#2<=x<3,y>2 
Fxy5 = bang[(1,1)]+bang[(2,1)]+bang[(1,2)]+bang[(2,2)]
print("2<=x<3,y>2",Fxy5)
#x>3,y>2
Fxy6 = 1
print("x>3,y>2=",Fxy6)
