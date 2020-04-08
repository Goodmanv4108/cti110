#CTI-110
#P4HW2 - BasicMath
#Veronica Goodman
#3/12/2020
#

ans=True
while ans:
    #Number One Choice
    Number1 = int(input('Enter your first number: '))
    #Number Two Choice
    Number2 = int(input('Enter your second number: '))

#The sum of the two numbers added, multiplied, and subtration
    add_sum = Number1 + Number2
    multi_sum = Number1 * Number2
    sub_sum = Number1 - Number2
    #Printing the menu
    print ("""
    1.Add Numbers
    2.Multiply Numbers
    3.Subtract Numbers
    4.Exit/Quit
    """)
    #Choosing what to do to the numbers. Add them, Multiply them or subtract them.
    ans=input("Enter your choice: ") 
    if ans=="1": 
      print("\n The numbers added together equals:" , add_sum) 
    elif ans=="2":
      print("\n The numbers multiplied equals:" , multi_sum) 
    elif ans=="3":
      print("\n The numbers subtracted equals:" , sub_sum) 
    elif ans=="4":
      print("\n Exit")
    elif ans !="":
      #Telling the user to choose a proper option
      ans=input("Enter your choice from the menu(1-4):" )
    if ans=="1": 
      print("\n The numbers added together equals:" , add_sum) 
    elif ans=="2":
      print("\n The numbers multiplied equals:" , multi_sum)   
    elif ans=="3":
      print("\n The numbers subtracted equals:" , sub_sum) 
    elif ans=="4":
      print("\n Exit")
    elif ans !="":
        #Telling the user to choose a proper option
      ans=input("Enter your choice from the menu(1-4):" )
