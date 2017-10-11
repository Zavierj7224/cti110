#CTI 110
#M3Hw2 - Software Sales
#Zavier Jones
#October 10th 2017
# Calculating users purchases with discounts

userNumberOfPackages = int(input("Please enter the number of pac" + \
                                 "kages bought: ") )

#Calculating the discounts
packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0;
elif userNumberOfPackages < 20:
    discount = 0.10
elif userNumberOfPackages < 50:
    discount = 0.20
elif userNumberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40


#Getting the total
subTotal = userNumberOfPackages * packagePrice

discountAmount = discount * subTotal

total =subTotal - discountAmount

print( "Amount of discount: $" + format(discountAmount, ",.3f" ) + \
       "\nTotal amount: $" + format( total, ",.2f"))


