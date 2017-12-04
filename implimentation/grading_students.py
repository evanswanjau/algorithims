'''
A program that takes in the student count and assigngs them their total grade.
Any grade below is a fail and anything above 40 is a pass. A number is rounded off to the nearest
multiple of 5 if the difference is less than 3
'''

student_count = int(input("Enter student count: "))
student_marks = []

def grading_students(student_count, student_marks):

    i = 0
    while i < student_count:
        i += 1
        mark = int(input("Enter student marks: "))

        if mark > 40:
            rounded_number = 5 * round(mark/5)

            if rounded_number > mark and rounded_number - mark < 3:
                mark = rounded_number

        student_marks.append(mark)


    for i in student_marks:
        print(i)

grading_students(student_count, student_marks)
