#count how many elements is greater than 1st element
def greaterthanone(nums):
    first = nums[0]
    count =0
    for i in range(len(nums)):
        if nums[i]>first:
            count+=1
    return count

nums=[5,7,3,9,6]
print(greaterthanone(nums))


#print index of first vowel
def firstvowelfind(stringss):
    vows=['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(stringss)):
        if stringss[i] in vows:
            print(i)
            break

firstvowelfind('bedfae')

#rverse a list 
def reverselist(nums):
    reverseds=[]
    for i in nums:
        reverseds=[i]+reverseds
    print(reverseds)

    #Another way
    '''
    for i in range(len(nums)-1,-1,-1):
        reverseds.append(nums[i])
    '''        
reverselist([1,2,3,4])



