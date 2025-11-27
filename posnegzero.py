class Solution:
    def posnegzero(self,number):
        if number>0:
            return "positive"
        elif number<0:
            return "negative"
        else:
            return "zero"
s = Solution()
print(s.posnegzero(0))