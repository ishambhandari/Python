#This function reads the text files..
def readInventory():
    inventory = []
    file = open("stock.txt", "r") #Reading the text file
    lines = file.readlines()
    for line in lines:
        product = line.split(',')
        product[1] = int(product[1])
        product[2] = int(product[2])
        inventory.append(product)
    return inventory
    

