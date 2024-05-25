import math
def integrate_rectangular(f, a, b, n):
    delta_x = (b - a) / n
    integral = 0
    for i in range(n):
        x_left = a + i * delta_x
        x_right = a + (i + 1) * delta_x
        integral += f((x_left + x_right) / 2) * delta_x
    return integral
# X ~ N(2.2, 0.4**2) and Y~N(2.5,0.6**2)
# a) Gọi T là tổng số thời gian học và thời gian chơi
# T = X + Y => E(T) = E(x + Y) = E(X) + E(Y)
# V(T) = V(X) + V(Y) + 2COV(X,Y)
# COV(X,Y) = p(X,Y)*Ox*Oy
ET = 2.2 + 2.5
COV = -0.5*0.4*0.6
VT = 0.4**2 + 0.6**2 +2*COV
OT = math.sqrt(VT)
# T~N(E(T),V(T)) 
# xác suất P(T>5) là:
PT1=1/(OT*math.sqrt(2*math.pi))
PT2= integrate_rectangular(lambda x: (math.e)**((-(x-ET)**2)/(2*VT)),0,5,100000)
#P(T>5) = 1 - PT1*PT2
PT= 1 - PT1*PT2
# b)
#  Gợi W là thời gian học lớn hơn thời gian chơi
# P(W) = P(X-Y)
# E(W) = E(X-Y) = E(X) - E(Y)
# V(w) = V(X) + V(Y) - 2COV(X,Y) 
EW = 2.2 - 2.5
VW = 0.4**2 + 0.6**2 - 2*COV
OW = math.sqrt(VW)
# W~N(E(W),V(W))
# xác suất thời gian học lớn hơn thời gian chơi là P(W>0)
PW1 = 1/(OW*math.sqrt(2*math.pi))
PW2 = integrate_rectangular(lambda x: (math.e)**((-(x-EW)**2)/(2*VW)),0,99999,100000)
# P(W>0) = PW1*PW2
PW = PW1*PW2
print("xác suất để tổng số thời gian học và thời gian chơi lớn hơn 5 giờ là:",PT)
print("xác suất thời gian học lớn hơn thời gian chơi là",PW)