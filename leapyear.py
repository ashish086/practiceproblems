class Solution:
    def leapyear(self,year):
        if year%4==0: #year =2200
            if year%100==0:
                if year%400==0:
                    return "Leap year"
                else:
                    return "Not a leap year"
            else:
                return "leap year"
        else:
            return "not a leap year"


        # if year %400==0:
        #     return "leap year"
        # elif year%100==0:
        #     return "no leap year"
        # elif year%4==0:
        #     return "leap"
        # else:
        #     return "no leap"
s=Solution()
print(s.leapyear(1688))