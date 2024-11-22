#!/usr/bin/env python3

# รหัสผ่านที่ต้องตรวจสอบ
password = "Python is awesome"

# ขอให้ผู้ใช้ป้อนรหัสผ่าน
user_input = input("Enter the password: ")

# ตรวจสอบว่ารหัสผ่านตรงกันหรือไม่
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
