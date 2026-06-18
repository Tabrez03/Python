li=[]

print("Welcome to our Programme !")

while True:
    print('''\nSelect your choice
    Enter 1 to create an array
    Enter 2 to read an array
    Enter 3 to delete an element of an array
    Enter 4 to update an element of an array
    Enter 0 to exit !\n''')

    choice = int(input("Enter your choice :"))
    if choice==1:
        num = int(input("Enter how many element you want to add :"))
        for i in range(num):
            a = int(input(f"Enter the element no. {i+1 } =>"))
            li.append(a)

        print("\nArray is created !")

    elif choice==2:
        print()
        for i in li:
            print(i , end=" ")
        print()

    elif choice==3:
        idx = int(input("Enter the index to remove the element :"))
        if idx>=0 and idx<len(li):
            li.pop(idx)
            print("\n Element removed !")
        else:
            print("\n Invalid index !")

    elif choice ==4:
        idx = int(input("Enter the index you want to upadte :"))
        val = int(input("Enter the new value :"))
        if idx>=0 and idx<len(li):
            li[idx] = val
            print("\nElement update !")
        else:
            print("\n Invalid index !")
    elif choice==0:
        print("\n Thank you !")
        break

    else:
        print("\n Invalid choice !")

        