# Tính tích phân bằng phương pháp hình học và công thức tích phân
def integrate(f, a, b, n=1000):
    step = (b - a) / n
    total = 0
    for i in range(n):
        total += f(a + i * step) * step
    return total

# Hàm mật độ xác suất
def pdf(x):
    if x <= 2:
        return 0
    elif x <= 3:
        return 2 * (x - 2)
    else:
        return 0

# Kỳ vọng E(X)
def expectation():
    f = lambda x: x * pdf(x)
    return integrate(f, 2, 3)

# Kỳ vọng E(X^2)
def expectation_squared():
    f = lambda x: x**2 * pdf(x)
    return integrate(f, 2, 3)

# Kỳ vọng E[(X - mu)^3]
def expectation_cube(mu):
    f = lambda x: (x - mu)**3 * pdf(x)
    return integrate(f, 2, 3)

# Kỳ vọng E[(X - mu)^4]
def expectation_fourth(mu):
    f = lambda x: (x - mu)**4 * pdf(x)
    return integrate(f, 2, 3)

# Tính toán kỳ vọng và phương sai
mu = expectation()
mu_squared = expectation_squared()
variance = mu_squared - mu**2

# Tính toán hệ số bất đối xứng và hệ số nhọn
skewness = expectation_cube(mu) / variance**1.5
kurtosis = expectation_fourth(mu) / variance**2

# Tìm mode
mode = 3  # Do hàm mật độ xác suất đạt cực đại tại x = 3

# Kết quả
print("Hàm mật độ xác suất (PDF) của X: f(x) = 2(x - 2) trong khoảng 2 < x <= 3")
print("P(1 < X < 1.6) =", 0)
print("Kỳ vọng E(X) =", mu)
print("Phương sai Var(X) =", variance)
print("Mode của X =", mode)
print("Hệ số bất đối xứng (Skewness) =", skewness)
print("Hệ số nhọn (Kurtosis) =", kurtosis)