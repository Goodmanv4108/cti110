#This program is changing feet to inches for the user.
#4/20/2020
#CTI-110 P5T2_FeetToInches
#Veronica Goodman
#




#Constant for the number of inches per foot.

INCHES_PER_FOOT = 12

#Main function
def main():
    #Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    #Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

#The feet_to_inches function coverts feet to inches.

def feet_to_inches(feet):
        return feet * INCHES_PER_FOOT

#Call the main function
main()
