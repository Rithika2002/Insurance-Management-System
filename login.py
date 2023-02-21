import csv
class Login:
    def login(self):
        em=input("Enter your mail id: ")
        passwd=input("Enter your password: ")
        flag=0
        with open('reg.csv','r')as file:
            enter=csv.reader(file)
            for x in enter:
                if(x[0]==em and x[1]==passwd):
                    flag=1
        file.close()
        if(flag==1):
            print("Logged in successfully")
            from profile1 import Profile
            prof=Profile()
            prof.user_info()
            
        else:
            print("Invalid login..Try again")
        

log=Login()
log.login()






