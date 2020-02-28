biology = float(input("Please enter your score for Biology: "))
chemistry = float(input("Please enter your score for Chemistry: "))
physics = float(input("Please enter your score for Physics: "))

score = (biology + chemistry + physics) / 3

if biology < 40 or chemistry < 40 or physics < 40:
    print("Fail")

elif score >= 70:
    print("1st")
elif score >= 60:
    print("2.1")
elif score >= 50:
    print("2.2")
elif score >= 40:
    print("Pass")
else:
    print("Fail!")
    
