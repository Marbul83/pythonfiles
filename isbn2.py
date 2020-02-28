num = (input("Please enter your 12 digit book code: "))
if len(num) != 12:
    print("ERROR! Please re-enter 12 digit code:")
result = 0
for i in range(1,12,2):
    result += int(num[i])*3
for i in range(0,12,2):
    result += int(num[i])
print(result)
rem = result % 10
check = 10 - rem

print("The remainer is: ",rem)
print("The check value is: ", check)

    
    