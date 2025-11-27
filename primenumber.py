class calculator:
    def calculator(self,num1,num2,operator):
        try:
            if operator==1:
                return num1+num2
            elif operator==2:
                return num1-num2
            elif operator==3:
                return num1*num2    
            elif operator ==4:
                return num1/num2
            elif operator ==5:
                return num1%num2
            else:
                return "Invalid operator"
        except ZeroDivisionError:
            return "Can not be divide by zero"    

if __name__=="__main__":
    num1=int(input("enter your first number"))
    num2=int(input("Enter second number\n"))
    print("--------------------------\n")
    print("Simple Calculator\n")
    print("Options\n")
    print("1.Add\n")
    print("2.Subtract\n")
    print("3.Multiply\n")
    print("4. Divide\n")
    print("5.Modulo remainder\n")
    opsnum=int(input("Enter your operator option"))
    res= calculator()
    print(res.calculator(num1,num2,opsnum))
    
