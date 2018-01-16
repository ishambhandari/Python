from purchase import purchase,discountAmount,createInvoice
from readfiles import readInventory
from updateinventory import updateStock
import datetime
print("Hello!!! This is an electronic store.We sell different kinds of mobile phones,laptops and Harddisks.Please Proceed if you wish to buy.")

def main():
    person_name = input("Enter your full name")
    inventory = readInventory()
    purchases = []
    ans = True
    while ans == True:
            handling_1 = True
            while handling_1 == True:
                try: 
                    ans = input("would you like to make a purchase?(y/n)")
                    if ans=="y":
                        purchased_item = purchase(inventory)
                        if (purchased_item):
                            purchases.append(purchased_item)
                        ans = True
                    elif ans=="n":
                        ans=False
                        handling_1 = False
                    else:
                        handling_1 = True
                        print("Please enter y or n")
                except:
                    print("Please enter correct values.")
                    handling_1 = True
                
                
    print("We give 10% discount in our product.Discount amount is subtracted in your bills.Enjoy shopping...")
    discount_check = True
    createInvoice(person_name, purchases, discount_check)
    print("Thank you for visiting our store..")
main()
	
		
		
    
