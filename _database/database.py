# # # # # # import mysql.connector

# # # # # # mydb = mysql.connector.connect(
# # # # # #     host="localhost",
# # # # # #     user="root",
# # # # # #     password="mysql1234",
# # # # # #     database="mydatabase"
# # # # # # )

# # # # # # mycursor=mydb.cursor()
# # # # # # # # mycursor.execute("CREATE DATABASE mydatabase")
# # # # # # # mycursor.execute("SHOW DATABASES")

# # # # # # # for x in mycursor:
# # # # # # #     print(x)

# # # # # # mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")

# # # # # # # print(mydb)

# # # # # import mysql.connector

# # # # # mydb=mysql.connector.connect(
# # # # #     host="localhost",
# # # # #     user="root",
# # # # #     password="mysql1234",
# # # # #     database= "schooldb"
# # # # # )

# # # # # mycursor=mydb.cursor()

# # # # # mycursor.execute("CREATE DATABASE schooldb")


# # # # import mysql.connector

# # # # def insertProduct():
# # # #     connection=mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
# # # #     cursor=connection.cursor()

# # # #     sql="INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
# # # #     values=("Samsung S2",1000,"1.jpg","iyi telefon")

# # # #     cursor.execute(sql,values)

# # # #     try:
# # # #         connection.commit()
# # # #     except mysql.connector.Error as err:
# # # #         print("hata: ",err)

# # # #     finally:
# # # #         connection.close()
# # # #         print('database bağlantısı kapandı.')

# # # # insertProduct()


# # # import mysql.connector

# # # def insertProduct(name,price,imageUrl,description):
# # #     connection=mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="node-app")
# # #     cursor=connection.cursor()

# # #     sql="INSERT INTO Products(name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
# # #     values=(name,price,imageUrl,description)

# # #     cursor.execute(sql,values)

# # #     try:
# # #         connection.commit()
# # #     except mysql.connector.Error as err:
# # #         print("hata: ",err)

# # #     finally:
# # #         connection.close()
# # #         print('database bağlantısı kapandı.')
# # # def insertProducts(list):
# # #     connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node-app")
# # #     cursor = connection.cursor()

# # #     sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
# # #     values = list

# # #     cursor.executemany(sql,values)

# # #     try:
# # #         connection.commit()   
# # #         print(f'{cursor.rowcount} tane kayıt eklendi')
# # #         print(f'son eklenen kaydın id: {cursor.lastrowid}')
# # #     except mysql.connector.Error as err:
# # #         print('hata:', err)
# # #     finally:
# # #         connection.close()
# # #         print('database bağlantısı kapandı.')

# # # list=[]
# # # while True:

# # #     name = input('ürün adı: ')
# # #     price = float(input('ürün fiyatı: '))
# # #     imageUrl = input('ürün resim adı: ')
# # #     description = input('ürün açıklaması: ')
    
# # #     list.append((name,price,imageUrl,description))

# # #     result=input("devam etmek istiyor musunuz? (e/h)")
# # #     if result =='h':
# # #         print("kayıtlarınız veritabanına aktarılıyor...")
# # #         print(list)
# # #         insertProducts(list)
# # #         break

# # # # insertProduct(name,price,imageUrl,description)

# # import mysql.connector
# # from datetime import datetime
# # from connection import connection


# # class Student:
# #     connection=connection
# #     mycursor=connection.cursor()

# #     def __init__(self,studentNumber,name,surname,birthdate,gender):
# #         self.studentNumber = studentNumber
# #         self.name = name
# #         self.surname = surname
# #         self.birthdate = birthdate
# #         self.gender = gender
    
# #     def saveStudent(self):
# #         sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
# #         value = (self.studentNumber,self.name, self.surname,self.birthdate,self.gender)
# #         Student.mycursor.execute(sql,value)
        
# #         try:
# #             Student.connection.commit()
# #             print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
# #         except mysql.connector.Error as err:
# #             print('hata:', err)
# #         finally:
# #             Student.connection.close()
# #     @staticmethod
# #     def saveStudents(students):
# #         sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
# #         values = students
# #         Student.mycursor.executemany(sql,values)
        
# #         try:
# #             Student.connection.commit()
# #             print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
# #         except mysql.connector.Error as err:
# #             print('hata:', err)
# #         finally:
# #             Student.connection.close()

# # # ahmet = Student("202","ahmet","yılmaz",datetime(2005, 5, 17),"E")
# # # ahmet.saveStudent()

# # ogrenciler = [
# #     ("401","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
# #     ("402","Ali","Can",datetime(2005, 6, 17),"E"),
# #     ("403","Canan","Tan",datetime(2005, 7, 7),"K"),
# #     ("404","Ayşe","Taner",datetime(2005, 9, 23),"K"),
# #     ("405","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
# #     ("406","Ali","Cenk",datetime(2003, 8, 25),"E")
# # ]
# # Student.saveStudents(ogrenciler)

# import mysql.connector

# def insertProduct(name, price, imageUrl, description):
#     connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
#     cursor = connection.cursor()

#     sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
#     values = (name,price,imageUrl,description)

#     cursor.execute(sql,values)

#     try:
#         connection.commit()   
#         print(f'{cursor.rowcount} tane kayıt eklendi')
#         print(f'son eklenen kaydın id: {cursor.lastrowid}')
#     except mysql.connector.Error as err:
#         print('hata:', err)
#     finally:
#         connection.close()
#         print('database bağlantısı kapandı.')

# def insertProducts(list):
#     connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
#     cursor = connection.cursor()

#     sql = "INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" 
#     values = list

#     cursor.executemany(sql,values)

#     try:
#         connection.commit()   
#         print(f'{cursor.rowcount} tane kayıt eklendi')
#         print(f'son eklenen kaydın id: {cursor.lastrowid}')
#     except mysql.connector.Error as err:
#         print('hata:', err)
#     finally:
#         connection.close()
#         print('database bağlantısı kapandı.')

# def getProducts():
#     connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
#     cursor = connection.cursor()

#     cursor.execute("Select * From Products Order By name, price")

#     try:
#         result = cursor.fetchall()    
#         for product in result:
#             print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
#     except mysql.connector.Error as err:
#         print('hata:', err)
#     finally:
#         connection.close()
#         print('database bağlantısı kapandı.')
    
# def getProductById(id):
#     connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node_app")
#     cursor = connection.cursor()

#     sql = "Select * From Products Where id=%s"
#     params = (id,)

#     cursor.execute(sql,params)

#     result = cursor.fetchone()    

#     print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

# def getProductInfo():
#     connection = mysql.connector.connect(host="localhost", user = "root", password="mysql1234", database="node-app")
#     cursor = connection.cursor()

#     sql = "Select COUNT(*) from Products"
#     # sql = "Select AVG(Price) from Products"
#     # sql = "Select SUM(Price) from Products"
#     # sql = "Select MIN(Price) from Products"
#     # sql = "Select MAX(Price) from Products"
#     sql = "Select Name,Price from Products Where Price = (Select MAX(Price) from Products)"

#     cursor.execute(sql)

#     result = cursor.fetchone()    

#     print(f'result: {result[0]} {result[1]}')

#     # print(f'result: {result[0]}')

# getProductInfo()





import mysql.connector
from datetime import datetime
from connection import connection


class Student:
    connection=connection
    mycursor=connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name, self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)
        
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err)
        finally:
            Student.connection.close()

# ahmet = Student("202","ahmet","yılmaz",datetime(2005, 5, 17),"E")
# ahmet.saveStudent()

# ogrenciler = [
#     ("401","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
#     ("402","Ali","Can",datetime(2005, 6, 17),"E"),
#     ("403","Canan","Tan",datetime(2005, 7, 7),"K"),
#     ("404","Ayşe","Taner",datetime(2005, 9, 23),"K"),
#     ("405","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
#     ("406","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]
# Student.saveStudents(ogrenciler)
    @staticmethod
    def StudentInfo():
        sql = "select * from student"
        # sql = "select * from student LIMIT 3"
        # sql = "select studentnumber,name,surname from student"
        # sql = "select name,surname from student where gender='K'"
        # sql = "select * from student where YEAR(birthdate) = 2003"
        # sql = "select * from student where YEAR(birthdate) = 2005 and name = 'Ali'"
        # sql = "select * from student where name like '%an%' or surname like '%an%'"
        # sql = "select COUNT(id) from student where gender='E'"
        # sql = "select name,surname from student where gender='K' order by name,surname"

        Student.mycursor.execute(sql)

        try:
            results = Student.mycursor.fetchall()
            for result in results:
                print(f'{result}')

        except mysql.connector.Error as err:
            print('hata', err)
        finally:
            Student.connection.close()

# Student.StudentInfo()
    @staticmethod
    def getStudentById(id):
        
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
            # return Student.mycursor.fetchone()
        except mysql.connector.Error as err:
            print('Error', err)
        


    def updateStudent(self):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err) 

# student=Student.getStudentById(7)
# # student=Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
# student.name="cınarr"
# student.surname="turam"

# student.updateStudent()
# print(student)

    @staticmethod
    def updateStudents(liste):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('Hata:',err)

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)

students = Student.getStudentsGender('E')
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]  
    liste.append(std)

Student.updateStudents(liste)