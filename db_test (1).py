import pymysql #library for sqlite database connection and querries
import sys # library for exit method

con= pymysql.connect(host="localhost",user="root",password="",database="db_test")#for creating database if do not exist and connecting to database
db=con.cursor()
#db.execute("drop table contact")

while(True):
    data=input("What do you want to do?\n1)Insertion\n2)Updation\n3)Deletion\n4)View Stored Data\n5)Exit\nEnter Choice : ")

    if data=='1':#for insertion
        x=int(input("Enter the no of employee : "))

        for i in range(x):
            print("-"*30)
            Id=int(input("Enter Id : "))
            name=input("Enter Name :")
            phone=int(input("Enter Phone No. : "))
            email=input("Enter Email :")
            print("-"*30)

            db.execute("create table if not exists contact(id integer,name text,phone integer,email text)")#to execute create table querry( * if not exist:- is used to create table if table do not exist ) 
            db.execute("insert into contact values(?,?,?,?)",(Id,name,phone,email))#to execute details insert querry
            db.commit()

        print("\n\nInserted Data is\n")

    elif data=='2':#for updation
        up=input("Do you want to Update some thing? :\n1)Yes\n2)No\nEnter Choice : ")
        if up=='1':
            uid=int(input("Enter Id of Employee to change : "))
            upd=input("What do you want to Update? :\n1)Name\n2)Phone No\n3)Email\nEnter Choice : ")
            if upd=='1':
                uname=input("Enter New Name : ")
                db.execute("update contact set name=? where contact.id=?",(uname,uid))
            elif upd=='2':
                uphone=input("Enter New Phone No. : ")
                db.execute("update contact set phone=? where contact.id=?",(uphone,uid))
            elif upd=='3':
                uemail=input("Enter New Email : ")
                db.execute("update contact set email=? where contact.id=?",(uemail,uid))
            else:
                print("Wrong Input !!!")
                continue
            db.commit()
            print("\n\nData after Updation\n")
            
        elif up=='2':
            continue
        else:
            print("Invalid Input !!!")
            continue

            
    elif data=='3':#for deletion
        delt=input("Do you want to Delete something? :\n1)Yes\n2)No\nEnter Choice : ")
        if delt=='1':
            de=int(input("Enter id to delte the Contact : "))
            db.execute("delete from contact where id=?",(de,))
            db.commit()
        elif delt=='2':
            continue
        else:
            print("Wrong Input !!!")
            continue

        print("\n\nData after Deleting\n")

    elif data=='4':#for View table Data
        print("\n\n")
        for a,b,c,d in db.execute("select * from contact"):#inserting data of single cell into a variable
            print("-"*30)
            print("|"," "*5,"Id | ",a)
            print("|"," "*3,"Name | ",b)
            print("| ""Phone No | ",c)
            print("|"," "*2,"Emial | ",d)
            print("-"*30)
        print("\n\n")
        continue
        

    elif data=='5':#for exit
        print("Thank You")
        sys.exit()
    else:
        print("\nWrong input!!\n")
        continue
        
    #for displaying the data after operation

    for a,b,c,d in db.execute("select * from contact"):#inserting data of single cell into a variable
            print("-"*30)
            print("|"," "*5,"Id | ",a)
            print("|"," "*3,"Name | ",b)
            print("| ""Phone No | ",c)
            print("|"," "*2,"Emial | ",d)
            print("-"*30)

#for permanently storing data in database commit method is used
#db.commit() 

db.close()#for closing the connection of database


