1
for i in range(0, 151):
    print(i)

2
for i in range(0, 1000):
    if i % 5 == 0:
        print(i)

3
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding")
    elif i % 5 == 0:
        print("CodingDojo")
    else: 
        print(i)

4
sum = 0
for i in range(1,500001):
    if i % 2 == 1:
        sum+= i
print(sum)

5
sum = 0
for i in range(2018, 0, -4):
    print(i)


6
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)