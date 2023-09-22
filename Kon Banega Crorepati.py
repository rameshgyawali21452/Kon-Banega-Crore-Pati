
money = 0
price = [12500,25000,50000,100000]
question = [ ["How can we access index and element of the list at a time?","\n 1. Enumerate 2. Split \n3.map 4.None"],
             ["what are the access specifier using in python", "1.Private?", "\n 2.Public \n3.protected 4.All the above"],
             ["How many byte took a short int ?","\n1. 2 byte", "2.1 byte \n3.8byte 4.4byte"],
             [". How can you create a virtual environment in Python?","\n 1.venv 2.vene \n3.both 4.None"]
           ]
for i in range(4):
    print("Hey competitor This is your i question, listen carefully")
    x = int(input(question[i]))
    if i == 0:
        if x == 1:
            print("Congratulation, You are right")
            money = money + price [i]
        money =0
        break
    if i == 1:
        if x == 4:
            print("Congratulation, You are right")
            money = money + price [i]
        money =0
        break
    if i == 2:
        if x == 1:
            print("Congratulation, You are right")
            money = money + price [i]
        money =0
        break
    if i == 3:
        if x == 1:
            print("Congratulation, You are right")
            money = money + price [i]
        money =0
        break

    a = int(input("Do you want to go forward 1.Yes 2. NO"))
    if a == 1:
       continue
    print(f"You won {money}")
    break
   
    
   
