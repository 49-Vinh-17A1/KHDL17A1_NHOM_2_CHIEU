import math
EX = 5
EX_X_minus_1 = 27.5
EX_square = EX_X_minus_1 + EX
VX = EX_square - EX**2
sigmaX = math.sqrt(VX)
print("Phương sai V(X):", VX)
print("Độ lệch chuẩn σ(X):", sigmaX)