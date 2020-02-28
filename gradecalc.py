def input_function():

    name = input("Please enter your name: ")
    homework = int(input("Please enter your homework score out of 50:"))
    assessment = int(input("Please enter your assessment score out of 50: "))
    finalexam = int(input("Please enter your final exam score out of 50: "))
    return name,homework,assessment,finalexam

def average():
    name,homework,assessment,finalexam = input_function()
    
    result = int(homework + assessment + finalexam) / 3
    return result 

score = average()

print(score)

if score < 40:
    print("Excellent!")
elif score < 25:
    print("Good work!")
else:
    print("You have failed!")

average()
