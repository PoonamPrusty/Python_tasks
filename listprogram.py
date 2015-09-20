scores = []
choice = None

while choice != 0:
    print """High Score Keeper
                0 - Exit
                1 - Show Scores
                2 - Add a score
                3 - Delete a score
                4 - Sort scores """
    choice = (raw_input("Choice: "))

    if choice == "0":
        print "Bye!"
        exit()   
    elif choice == "1":
        for score in scores:
            print score
    elif choice == "2":
        score = int(raw_input("Enter score to add: "))
        scores.append(score)
        print "The modified score list is: ", scores
    elif choice == "3":
        score = int(raw_input("Enter score to remove: "))
        if score in scores:
            scores.remove(score) 
            print "The modified score list is: ", scores
        else:
            print "That score is not in the list"
    elif choice == "4":
        scores.sort()
        scores.reverse()
        print scores
        
    else:
        print choice, "is not a valid entry."

 
