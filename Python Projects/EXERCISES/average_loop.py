# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# for height in student_heights:
total = 0
num_students = 0

for height in student_heights:
    total = total + height
    num_students = num_students + 1

average = total / num_students
print(round(average))