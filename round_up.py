#!/usr/bin/env python3
import math

# รับค่าตัวเลขจากผู้ใช้
number = float(input("กรุณากรอกตัวเลข: "))

# ปัดขึ้นเลขนั้น
rounded_number = math.ceil(number)

# แสดงผลลัพธ์
print(f"ตัวเลขที่ปัดขึ้น: {rounded_number}")
