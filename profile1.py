import datetime
import csv
global age,dob,salary

class Profile:
    def calculate_age(self,dob):
        today = datetime.date.today()
        age =today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print("Your age is: ",age)
        print("1.Below 1 lakhs  2. below 2 lakhs 3. Between 5 - 10 lakhs  4. Above 10 lakhs")
        salary=int(input("Enter your income range: "))
        number=(input("Enter your mobile number: "))
        prof.contact_num(number,salary,age)
 
    def contact_num(self,number,salary,age):
        print("1. SMS 2.Call")
        number1=int(input("How would you like to verify your number? ")) 
        if number==1:
            print("You will get a SMS from our side for verification")
            one_pass=input("Enter OTP: ")
            if len(one_pass)==4:
                print("Your account is verified")
            else:
                print("Your OTP is wrong..Try again")
            
        elif number==2:
            print("You will get a call from our side for verification")
            print("1.Yes 2.No")
            call=int(input("Did you received the call? "))
            if call==1:
                print("You will be directed to policy plans page")
            else:
                print("Kindly wait for sometime and try again")
        else:
            print("Enter a valid option")

        values=[]
        values.append(salary)
        values.append(age)
        values.append(number)
        with open('result.csv','a',newline='')as file:
            f=csv.writer(file)
            f.writerow(values)
        file.close()
        from policy import Policy
        pol=Policy()
        pol.plan()

    def user_info(self):
        year=int(input("Enter birth year: "))
        month=int(input("Enter birth month: "))
        date=int(input("Enter birth date: "))
        dob = datetime.date(year,month,date)
        prof.calculate_age(dob)
        

prof=Profile()


    









