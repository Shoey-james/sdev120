# Day 3 Did before demonstration. Calculate grade from an input score on a 10 point scale. Nested if/elif/else statements. do a second pass if/else.
# James Shoemaker 10/30/23 Fall Second 8 Weeks

score = input("Enter integer score from 0 to 100 to calculate grade: ")       # prompt for input value from user
s =float(score)                     # turning score into a floating number
if (s < 0):                        # getting rid of numbers less than a score of 0
        print("Wrong Input")         #error message
if s >=90:                         # setting parameters to get an A
        print("The grade is an A")   # print command to display the grade based off score for the user
elif s >=80:                         # setting parameters to get an B
        print("The grade is a B")    # print command to display the grade based off score for the user
elif s >=70:                         # setting parameters to get an C
        print("The grade is a C")    # print command to display the grade based off score for the user
elif s >=60:                         # setting parameters to get an D
        print("The grade is a D")    # print command to display the grade based off score for the user
else:
        print("The grade is a F")    # print command to display the grade based off score for the user
