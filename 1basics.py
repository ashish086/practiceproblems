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


#sum of numbers from 1 to n
n=60
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
