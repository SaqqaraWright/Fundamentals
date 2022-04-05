#Note: in the comments I have written out the solutions to the problems in JavaScript first to help me better understand the logic behind the functions before switching them to the Python syntax.

# 1. Basic - Print out all integers from 0 to 150
# for(var i=0; i<150; i+=1)
#     print(i)

for i in range(0, 151): #if don't include 1 at the end, it will naturally just count by 1 without me explicitly stating it.
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# for(var i=5; i<=1000; i+=1)
#     if(i%5==0)
#     print(i)

for i in range(5, 1001):
    if i%5==0:
        print(i)


# 3. Counting the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# for(var i=1; i<101, i+=1)
#     if(i%5==0)
#         print("Coding")
#     elif(i%10==0)
#         print("Coding Dojo")

for i in range(1, 101):  #There appears to be an overlap happening here because 10 is a multiple of 5; therefore, when the code is ran it is only placing "Coding" at every multiple of 5 and 10. So, I guess the fist if statement is taking precedence in this case and the 2nd on for multiples of 10 is getting overwritten.
    if i%5==0:
        print("Coding")        
    elif i%10==0:        
        print("Coding Dojo")
    else:    
        print(i)


# 4.Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000 and print the final sum.
# var sum=0  # no need to say var just state the variable btw the syntax I've been using is JavaScript not Python
# for(var i=0; i<=500,000; i+=1)
# if(i%2!==0)
#     print(sum+=i)

sum=0        #This is the correct Python syntax
for i in range(0, 500001):
    if i%2!=0:
        print(sum+i)



# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# for(var i=1; i<2019; i-=4)
#     print(i)

for i in range(1, 2019, -4):
    print(i)

# 6. Set three variables: lowNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3,6,9 (on successive lines)
lowNum=4
highNum=25
mult= 5
for i in range(lowNum, highNum+1):
    if i%mult==0:
        print(i)


