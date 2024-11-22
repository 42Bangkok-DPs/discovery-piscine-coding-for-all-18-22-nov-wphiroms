#!/usr/bin/env python3

def display_multiplication_table(start=1, end=10):
    """สร้างและแสดงตารางการคูณ"""
    for i in range(1, 11):  # แถว (ตัวคูณ)
        for j in range(1, 11):  # คอลัมน์ (ตัวตั้ง)
            print(f"{j} x {i:2} = {j*i:2}", end="   ")
        print()  # แสดงบรรทัดใหม่หลังจากแต่ละแถว
    print("\nตารางการคูณแสดงผลสำเร็จ!")

if __name__ == "__main__":
    print("=== ตารางการคูณ ===\n")
    display_multiplication_table()
