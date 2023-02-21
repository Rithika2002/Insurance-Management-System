class home():
    def main(self):
        print("1.New user 2.Registered user")
        x=int(input("Enter the number for navigation: "))
        if x==1:
            print("You will be directed to registration page")
            from registration import Register
            obj=Register
            obj.reg(self)
        elif x==2:
            print("You will be directed to login page")
            from login import Login
            log=Login()
            log.login(self)
        else:
            print("Enter valid credentials")
r=home()
r.main()
