# รับค่าจากผู้ใช้
try:
    number = int(input("กรุณาป้อนตัวเลขสำหรับตารางสูตรคูณ: "))
    
    # แสดงตารางสูตรคูณ
    print(f"\nตารางสูตรคูณของ {number}:")
    for i in range(1, 13):  # ใช้ range 1 ถึง 12
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("กรุณาป้อนตัวเลขที่ถูกต้อง!")
