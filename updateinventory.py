def updateStock(inventory):
    file = open("stock.txt", "w")
    for product in inventory:
        line = product[0] + "," + str(product[1]) + "," + str(product[2]) + "\n"
        file.write(line)
    file.close()