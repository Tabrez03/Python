print("\nWelcome to the Pattern Generator and number Analyzer!\n")

while True:
    print("\nSelect an Option:\n")
    print("1. Genrate a pattern:\n")
    print("2. Analyze a Rnage of Numbers:\n")
    print("3. Exit:\n")

    choice = int(input("Enter your choice :"))

    match choice:

        case 1:
                num=int(input("Enter the number of rows you want to draw:"))
                for i in range(1,num+1):
                    for j in range(1,i+1):
                        print("*",end=" ")
                    print("")   
        
        case 2:
                sum=0
                start =int(input("Enter the start of the range :"))
                end =int(input("Enter the end of the range :"))

                for i in range(start,end+1):
                     if i%2==0:
                          print(f"The number {i} is even.")
                     else:
                          print(f"The number {i} is odd.")
                     sum=sum+i
                print(f"The sum of number is:",sum)      
        case 3:
            break            





         