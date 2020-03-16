#CTI-110
#P3HW2 - BasicMath
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
      print("\n Added Numbers" , add_sum) 
    elif ans=="2":
      print("\n Multiplied Numbers" , muilti_sum) 
    elif ans=="3":
      print("\n Subtracted Numbers" , sub_sum) 
    elif ans=="4":
      print("\n Exit")
    elif ans !="":
      print("\n Not Valid Choice Try again")
      #end of code
