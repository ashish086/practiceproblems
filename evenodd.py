class Solution:
    def evenodd(self, number):
        if number%2==0:
            return "Even"
        else:
            return "Odd"
s= Solution()
print(s.evenodd(4)) 
print(s.evenodd(7))