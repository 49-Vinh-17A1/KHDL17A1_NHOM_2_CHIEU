# tính xác suất đỗ cả 3 vòng
p1 = 0.8
p2 = 0.6
p3 = 0.55
dc3v = p1*p2*p3
print("xac xuat do ca 3 vong",dc3v)
# bảng ppxs cho so vòng thi đỗ
def tính_sxdoi(p1):
    return 1-p1

def tính_sxdoi(p2):

    return 1-p2

def tính_sxdoi(p3):
    return 1-p3
for i in range (0,4):
    if i == 0:
        sxovld = tính_sxdoi(p1)*tính_sxdoi(p2)*tính_sxdoi(p3)# xác xuất 0 vào nào đỗ
        
    elif  i == 1:
       sx1vd = (p1*tính_sxdoi(p2)*tính_sxdoi(p3))+(tính_sxdoi(p1)*p2*tính_sxdoi(p3))+(tính_sxdoi(p1)*tính_sxdoi(p2)*p3)
       
    elif i == 2:
        sxd2ld = (p1*p2*tính_sxdoi(p3)) + (tính_sxdoi(p1)*p2*p3) +(p1*tính_sxdoi(p2)*p3)
    else:
        sxd3v = p1*p2*p3
print(sxovld,sx1vd,sxd2ld,sxd3v)  

# tính kì vọng 
X = [0,1,2,3]
P = [sxovld,sx1vd,sxd2ld,sxd3v]
KV=0
for i in X:
    KV+= i*P[i]
print("Ki vong la", KV)
# tinh  phuong sai
PS=0
for i in X:
    PS+= (i**2)*P[i]
V= PS-(KV**2)
print(" phuong sai la",V)
