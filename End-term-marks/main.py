print('''Hello, I am Shivam Sharma 🍁.

This is a program that calculates the minimum marks you need in the final exam to pass the course.

😎😇''')

# This part takes the input from user that what is his/her name and how much marks did he/she obtained in the quiz1 and quiz 2
name = input("What is your name? ")
quiz1 = float(input("What percentage did you score in Quiz 1? "))
quiz2 = float(input("What percentage did you score in Quiz 2? "))

# This portion take 20% and 30% of quiz 1 and quiz 2 respectively and gives total weightage
weighted_quiz1 = 0.2 * quiz1
weighted_quiz2 = 0.3 * quiz2
total_weighted_marks = weighted_quiz1 + weighted_quiz2

# this portion checks wether the the user have marks greater in quiz 1 or two
if quiz2 > quiz1:
    weighted_quiz2 = 0.2 * quiz2
else:
    weighted_quiz1 = 0.2 * quiz1
    
# This portion tells you what the marks required to pass are 
marks_required = 40 - total_weighted_marks

# This portion tells you how much marks you have to obtain 
if marks_required > 0:
    minimum_marks_required = marks_required / 0.4
    print(f"You need at least {round(minimum_marks_required, 2)}% in the final exam to pass the course.")
else:
    minimum_marks_required = 0
    print("You just need to attend the final exam. You need at least 0 marks to pass the course.")

print(f'''
Wishing you all the best, {name}!
Abki bar FOD dena 🥳 🥳
''')

