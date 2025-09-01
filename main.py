#importing all the modules 
import add
import sub
import mul
import div
import modulousdiv
import power
import square_root


operations = (
    " 1.add\n",
    "2.sub\n",
    "3.mul\n",
    "4.div\n",
    "5.modulousdiv\n",
    "6.power\n",
    "7.Square_root\n"
)
# main function 
if __name__== "__main__":
    print("Welcome to Simple Calculator , Im here to do 2 number operations")
   
    #creating infinate loop 

    while True:
        print(*operations)
        choice=int(input("Please slecte your operation :"))

        if choice==1:
            num1=int(input("enter num 1:"))
            num2=int(input("enter num 2:"))
            print(add.addition(a=num1,b=num2))

        elif choice==2:
            num1=float(input("enter num 1:"))
            num2=float(input("enter num 2:"))
            print(sub.subtraction(a=num1,b=num2))


        elif choice==3:
            num1=float(input("enter num 1:"))
            num2=float(input("enter num 2:"))
            print(mul.multiplication(a=num1,b=num2))


        elif choice==4:
            num1=float(input("enter num 1:"))
            num2=float(input("enter num 2:"))
            print(div.division(a=num1,b=num2))

        elif choice==5:
            num1=int(input("enter num 1:"))
            num2=int(input("enter num 2:"))
            print(modulousdiv.modulous(a=num1,b=num2))

        elif choice==6:
            num1=int(input("enter num 1:"))
            num2=int(input("enter num 2:"))
            print(power.pow(a=num1,b=num2))
            
        elif choice==7:
            num1=float(input("enter num 1:"))
            num2=float(input("enter num 2:"))
            print(square_root.squ(a=num1,b=num2))

        elif choice==8:
            print("Exiting from caluclotor")
            exit()

        else:
            print("Please select the operation between 1 to 6 :")


        

