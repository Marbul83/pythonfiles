num = (input("Please enter your 12 digit book code: "))
if len(num) != 12:
    print("ERROR! Please re-enter 12 digit code code:")
book = list(map(int,str(num)))
total = 0
for x in book:
    if book.index(x) % 2 > 0:
        total += x
print(total)
