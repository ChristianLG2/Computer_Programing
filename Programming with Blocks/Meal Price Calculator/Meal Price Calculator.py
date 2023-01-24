# Fall 2021 / Revised Winter 2023 - Christian Lira
# This code contains basic mathematical operations that provide the opportunity to get the final price of a product, a meal in this case. Calculating the price per person and the taxes. 
print("")
#first we get the for the items or services provided (meal for this case).
ChildrenMeal = float (input("What is the children meal price? "))
AdultMeal = float (input("What is the Adult meal price? "))
# Second we get the number of items (people for this case) and their own description exp. "Children"
ChildrenCount = int (input("How Many Kids ate? "))
AdultCount = int (input("How Many Adults ate? "))
Tax = float (input("What is the tax rate? "))
print("")
#we calculate price without taxes
subtotal = (ChildrenMeal*ChildrenCount)+(AdultMeal*AdultCount)
print (f"Subtotal: ${subtotal}")
# with Taxes
RealT = (Tax / 100) 
RealTaxes = RealT * subtotal
#And our final product
Total = subtotal + RealTaxes
print (f"Sales Tax:  ${RealTaxes}")  
print (f"Total: ${Total}")
print("")
# We create an if statement for the payment form. 
PaymentMethod = float(input("What is your payment amount? $"))
print("")
if PaymentMethod >= Total :
 print(f"Your Change is: ${PaymentMethod - Total}")
elif PaymentMethod < Total :
    print ("Your Payment Method has failed for insufucient founds. Repeat Calculation process again")
print("")

