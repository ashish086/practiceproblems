class Solution:
    def largestoftwonums(self,number1,number2):
        if number1>number2:
            return f"{number1} is largest"
        elif number1<number2:
            return f"{number2} is largest"
        else:
            return "both equal"
        
    def largestofthreenums(self,number1,number2,number3):
        if number1>=number2 and number1>=number3:
            return number1
        elif number2>=number1 and number2>=number3:
            return number2
        else:
            return number3
s= Solution()
print(s.largestoftwonums(25,24))
print(s.largestofthreenums(26,24,25))
        