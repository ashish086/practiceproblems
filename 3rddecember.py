#Check if removing one adjacent pair makes list sorted.

def removeadjacent(numslist):
    n= len(numslist)
    for i in range(n-1):
        new = []
        for j in range(n):
            if j==i or j==i+1:
                continue
            new.append(numslist[j])

        if new==sorted(new):
            return True
    
    return False


#print(removeadjacent([17,5,13,1]))


#Count elements greater than sum of previous elements.

def countsum(nums):
    count = 0
    prev_sum = 0

    for i in range(len(nums)):
        if nums[i] > prev_sum:
            count += 1

        prev_sum += nums[i]

    return count

print(countsum([2, 3, 7, 1, 12]))


#Longest subarray with same adjacent difference.

def longsubarray(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev_diff = nums[1] - nums[0]
    cur_len = 2
    max_len = 2
    for i in range(2, n):
        diff = nums[i] - nums[i - 1]

        if diff == prev_diff:
            cur_len += 1
        else:
            prev_diff = diff
            cur_len = 2  

        if cur_len > max_len:
            max_len = cur_len

    return max_len

print(longsubarray([1,3,5,8,11,14,16,18,20]))



#Longest strictly increasing alphabetical substring.

def longalpha(s):
    if not s:
        return ""

    s_lower = s.lower()
    b = current = s[0]

    for i in range(1, len(s)):
        if s_lower[i] > s_lower[i-1]:
            current += s[i]
        else:
            if len(current) > len(b):
                b = current
            current = s[i]

    if len(current) > len(b):
        b = current

    return b

print(longalpha("abcfdea"))



        