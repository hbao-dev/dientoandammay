import cmath

def giai_phuong_trinh_bac_nhat(a, b):
    
    if a == 0:
        raise ValueError("Hệ số 'a' không thể bằng không cho phương trình bậc nhất.")
    x = -b / a
    return x

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("Phương trình không có nghiệm thực.")
    x1 = (-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)
    return x1, x2

# Ví dụ sử dụng
if __name__ == "__main__":
    try:
        # Nhập hệ số a và b từ bàn phím
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))

        # Giải phương trình bậc nhất
        x_bac_nhat = giai_phuong_trinh_bac_nhat(a, b)
        print(f"Phương trình bậc nhất: {a}x + {b} = 0")
        print(f"Giải: x = {x_bac_nhat:.2f}")

        print("---------------------------")
        # Nhập hệ số c từ bàn phím
        c = float(input("Nhập hệ số c: "))

        # Giải phương trình bậc hai
        x1, x2 = giai_phuong_trinh_bac_hai(a, b, c)
        print(f"Phương trình bậc hai: {a}x^2 + {b}x + {c} = 0")
        print(f"Nghiệm: x1 = {x1:.2f}, x2 = {x2:.2f}")
    except ValueError as e:
        print(f"Lỗi: {e}")
