x=10
print(x)
name ="alice"
print(name)
bools=True
print(bools)
a=5
b=3
print(a+b)

#for loop which prints 0 to 4 inclusive
for i in range(0,4+1):
    print(i)
    print("\n")


def evenodd(num):
    if num%2==0:
        return "Even"
    return "Odd"
print(evenodd(num=2))
print(evenodd(num=5))

nums=[1,2,3,4]
print(nums[2])

s="hello"
print(s+" world")

stringtoint="123"
stringtoint=int(stringtoint)
print(stringtoint+7)


#write a loop to sum number from 1 to 10

sum =0
for i in range(11):
    sum=sum+i
print(sum)

numstot=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(numstot)+1):
    if i%2==0:
        print(i)
    continue


#grading score

def scoregrader(score):
    if score>=90:
        return "A"
    elif score>=75:
        return "B"
    elif score>=60:
        return "C"
    else:
        return "F"
print(scoregrader(score=94))
print(scoregrader(score=89))
print(scoregrader(score=65))
print(scoregrader(score=55))


#swap variables
x=6
y=7
x,y=y,x
print(x)
print(y)

#print each character in new line using for loop

s="python"
for i in range(len(s)):
    print(s[i]+"\n")


#print list lenght and first and last element

items=[5,7,5,2]
print(len(items))
print(items[0])
print(items[-1])


#takes alist and counts the number of items in it
count =0
for i in range(len(numstot)):
    count=count+1
print(count)


#sum of i from 1 to n
n=60
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


s=""
if s=="":
    print("empty string")
else:
    print("not empty string")


#print pairwsie elements side by side using for loop
nums1=[1,2,3,4,5,6]
nums2=[10,11,12,13,14,15]
min_len = min(len(nums1),len(nums2))
for i in range(min_len):
    print(nums1[i],nums2[2])


#count the number of zeroes in a list
zeroslist=[0,0,0,1,2,3,0,0,5]
counts=0
for i in range(len(zeroslist)):
    if zeroslist[i]==0:
        counts+=1
print(counts)


#print the largest number in the list
nums22=[1,2,3,4,10,6,100,99,1]
sets=nums22[0]
for i in range(0,len(nums22)):
    if nums22[i]>=sets:
        sets=nums22[i]
print(sets)


#returns a true if all characters in string a lower case
def lowercheck(strings):
    checks=True
    for i in range(len(strings)):
        if strings[i].islower():
            continue
        checks=False
        break
    print(checks)
lowercheck(strings="PYTHON")



#print fizzbuzz

def printbuzz():
    for i in range(1,16):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
            continue
        elif i%3==0:
            print("fizz")
            continue
        elif i%5==0:
            print("buzz")
            continue
        else:
            print("not fizzbuzz")
            continue
        
printbuzz()


#list to convert to 2
list11=[1,2,3,4,5,6]
list2=[]
def mulby2(list11):
    for i in range(0,len(list11)):
        list11[i]=list11[i]*2
        list2.append(list11[i])
mulby2(list11=list11)
print(list2)


#print index of first occurence
listspop=[1,3,5,7,7,8,9]
def checkoccurence(lists,numbers):
    for i in range(0, len(lists)):
        if lists[i]==numbers:
            return i
    return -1
            

print(checkoccurence(listspop,7))


#count number of vowels 
vows=['a','e','i','o','u','A','E','I','O','U']
def countvowels(strings):
    count =0
    for i in range(0,len(strings)):
        if strings[i] in vows:
            count+=1
    print(count)

countvowels(strings="Ashish")


#rotate a list by one positon to left 
list1=[1,2,3,4,5,6]
first = list1[0]
for i in range(len(list1)-1):
    list1[i]=list1[i+1]
list1[-1]=first
print(list1)


#print swapped and original values
x=5
y=6
print(f"Before swap x:{x} and y:{y}")
x,y=y,x
print(f"after swapp x:{x} and y:{y}")




