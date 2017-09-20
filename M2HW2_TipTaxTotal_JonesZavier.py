#CTI 110
#M2HW2 - TipTaxTotal
#Calculating the cost of a meal I purchased
#Zavier Jones
#September 19th, 2017

#Asking the user to enter the charge for the food
foodCost= float(input("Please enter the charge of the food: ") )

#Calculating the tip and sales tax
tipAmount = 0.18 * foodCost

salesTax = 0.07 * foodCost

#Displaying the total

totalCost = foodCost + tipAmount + salesTax

print("Food Cost: $" + format(foodCost, ",.2f"), "tipAmount: $" + \
      format( tipAmount,",.2f"), "sales Tax: $" + format( salesTax, ",.2f"), \
      "total Cost: $" + format( totalCost, ",.2f")) 
