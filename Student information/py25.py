from pymysql import *

def calculate_average(total_marks, num_subjects):
    return total_marks / num_subjects
    
def add():
    try:
        con=connect(host="localhost",user="root",password="Kaleesh",database="sinfo")
        sid=int(input("Enter the student I'd :"))
        sname=input("Enter the student name :")
        smark=int(input("Enter the Total mark :"))
        num_subjects = int(input("Enter the number of subjects: "))
        
        savg=calculate_average(smark,num_subjects)
        q="insert into staff values('{0}','{1}','{2}','{3}')".format(sid,sname,savg,smark)
        c=con.cursor()
        c.execute(q)
        con.commit()
        print("data inserted")
        con.close()
    except Exception as e:
        print("Upload Error")
        
def view():
    try:
        con=connect(host="localhost",user="root",password="Kaleesh",database="sinfo")
        q="select * from staff"
        c=con.cursor()
        c.execute(q)
        a=c.fetchall()
        print("Id \t Name \t Average \t Mark ")
        for i in a:
            for j in i:
                print(j,end="\t")
            print("")
        con.close()
    except Exception as e:
        print("Check Error")
        
        
def update():
    try:
        con=connect(host="localhost",user="root",password="Kaleesh",database="sinfo")
        sid=int(input("Enter the student I'd to update :"))
        savg=float(input("Enter new Average :"))
        q="update staff set avg='{0}' where id='{1}'".format(savg,sid)
        c=con.cursor()
        res=c.execute(q)
        con.commit()
        print("Data Updated Successfully" if res != 0 else "Update Failed")
        con.close()
    except Exception as e:
        print("Update Error")    
        

def delete():
    try:
        con=connect(host="localhost",user="root",password="Kaleesh",database="sinfo")
        sid=int(input("Enter the Id :"))
        q="delete from staff where id='{0}'".format(sid)
        c=con.cursor()
        res=c.execute(q)
        con.commit()
        print("Data Deleted" if res != 0 else "Data Failed")
        con.close()
    except Exception as e:
        print("Delete Error")     
    
    
while True:
    print("-------Welcome-------")
    print("1.Add Data")
    print("2.View Data")
    print("3.Update Data")
    print("4.Delete Data")
    print("5.Exit")
    print("----------------------")
    opt=int(input("Select a Option :"))
    if opt==1:
        add()
    elif opt==2:
        view()
    elif opt==3:
        update()
    elif opt==4:
        delete()
    elif opt==5:
        print("Thank You")
        break
    print("-----------------------------------------------------------------")
    



