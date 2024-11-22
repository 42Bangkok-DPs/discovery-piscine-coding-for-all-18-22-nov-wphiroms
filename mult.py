# mult.py
def main():
    try:
        # รับตัวเลข 2 ตัวจากผู้ใช้
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # คำนวณผลลัพธ์ของการคูณ
        result = num1 * num2
        
        # ตรวจสอบว่าผลลัพธ์เป็นบวก ลบ หรือศูนย์
        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")
        else:
            print("The result is zero.")
        
        # แสดงผลลัพธ์การคูณ
        print(f"The result of multiplication is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
