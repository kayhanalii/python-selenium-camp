studentList = []
name_lastname = input("lütfen bir isim ve soyisim giriniz : ")


def studentAdd():
    studentList.append(name_lastname)
    print(f"{studentList} Eklendi.")
studentAdd()


name_lastname = input("lütfen bir isim ve soyisim giriniz : ")

def studentDelete():
    print(f"{studentList} Silindi.")
    studentList.remove(name_lastname)

studentDelete()

def studentAllAdd():
    number = int(input("Kaç kişi eklemek istiyorsunuz: "))
    names=[]
    for i in range(number):
        name_lastname = input("Eklemek istediğiniz isim ve soyismi giriniz: ")
        names.append(name_lastname)
        print(f"{name_lastname} Eklendi.")
    studentList.extend(names)

studentAllAdd()

def listOfStudent():
    print("Öğrenciler yazdırılıyor.")
    for name_lastname in studentList:
        print(name_lastname)

listOfStudent()

def studentNumber():
    name_lastname=input("lütfen bir isim ve soyisim giriniz: ")
    if name_lastname in studentList:
        number = studentList.index(name_lastname)
        print(number)
    else:
        print("Böyle bir isim ve soyisim bulunamadı.")

studentNumber()

def studentAllDelete():
    number=int(input("Silmek istediğiniz öğrenci sayısı: "))
    i=0
    while i<number:
        studentList.remove(studentList[i])
        i+=1
studentAllDelete()
print(studentList)

