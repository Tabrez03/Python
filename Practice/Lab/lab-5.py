Student =[]

print ("welcome to Student portal")

while True:
    print('''
    Enter 1 to add student
    Enter 2 to view student
    Enter 3 to delete student
    Enter 4 to update student
    Enter 0 to exit\n''')

    choice = int(input("Enter your choice :"))              

    if choice==1:
        st = {
            "Id" : (len(Student)+1,),
            "Name" :input("Enter student name :"),
            "Subject" : set(input("Enter student subject seprated by comma(,) :").split(","))
        }

        Student.append(st)

        print("\nStudent added successfully !\n")

    elif choice==2:
        for st in Student:
            print(f"Id :{st["Id"][0]} Name : {st["Name"]} Subject :{", ".join(st["Subject"])}")

    elif choice==3:
        stid = int(input("Enter student id to delete :"))
        found = False

        for st in Student:
            if st["Id"]==stid:
                found = True
                Student.remove(st)
                print("Student Deleted Successfully !")

        if found==False:
            print("Student not Found !")

    elif choice==4:

        for st in Student:
            if st["Id"]==stid:
                    found = True
                    st["Name"]= input ("Enter student updated name :")
                    st["Student"]=set(input("Enter student updated subject seprated by comma(,):").split(","))
                    print("Student Updated Successfully !")

        if found==False:
            print("student not found !")

    elif choice==0:
     print("Thank you !")
     break       
            
             
             