# โปรแกรมคำนวนค่า BMI
# BMI = น้ำหนัก (KG) / ส่วนสูง*ส่วนสูง (CM)

#input
Weight = int(input ("กรุณาป้อนน้ำหนักของคุณ = "))
Height = int(input ("กรุณาป้อนส่วนสูงของคุณ = "))

#Processing
#แปลง CM เป็น M
Height /= 100  #ใช้วิธีย่อ Compound จาก Height = Height / 100

#Calculate BMI
BMI = Weight / Height**2

#Output
print ("ค่า BMI ของคุณคือ",BMI)

#เขียนแบบย่อโดยใช้ Code ดังนี้***

# Weight = int(input("กรุณาใส่น้ำหนักของคุณ (Kg)"))
# Height = int(input("กรุณาใส่ส่วนสูงของคุณ (Cm)")) / 100 # ใส่ตัวหารไปเลย
# print ("ค่า BMI ของคุณคือ ",Weight / Height**2)

