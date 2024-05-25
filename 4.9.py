a = 1 / (3 + 1 + 2 + 2 + 2 + 0 + 1 + 4 + 5)
bang_pp = [[2, 2.5, 4],
           [1, 3*a, a, 2*a],
           [1.5, 2*a, 2*a, 0],
           [2, a, 4*a, 5*a]]
X = [1, 1.5, 2]
PX1 = sum(bang_pp[1][1:])
PX1_5 = sum(bang_pp[2][1:])
PX2 = sum(bang_pp[3][1:])
bang_X = [PX1, PX1_5, PX2]
Y = [2, 2.5, 4]
PY2 = sum(bang_pp[i][1] for i in range(1, len(bang_pp)))
PY2_5 = sum(bang_pp[i][2] for i in range(1, len(bang_pp)))
PY4 = sum(bang_pp[i][3] for i in range(1, len(bang_pp)))
bang_Y = [PY2, PY2_5, PY4]
print("Phân phối xác suất biên của X:", bang_X)
print("Phân phối xác suất biên của Y:", bang_Y)
#P[X|Y]
PX1Y2 = bang_pp[1][1] / PY2
PX1_5Y2 = bang_pp[2][1] / PY2
PX2Y2 = bang_pp[3][1] / PY2
print("P[X=1|Y=2] =", round(PX1Y2, 4))
print("P[X=1.5|Y=2] =", round(PX1_5Y2, 4))
print("P[X=2|Y=2] =", round(PX2Y2, 4))
#P[Y|X]
PY2_X1 = bang_pp[2][1] / PX1
PY2_X1_5 = bang_pp[2][2] / PX1_5
PY2_X2 = bang_pp[2][3] / PX2
print("P[Y=2|X=1] =", round(PY2_X1, 4))
print("P[Y=2|X=1.5] =", round(PY2_X1_5, 4))
print("P[Y=2|X=2] =", round(PY2_X2, 4))