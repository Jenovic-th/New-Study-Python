# แปลงอุณหภูมิ
# C = (F-32)x5/9
# F = (Cx9/5)+32

temp = input("ป้อนอุณหภูมิ (องศา) : ") # หากป้อนโดยใส่ C หรือ F เช่น 35c

# ตัวอย่างถ้าต้องการได้แต่ตัวเลข ไม่เอาตัวอักษร
# ตัวแปร 1 = temp[:-1] # ไม่เอาตัวสุดท้าย ก็จะได้ 35
# ตัวแปร 2 = temp[-1]  # เอาตัวท้ายไปใช้งาน ในที่นี้คือ c
# หากต้องใช้ตัวพิมพ์เล็กหรือใหญ่ใช้คำสั่ง .upper()ดัดแปลงได้

#ตัวอย่าง

degree = int(temp[:-1]) # แล้วแต่ค่าที่ใส่ลงมา ไม่เอา C หรือ F
unit = temp[-1].upper()  # แปลงให้เป็นตัวใหญ่ไปเลย
print(degree,"=",unit)

if unit == "C":
    result = (9*degree) / 5 + 32 
    unit_result = "ฟาเรนไฮน์"

if unit == "F":
    result = (degree - 32) * 5 / 9
    unit_result = "เซลเซียส"

print("แปลงค่าอุณหภูมิ = ",temp,"เป็น",unit_result," = ",result)
