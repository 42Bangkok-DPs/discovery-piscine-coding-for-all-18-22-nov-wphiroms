#!/usr/bin/env python3

# ขอให้ผู้ใช้กรอกหมายเลข
user_input = input("กรุณากรอกหมายเลข: ")

# ตรวจสอบว่าเป็นทศนิยมหรือไม่
try:
    # พยายามแปลงค่าที่กรอกเป็น float
    number = float(user_input)
    
    # ตรวจสอบว่าหมายเลขเป็นทศนิยมหรือไม่
    if '.' in user_input:
        print(f"{user_input} เป็นเลขทศนิยม")
    else:
        print(f"{user_input} ไม่เป็นเลขทศนิยม")
except ValueError:
    # หากไม่สามารถแปลงเป็น float ได้
    print("กรุณากรอกหมายเลขที่ถูกต้อง")
