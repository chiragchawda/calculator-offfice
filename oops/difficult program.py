class org:
    print("Bitsquad team")
    def dep(self,department,language):
        self.department=department
        self.language=language
        self.a=["automation","development","testing","sales"]
        self.b=["python","java",".net","power"]
        if self.department in self.a and self.language in self.b:
            return[self.department,self.language]
        else:
            return["enter valid details"]
        

class depa(org):
    def show(self,name,age,des,mob,department,language):
        self.name=name
        self.age=age
        self.des=des
        self.mob=mob
        self.d= super().dep(department,language)
        return [self.name,self.age,self.des,self.mob]+self.d
   
    
    def info(self,name,age,des,mob,department,language):
        data=self.show(name,age,des,mob,department,language)
        return(data)
    
a=depa()

# b=dep()a.dep(department,)
abc={}
key=1
while True:

    name=input("enter a name")
    age=input("enter a age")
    des=input("enter a designation")
    mob=input("enter a mobile no.")
    department=input("enter a deparment")
    language=input("enter a language")
    ab=a.info(name,age,des,mob,department,language)
    abc[key]=ab
    x=input("do yo want to continue yes or no")
    if x=="yes":
        key+=1
        continue
    else:
        break
print(abc)

    