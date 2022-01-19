# นายชยุตพงศ์ จำเนียรพงษ์พันธ์ 1620706646 CS441 - Algorithms

# นำเข้า library
import random

# สร้างตัวแปรความยาวของ array = 10000
length_array = 10000

# สร้างตัวแปร array เปล่าๆ ไว้เก็บตัวเลขทีทำการสุ่ม
random_numlst = []

# วนลูป length_array ทั้งหมด 10000 ครั้ง
for i in range(0, length_array):

    # สร้างตัวแปรเก็บตัวเลขที่สุ่ม ตั้งแต่เลข 1 - 1000
    item = random.randint(1,1000)

    # เพิ่มตัวเลขที่สุ่มไว้ใน mylist
    random_numlst.append(item)

# สร้างไฟล์ txt 
# แปลงจาก int เป็น str
random_numlst = str(random_numlst)
f = open("Input1000.txt","w") 
f.write(random_numlst)

# เนื่องจากการอ่านไฟล์ เราต้องแปลงกลับไปเป็น array ก่อน
# สร้างตัวแปร array เปล่าๆ
array = []
with open('Input1000.txt') as f:

    #ทำการวนลูป จากนั้นทำการแยกสตริงด้วยเครื่องหมายจุลภาคจะทำให้แต่ละตัวเลขแยกกัน
    for number in f.read()[1:-1].split(','):

        # ทำการแปลงเป็น int และเพิ่มลงใน array
        array.append(int(number))

#Bubble sort algorithm
# สร้างฟังก์ชัน BubbleSort รับ array เป็นอากิวเมนต์
def BubbleSort(array):

    # กำหนดความยาวของอาร์เรย์ใน n
    n = len(array)

    # ภายในฟังก์ชัน ได้กำหนดไว้ 2 for loop
    # for loop แรกคือรอบนอกที่รันอัลกอริธึมการเรียงลำดับแบบ BubbleSort (n – 1) ครั้ง
    for i in range(n-1):

        # กำหนดตัวแปรแฟล็กที่จะใช้ในการพิจารณาว่ามีการสลับเกิดขึ้นหรือไม่ ทำเพื่อเพิ่มประสิทธิภาพ
        flag = 0

        # จากนั้น for loop เปรียบเทียบค่าทั้งหมดตั้งแต่ค่าแรกจนถึงค่าสุดท้าย
        for j in range(0, n-i-1):

            # กำหนดเงื่อนไขหากค่า index ตัวแรกมากกว่าค่า index ตัวที่สอง ให้สลับตำแหน่งกัน
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]

                # ตัวแปรแฟล็กถูกกำหนดเป็นค่า 1 เพื่อบอกว่ามีการสลับเกิดขึ้น
                flag = 1

        # ใช้คำสั่ง if เพื่อตรวจสอบว่าค่าของแฟล็กตัวแปรเป็น 0 หรือไม่
        # หากค่าเป็น 0 จะเรียกคำสั่ง break ออกจาก for loop
        if flag == 0:
            break
    
    # ทำการส่งคืน array ที่ทำการ sort เรียบร้อยแล้ว
    return array

# ทำการเรียกฟังก์ชัน BubbleSort เพื่อสร้างไฟล์ Output10000
with open('Output10000.txt', 'w') as f:
    for i in BubbleSort(array):
        f.write(str(i))
        f.write('\n')
