import readfiles
from updateinventory import updateStock
import datetime
inventory = readfiles.readInventory() #Assigning readInventory function from readfiles.py to inventory
#This is the main function. It take input and calls other functions.
#This is purchase(inventory) function. 
def purchase(inventory):
    for index, product in enumerate(inventory, 1):
        print(str(index) + ". " + product[0])
    choice = int(input("What would you like to purchase? "))
    name = inventory[choice - 1][0]
    price = inventory[choice - 1][1]
    stock = int(inventory[choice - 1][2])
    print("Price: " + str(price))
    print("Available: " + str(stock))
    quantity = int(input("How many " + name + " would you like to buy?"))
    if stock - quantity < 0:
        print("Out of stock!!")
        return False
    stock = stock - quantity
    inventory[choice - 1][2] = stock
    updateStock(inventory)
    return [name, price, quantity]

def discountAmount(price):
    return price * 0.1
    
def createInvoice(person_name, purchases, discount_check):
    Total_price = []
    invoice_name = person_name + '-' + str(datetime.datetime.now())
    file = open(invoice_name+".txt","w")
    file.write('Person Name: ' + person_name + '\n')
    file.write('Purchase Date ' + str(datetime.datetime.now()) + '\n')
    file.write('Purchase details\n'+"\n")
    for purchase in purchases:
        price = purchase[1]
        quantity = purchase[2]
        total = price * quantity
        if (discount_check):
            discount = discountAmount(total)
        else:
            discount = 0
        net = total - discount
        file.write("Product Name=" + '\t'+ purchase[0]+ '\n')
        file.write("Price=" + '\t'+ str(price)+"$" + '\n')
        file.write("Quantity=" + '\t'+ str(quantity)+" piece" + '\n')
        file.write("Total=" + '\t'+ str(total) +"$"+ '\n')
        file.write("Discount amount=" + '\t'+ str(discount) +"$"+ '\n')
        file.write("Final amount=" + '\t'+ str(net) + "$"+'\n'+"\n"+"\n"+"\n")
        Total_price.append(int(net))
        sum_ = 0
        for prices in Total_price:
            sum_  = float(sum_) + prices
    file.write("Total amount =" + str(sum_)+"$")
    print("Total amount =",float(sum_),"$"+'\n')
    print("Please check your invoice for further details..")
    file.close()
    


