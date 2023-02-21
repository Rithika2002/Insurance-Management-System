import csv
class Register:
    def reg(self):
        email=input("Enter the email: ")
        password=input("Enter the password: ")
        from validate import Validate
        obj=Validate
        obj.checkmail(self,email)
        obj.validpass(self,password)
        details=[]
        details.append(email)
        details.append(password)
        with open ('reg.csv','a',newline='') as file:
         obj=csv.writer(file)
         obj.writerow(details)
        file.close()
        from login import Login
        log=Login()
        log.login()
        #print("Registered successfully")
object1 =Register()



