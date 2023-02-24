class office_stats:
    organisation_name = "BitSquad Softwware PVT ltd"
    def __init__(self):
        self.employ_count = 3
        

    def departments(self,department,employee_name, id, gender, mobile_number,departments_data):
        self.department = department.lower() if department.lower().strip() in self.departments_data else "Department not present here!!!!"
        self.emp_name = employee_name
        self.emp_id = id
        self.gender = gender
        self.mobile_number  = mobile_number
        return [office_stats.organisation_name,self.department, self.emp_name, self.emp_id, self.gender, self.mobile_number,self.employ_count,departments_data]
    
class language_stats(office_stats):
    def departments(self, language, department, employee_name, id, gender, mobile_number,departments_data):
        self.department = super().departments(department, employee_name, id, gender, mobile_number,departments_data)
        self.language = language.lower() if language.lower().strip() in self.languages_data else "Language is not present here!!!"
        self.department.append(language)
        return self.department
    
    
    def Info(self, lan , department, employee_name, id, gender, mobile_number,departments_data):
        self.lan_data = self.departments(lan, department, employee_name, id, gender, mobile_number,departments_data)
        return self.lan_data
l =language_stats()


departments_data =  ["automation","development","testing"]
languages_data  = ["python","java",".net","power app"]
data_dict = {}
i=1
while i<=l.employ_count:
    lan = input("Please enter the valid language:")
    department = input("Please enter the valid department:")
    employee_name = input("Please enter the valid employee_name:")
    id = input("Please enter the valid id :")
    gender = input("Please enter the valid gender (M/F):")
    mobile_number = input("Please enter the valid monile number:")
    data = l.Info(lan, department, employee_name, id, gender, mobile_number,departments_data)
    data_dict[i] = data
    print(data_dict)
    user_input = input("Want to enter more data (yes/no):")
    if user_input.lower().strip() == 'yes':
        i+=1
        continue
    else:
        break


print(data_dict)

