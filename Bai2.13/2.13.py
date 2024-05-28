#giải phương trình kỳ vọng để biểu diễn x2 qua x1
def solve_expectation(x1, expected_value=2.6, p1=0.2, p2=0.8):
    return (expected_value - p1 * x1) / p2

#Kiểm tra phương trình phương sai
def check_variance(x1, x2, variance=0.64, expected_value=2.6, p1=0.2, p2=0.8):
    E_X2 = p1 * x1**2 + p2 * x2**2
    var_X = E_X2 - expected_value**2
    return abs(var_X - variance) < 1e-6

#Tìm x1 và x2 thỏa mãn cả hai phương trình
def find_solution():
    for x1 in range(-100, 101):  # Thử các giá trị trong khoảng -100 đến 100
        x1 = x1 / 10.0  # Chuyển đổi thành số thập phân
        x2 = solve_expectation(x1)
        if check_variance(x1, x2):
            return x1, x2
    return None, None

x1, x2 = find_solution()
print(f"x1 = {x1}, x2 = {x2}")