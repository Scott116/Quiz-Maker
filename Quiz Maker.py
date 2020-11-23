print('''

*****************************************************************************
WELCOME TO THE QUIZ
--------------------------------------------------
PLEASE ANSWER THE QUESTIONS BELOW
POINT TABLE
TO PASS: 15 POINTS
TOTAL: 20 POINTS

**********************************************
''')

name = input("Please enter your name:")

print("\n")

print("Dear "+ name+ " Welcome to your test...!")

print("\n")

points = 0
points = int(points)


print("Question 1")
print("How many countries are there in our world?")

ans1 = 195
ans1 = int(ans1)

ans1u = input("Please Enter your answer here:")
ans1u = int(ans1u)

if ans1 == ans1u :
    print("Great Job!")
    points = points + 5
else:
    print("nevermind, the question was hard we know!")

print("\n")
print('''

Do you know
--------------
FACT: Australia is the only country that is also considered a continent
*************************************************************************
''')

print("\n")

print("Question 2")
print("What color is the sky?")

ans2 = "blue"

ans2u = input("Please enter your answer here:")

if ans2 == ans2u :
    print("Nice!")
    points = points + 5
else:
    print("How do you not know the color of the sky?")

print("\n")
print('''

Do you know
-------------------
FACT: Sometimes the sky is pink or orange during a sunset
''')

print("\n")

print("Summary of your quiz")


print("Dear " + name + "... You have Scored " + str(points)+ " points")

if points < 15:
    print("Sorry.. You failed the test!")
else:
    print("Congratulations!  You passed!")
