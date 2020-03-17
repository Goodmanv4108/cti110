#Asking for the color from the user to input into python to make the secondary color.
color1 = (input('Enter your first color(red, blue or yellow): '))

color2 = (input('Enter your second color(red, blue or yellow): '))

#Comparing the choices
#Mixing Purple
if color1 == "red" and color2 == "blue":
    print ("You mixed purple.")
    
elif    color1 == "blue" and color2 == "red":
        print ("You mixed purple.")
#
#mixing orange
elif    color1 == "red" and color2 == "yellow":
        print ("You mixed orange.")
        
elif    color1 == "yellow" and color2 == "red":
        print ("You mixed orange.")
#
#mixing green
elif    color1 == "blue" and color2 == "yellow":
        print ("You mixed green.")
        
elif    color1 == "Yellow" and color2 == "blue":
        print ("You mixed green.")
#
#If you choose another color it will show an error and that they need to choose one of the three colors.
else:
    print ("Error. Choose red, yellow or blue only.")






