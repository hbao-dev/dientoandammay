import random

def sinh_day_so(n):
    if(n>100):
        raise ValueError("Lỗi!")
    
    else:
        return [random.randint(0, n) for _ in range(n)]
    
def la_so_nguyen_to(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Nhập số phần tử của dãy số: "))
    day_so = sinh_day_so(n)

    print("Dãy số ngẫu nhiên:")
    print(day_so)

    so_nguyen_to_chia_het_7 = []
    tong_so_le = 0

    for so in day_so:
        if so % 7 == 0 and la_so_nguyen_to(so):
            so_nguyen_to_chia_het_7.append(so)
        if so % 2 != 0:
            tong_so_le += so

    print("Các số nguyên tố chia hết cho 7:")
    print(so_nguyen_to_chia_het_7)

    print(f"Tổng các số lẻ trong dãy: {tong_so_le}")

if __name__ == "__main__":
    main()
