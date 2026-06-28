print("Welcome to our program !\n")


Arr =[]
total=0
while True:

    print(''' Select the choice:
          
          1. Enter 1 to add the element in arr :
          2. Enter 2 to see the array element :
          3. Enter 3 to sum of the all element :
          4. Enter 4 to find the largest element in array:
          5. Enter 5 to find smallest element in array:
          6. Enter 6 to find count of odd and even :
          7. Enter 7 to do reverse the all array element :
          8. Enter 8 to check the element is exists or not:
          9. Enter 9 to count frequency of each element :
          10. Enter 10 to exit the program :
            ''')
    
    choice=int(input("Enter your choice :")) 
    

    if choice==1:
        n=int(input("Enter the number of element :"))


        for i in range(n):
            a = int(input(f"Enter the element {i+1} :"))
            Arr.append(a)

        print("Array is created !\n")

    elif choice==2:
        
        print(Arr)

    elif choice==3:
        for i in Arr:
            total +=i
        print(total)   

    elif choice==4:
        largest=Arr[0]
        for i in Arr:
            if i>largest:
                largest=i   
        print(f"The Largest elemet is :{largest}")