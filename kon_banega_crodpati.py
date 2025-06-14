questions = [
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
      ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
      ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
    ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
      ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
      ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
      ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],
     ["which language was used to create the fb ?" , "python" , "Freanch" , "javascript", "php" , "None" , 4],

]

levels = [1000 , 2000 , 3000, 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000 , 640000 , 1250000 , 2500000 , 5000000 , 7500000 , "1Crore" , "7Crore"]
money = 0

for i in range( 0 , len(questions)):
    q = questions[i]

    print(f"{q[0]}")
    print(f"this question for {levels[i]}")
    print(f"1.{q[1]}        2.{q[2]}")
    print(f"3.{q[3]}        4.{q[4]}")

    reply = int(input("Enter (1 to 4) number or enter 0 to exit "))

    if(reply == 0):
        money = levels[i -1]
        break

    if(reply == q[-1]):
        print(f"\n Answer is correct you won {levels[i]}\n")

        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer")
        break

print(f"Take this money {money} and go home ")