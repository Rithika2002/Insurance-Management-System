import csv
class Policy:
    def plan(self):
        flag=0
        with open('result.csv','r')as file:
            plan=csv.reader(file)
            for x in plan:
                if x[0]=='1':
                    file1=open('plan1.txt','r')
                    line_1=file1.readlines()[-1]
                    print(line_1)
                elif x[0]=='2':
                    file2=open('plan2.txt','r')
                    line_2=file2.readlines()[-1]
                    print(line_2)
                elif x[0]=='3':
                    file3=open('plan3.txt','r')
                    line_3=file3.readlines()[-1]
                    print(line_3)
                elif x[0]=='4':
                    file4=open('plan4.txt','r')
                    line_4=file4.readlines()[-1]
                    print(line_4)
                else:
                    print("Invalid details")

                    
        file.close()

    
    def suggest(num): 
        print("1.Yes 2.No") 
        num=int(input("Are you willing to claim the policy we suggested?: ")) 
        if(num==1): 
            print("Thankyou for choosing our service. We will mail you the policy details and make your payment within two working days") 
        elif(num==2): 
            sugg=input("Kindly tell the reason for not choosing the policy, we will improve us better next time") 
        else: 
            print("Enter the valid number") 

    

pol=Policy()
        