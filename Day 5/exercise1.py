'''
EXERCISE 1:
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.
'''

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above👆


# Write your code below this row 👇
summ = 0
t_num = len(student_heights)
for n in range(0, t_num):
    summ += int(student_heights[n])
avg_height = round(summ/t_num, 2)
print(f"avg height is {avg_height}")
