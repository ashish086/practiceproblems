class Primenumber:
    def isPrimeNumbertimehigh(self,num):
        if num<=1:
            return "Not Prime"
        else:
            is_prime:True
            for i in range(2,num):
                if num%i==0:
                    is_prime=False
                    break 
            if is_prime:
                print("prime")
            else:
                print("not prime")

    def isPrimeNumbertimelow(self,num):
        if num<=1:
            return "Not prime"
        else:
            for i in range(2,int(num**0.5+1)):
                if num%i==0:
                    print("Not prime")
                    break
            else:
                print("prime")

z= Primenumber()
z.isPrimeNumbertimehigh(18)
z.isPrimeNumbertimelow(18)
        