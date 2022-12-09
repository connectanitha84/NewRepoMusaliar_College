import mysql.connector
import sys
connection = mysql.connector.connect(host="localhost",user="root",password="Mysql@2022",database="tot_db")
cursor = connection.cursor()
connection.commit()

while(True):
    print('1. add student')
    print('2. view all students')
    print('3. search a student')
    print('4. Delete a student')
    print('5. Exit')
    choice=int(input('Select a choice'))
    if choice ==1:
        name = input('student name?\n')
        rollno=int(input("Roll no"))
        admno=int(input("adm no"))
        sql = "INSERT INTO `tot_db`.`student_table` (`name`, `rollno`,`admission`) VALUES (%s,%s,%s);"
        data = (name,rollno,admno)
        cursor.execute(sql,data)
        print("inserted successfully")
    if choice == 2:
        sql= "SELECT * FROM student_table"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    if choice ==3 :
        admno = input("enter the admission no to be searched")
        sql= "select * from student_table where admission="+admno
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    if choice ==4 :
        admno = input("enter the admission no to be deleted")
        sql= "delete from student_table where admission="+admno
        cursor.execute(sql)
        print("Deleted Successfully")
    if choice ==5 :
        sys.exit(0)
        
connection.close()