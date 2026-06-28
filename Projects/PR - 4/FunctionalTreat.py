Arr=[]

print("Welcome to the Data Analyzer and Transformer Program\n")

#Summery

def summery(Arr):
     count =len(Arr)
     maximum = max(Arr)
     minimum = min(Arr)
     Total =sum(Arr)
     average = sum(Arr)/len(Arr)

     return count,maximum,minimum,Total,average

# factorial
def factorial(n):
     if n<=1:
          return 1
     else :
         return n * factorial(n-1)

# filter
def fil(m):

     new_l=list(filter(lambda x : x>=m,Arr))
     print(f"Filter Data (valuse >={m} ):",new_l) 

#sorting
def sort_Arr(Arr):
    global sorting,r_sorting
    sorting=sorted(Arr)
    r_sorting=sorted(Arr,reverse=True)

#return multi value

def multi_val(Arr):
     maximum_value = max(Arr)
     minimum_value = min(Arr)
     Total_value =sum(Arr)
     average_value = sum(Arr)/len(Arr)

     return maximum_value,minimum_value,Total_value,average_value


while True:

    print('''
          1. Input data 
          2. Display data summery
          3. Calculate factorial
          4. Filter data by Threshold
          5. sort data
          6. Display dataset Statistics
          7. Exit Program \n''')
    
    choice=int(input("Please enter your choice :"))

    if choice==1:
            Arr = [int(i) for i in input(f"Enter data for a 1D array :").split(" ")]
        
            print("\nData has been stored successfully!\n")

    elif choice==2:
          count,maximum,minimum,Total,average = summery(Arr)
          print (f'''\n Total Elements :{count}
                        Maximum value :{maximum}
                        Minimum value :{minimum}
                        Sum of all value :{Total}
                        Average value :{average}''')
     #    count =len(Arr)
     #    print("Tatal Emlements :",count)

     #    maximum = max(Arr)

     #    print("\nMaximum value :",maximum)

     #    minimum = min(Arr)

     #    print("\nMinimum value:",minimum)

     #    Total =sum(Arr)

     #    print("\nSum of all value :",Total)

     #    average = sum(Arr)/len(Arr)

     #    print("\nAverage Value:",average)

    elif choice ==3:
         
         n =int(input("Enter a number to calculate it's factorial :"))
         print(f"The factorial of {n} is :",factorial(n))

    elif choice ==4:
         
        m = int(input("Enter the Threshold value to filter out data above this value :"))
        

        fil(m)
    elif choice==5:
         sort_Arr(Arr)
         print(''' Chose sorting option
               1. Ascending
               2. descending\n''')
         
         subchoice=int(input("Please enter your sub choice :"))

         if subchoice==1:
              print("sorted data in ascending order :",sorting)
         elif subchoice==2:
              print("sorted data in descending oder :",r_sorting)
     
    elif choice ==6:
         if not Arr:
              print("\n Please enter the element first\n")

         else:
             maximum_value,minimum_value,Total_value,average_value = multi_val(Arr)

             print(f'''\n Dataset Statistics:
                   > Maximum value :{maximum_value}
                   > Minimum value :{minimum_value}
                   > Sum of all value :{Total_value}
                   > Average value :{average_value}''')
             
    elif choice ==7:
         print("\n Thank you for using the  Data Analyzer and Transformer Program. Goodbye !")
         break
    