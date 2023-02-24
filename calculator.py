bool= True
while bool:
    first=input("do you want to calculate [Y/N]=")
    print(first)
    if first.lower()=="y":
        operatorFlag= True
        while operatorFlag:
            operator=input("what do you want to do [+,-,*,/]")
            if operator=="+":
                firstnoFlag=True
                while True:
                    firstno = (input("enter a first no.="))
                    # if firstno.isnumeric():
                    if firstno.isnumeric():
                        firstno=int(firstno)
                        while True:
                            secondno=(input("enter a second digit no.="))
                            if secondno.isnumeric():
                                secondno=int(secondno)
                                print(firstno+secondno)
                                operatorFlag=False
                                break
                            else:
                                print("invalid input")
                            
                        break
                    else:
                        print("enter input is not digit")
                
            elif operator=="-":
                firstnoFlag=True
                while True:
                    firstno = (input("enter a first no.="))
                    if firstno.isnumeric():
                        firstno=int(firstno)
                        while True:
                            secondno=(input("enter a second digit no.="))
                            if secondno.isnumeric():
                                secondno=int(secondno)
                                print(firstno-secondno)
                                operatorFlag=False
                                break
                            else:
                                print("invalid input")
                            
                        break
                    else:
                        print("enter input is not digit")
            elif operator=="*":
                firstnoFlag=True
                while True:
                    firstno = (input("enter a first no.="))
                    if firstno.isnumeric():
                        firstno=int(firstno)
                        while True:
                            secondno=(input("enter a second digit no.="))
                            if secondno.isnumeric():
                                secondno=int(secondno)
                                print(firstno*secondno)
                                operatorFlag=False
                                break
                            else:
                                print("invalid input")
                            
                        break
                    else:
                        print("enter input is not digit")
            elif operator=="/":
                firstnoFlag=True
                while True:
                    firstno = (input("enter a first no.="))
                    if firstno.isnumeric():
                        firstno=int(firstno)
                        while True:
                            secondno=(input("enter a second digit no.="))
                            if secondno.isnumeric():
                                secondno=int(secondno)
                                try:
                                    print(firstno/secondno)
                                except:
                                    print("error can't divide by zero")
                                operatorFlag=False
                                break
                            else:
                                print("invalid input")
                            
                        break
                    else:
                        print("enter input is not digit")
            else:
                print("invalid operator")

    elif first=="N":
        print("finish")
        bool=False
        # break
    else:
        print("invalid input")
        

