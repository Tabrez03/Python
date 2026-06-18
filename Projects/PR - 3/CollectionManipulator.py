print("Welcome to the student data organizer!")

Students = []

while True:

    print('''\nSelect an Option:
          1. Add Student
          2. Display All Studens
          3. Update Student Information
          4. Delete Student
          5. Display Subject Offered
          6. Exit\n''')
    
    choice = int(input("Enter your choice :"))

    if choice == 1:
        st = {
            "Id" : len(Students)+1,
            "Name" : input("Enter student name: "),
            "Age" : int(input("Enter student age :")),
            "Grade" : input("Enter student grade :"),
            "Date of Birth" : input("Enter student birthdate(YYYY-MM-DD) :"),
            "Subjects" : set(input("Enter student subjects (comma-separated):").split(","))
        }
    
        Students.append(st)

        print("\nStudent added successfully !\n")
    
    elif choice == 2:
        for st in Students:
            print(f"Id :{st["Id"]} | Name :{st["Name"]} | Age :{st["Age"]} | Grade :{st["Grade"]} | Date of Birth :{st["Date of Birth"]} | Subject :{", ".join(st["Subjects"])}")
    
    elif choice ==3:

        stid = int(input("Enter student id to update :"))
        found = False

        for st in Students:
            if st["Id"]==stid:
                found = True
                st["Name"]=input("Enter student updated name: ")
                st["Age"]=int(input("Enter student updated age :"))
                st["Grade"]=input("Enter student updated grade :")
                st["Date of Birth"]=input("Enter student updated birthdate(YYYY-MM-DD) :")
                st["Subjects"]= set(input("Enter student updated subjects (comma-separated):").split(","))
                print("\nStudent Updated Successfully !")

        if found==False:
            print("Student not found !")

    elif choice == 4:

        stid = int(input("Enter student id to delete :"))
        found = False

        for st in Students:
            if st["Id"]==stid:
                found = True
                Students.remove(st)
                print("Student Deleted Successfully !")

        if found==False:
            print("Student not found !")
            
    elif choice == 5:
        all_sub=set()
        for st in Students:
            all_sub.update(st["Subjects"])
        if all_sub:
            print("\nUnique Subjects Available:", ", ".join(all_sub))
        else:
            print("\nNo student records found to extract subjects!")

    elif choice==6:
        print("Thank you !")
        break
