# calculator.py

# ขอให้ผู้ใช้กรอกตัวเลขสองตัว
num1 = float(input("กรุณาใส่ตัวเลขตัวแรก: "))
num2 = float(input("กรุณาใส่ตัวเลขตัวที่สอง: "))

# คำนวณและแสดงผลลัพธ์
print(f"ผลลัพธ์การบวก: {num1 + num2}")
print(f"ผลลัพธ์การลบ: {num1 - num2}")
print(f"ผลลัพธ์การคูณ: {num1 * num2}")
if num2 != 0:
    print(f"ผลลัพธ์การหาร: {num1 / num2}")
else:
    print("ไม่สามารถหารด้วยศูนย์ได้")
