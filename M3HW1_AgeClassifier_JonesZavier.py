#CTI-110
#M3HW1 - Age Classifier
#Zavier Jones
#October 4th 2017
# Classifying Ages

userAge = int(input( "Please enter your age: " ) )

if userAge <= 1:
    print( "You are an infant" )
elif userAge <13:
    print("You are an child" )
elif userAge < 20:
    print(" You are a teenager" )
elif userAge >= 20:
    print("You are an adult" )

