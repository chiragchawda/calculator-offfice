class boi:
    def intrest1(self):
        print("2")
        
class axis:
    def intrest2(self):
        print("3")
        
class bob:
    def intrest3(self):
        print("4")
        
class child(boi,axis,bob):
    def __init__(self):
        print("Hey buddy! welcome")
        print("enter 1 for boi")
        print("enter 2 for axis")
        print("enter 3 for bob")
        
a= child()
w=input("enter a number=")        
if w=="1":
    a.intrest1()
elif w=="2":
    a.intrest2()
elif w=="3":
    a.intrest3()
else:
    print("your entry is wrong")




