# Add/Subtract Calculator
# Dan Schellenberg
# May 16, 2022

# figure out which operation to do
operation = input("Do you want to add or subtract? ")

if operation == "add":
    #take user input
    first = input("What's the first number? ")
    second = input("What's the second number? ")
    
    #convert data types
    first = int(first)
    second = int(second)
    
    #do the math
    answer = first + second
    
    #output
    print("The sum will be " + str(answer))
    
elif operation == "subtract":
    #take user input
    first = input("What's the first number? ")
    second = input("What's the second number? ")
    
    #convert data types
    first = int(first)
    second = int(second)
    
    #do the math
    answer = first - second
    
    #output
    print("The difference will be " + str(answer))

else:
    print("That wasn't an option!")