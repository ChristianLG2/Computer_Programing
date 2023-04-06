# Fall 2021 Last Revised Winter 2023 - Christian Lira
# At our store we sell the following items at defined price in dollars.
totalItems = 0
milk = float("2.50")
milkCounter = 0
bread = float("1.25")
breadCounter = 0
juice = float("5")
JuiceCounter = 0
oranges = float("2")
orangesCounter = 0
eggs = float("2")
eggsCounter = 0
butter = float("1.25")
butterCounter = 0
peanutbutter = float("2")
peanutbutterCounter = 0
bananas =float("1.25")
bananasCounter= 0

cart = 0
option = ''

print("Welcome to our store! to start:")
while option != 'E': # true
    for options in ['A. select items', 'B. delete an item', 'C. view cart', 'D. compute total', 'E. Quit']:
        print (options)

    option = input("What do you want to do? selct a letter (Please enter a letter): ")

    if option == 'a' or option == 'A':
        option = 'A'
    elif  option == 'b' or option == 'B':
        option = 'B'
    elif  option == 'c' or option == 'C':
        option = 'C'
    elif  option == 'd' or option == 'D':
        option = 'D'
    elif  option == 'e' or option == 'E':
        option = 'E'
    else: 
        print()
        print("INVALID OPTION. Enter from the available options:")
        print()
        continue

    if option == "A":
    
        for objects in ['1. Milk $2.50', '2. bread $1.25', '3. juice $5', '4. oranges $2', '5. eggs $2', '6. butter $1.25', '7. peanutbutter $2', '8. bananas $1.25']:
            print ("we offer the best price for", objects )
            print()
            
        choice = input("what would you like to add to your cart? (Please enter a number)")

        if choice == "1":
            milkCounter = milkCounter + 1
            cart = (cart + milk)
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            print("you have ", milkCounter, " Milk(s) in your cart" )
            print("you have ", totalItems, " iteams in your cart" )
            print("total: ", cart )
            # print("you have spent", cart, "in your cart" )
            print()
        if choice == "2":
            breadCounter = breadCounter + 1
            cart = (cart + bread)
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            print("you have ", breadCounter, " Bread in your cart" )
            print("you have ", totalItems, "in your cart" )
            print("total: ", cart )
            # print("you have spent", cart, "in your cart" )
            print()
        if choice == "3":
            JuiceCounter = JuiceCounter + 1
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            cart = (cart + juice) 
            print("you have ", JuiceCounter, " Juice in your cart" )
            print("you have ", totalItems, "in your cart" )
            print("total: ", cart )
            print()
        if choice == "4":
            orangesCounter = orangesCounter + 1
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            cart = (cart + oranges)
            print("you have ", orangesCounter, " oranges in your cart" )
            print("you have ", totalItems, "in your cart" )
            print("total: ", cart )
            print()
        if  choice == "5":
            eggsCounter = eggsCounter + 1
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            cart = (cart + eggs)
            print("you have ", eggsCounter, "eggs in your cart" )
            print("you have ", totalItems, "in your cart" )
            print("total: ", cart )
            print()
        if choice == "6":
            butterCounter = butterCounter + 1
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            cart = (cart + butter)
            print("you have", butterCounter, " butter in your cart" )
            print("you have ", totalItems, "in your cart" )
            print("total: ", cart )
            print()
        if choice == "7":
            peanutbutterCounter = peanutbutterCounter + 1
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            cart = (cart + peanutbutter)
            print("you have ", peanutbutterCounter, " peanutbutter in your cart" )
            print("you have ", totalItems, "in your cart" )
            print("total: ", cart )
            print()
        if choice == "8":
            bananasCounter = bananasCounter + 1 
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            cart = (cart + bananas)
            print("you have",bananasCounter, " bananas in your cart" )
            print()
    
    print()

    if option == "B":
        if totalItems == 0:
            print("You dont have any items yet")
            continue
        else:
    
            totalItems = milkCounter + breadCounter + JuiceCounter + orangesCounter + eggsCounter + butterCounter +peanutbutterCounter +bananasCounter
            print("you have ", milkCounter, " Milk(s) in your cart" )
            print("you have ", breadCounter, " Bread in your cart" )
            print("you have ", JuiceCounter, " Juice in your cart" )
            print("you have ", orangesCounter, " oranges in your cart" )
            print("you have ", eggsCounter, "eggs in your cart" )
            print("you have", butterCounter, " butter in your cart" )
            print("you have ", peanutbutterCounter, " peanutbutter in your cart" )
            print("you have",bananasCounter, " bananas in your cart" )

            print("you have ", totalItems, "in your cart" )
            print("total spent: ", cart )
            
            print("what item do you want to delete?")
            
            for objects in ['1. Milk 2.50$', '2. bread 1.25$', '3. juice 5$', '4. oranges 2$', '5. eggs 2$', '6. butter 1.25$', '7. peanutbutter 2$', '8. bananas 1.25$']:
             print (objects )
            delition = input(" Enter Item Number: ")
            if delition == "1":
                milkCounter = milkCounter - 1
                totalItems = totalItems -1 
                cart = cart - milk
                continue
            if delition =="2":
                breadCounter = breadCounter -1
                totalItems = totalItems -1 
                cart = cart - bread
                continue
            if delition == "3":
                JuiceCounter=JuiceCounter -1
                totalItems = totalItems -1 
                cart = cart - juice
                continue
            if delition == "4":
                orangesCounter = orangesCounter -1 
                totalItems = totalItems -1 
                cart = cart - oranges
                continue
            if delition == "5":
                eggsCounter = eggsCounter -1
                totalItems = totalItems -1 
                cart = cart - eggs
                continue
            if delition == "6":
                butterCounter = butterCounter - 1
                totalItems = totalItems -1 
                cart = cart - butter
                continue
            if delition == "7":
                peanutbutterCounter = peanutbutterCounter -1 
                totalItems = totalItems -1 
                cart = cart - peanutbutter
                continue
            if delition == "8":
                bananasCounter = bananasCounter-1
                totalItems = totalItems -1 
                cart = cart - bananas
                continue
        
             
    
    if option == "C":
        if totalItems == 0:
            print("You dont have any items yet")
            continue
        else:
            print("you have ", milkCounter, " Milk(s) in your cart" )
            print("you have ", breadCounter, " Bread in your cart" )
            print("you have ", JuiceCounter, " Juice in your cart" )
            print("you have ", orangesCounter, " oranges in your cart" )
            print("you have ", eggsCounter, "eggs in your cart" )
            print("you have", butterCounter, " butter in your cart" )
            print("you have ", peanutbutterCounter, " peanutbutter in your cart" )
            print("you have",bananasCounter, " bananas in your cart" )

            print("you have ", totalItems, "in your cart" )
            print("total amount spent: $", cart )

        

    if option == "D":
        if totalItems == 0:
            print("You dont have any items yet")
            continue
        else:
            print("total amount spent: $", cart)


    if option == "E":
        #print("thanks for your visit!")
        continue
    
else:
    print("We appreciate your Business, Thanks For choosing us!")
   



