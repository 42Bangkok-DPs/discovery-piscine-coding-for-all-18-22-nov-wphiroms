#!/usr/bin/env python3

def main():
    # ขออายุจากผู้ใช้
    age = int(input("กรุณากรอกอายุของคุณ: "))
    
    # คำนวณอายุใน 10 ปี 20 ปี และ 30 ปี
    age_in_10_years = age + 10
    age_in_20_years = age + 20
    age_in_30_years = age + 30
    
    # แสดงผลลัพธ์
    print(f"ในอีก 10 ปี คุณจะมีอายุ {age_in_10_years} ปี")
    print(f"ในอีก 20 ปี คุณจะมีอายุ {age_in_20_years} ปี")
    print(f"ในอีก 30 ปี คุณจะมีอายุ {age_in_30_years} ปี")

if __name__ == "__main__":
    main()
