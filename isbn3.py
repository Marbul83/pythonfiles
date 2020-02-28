num = input("Enter ISBN: ")
sum1 = 0
sum2 = 0
for index in range (0,13,2):
    temp = int(num[index])
    sum1 = sum1 + temp
for index2 in range (1,12,2):
    temp2 = int(num[index2])*3
    sum2 = sum2 + temp2
total = sum1 + sum2 
remain = total % 10
x13 = 10 - remain