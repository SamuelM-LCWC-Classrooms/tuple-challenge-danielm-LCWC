def task():
    name = input("Enter a student name: ")

    subject = input("Enter a subject: ")

    score = int(input("Enter a score (0-100): "))

    grade = (name, subject, score)

    return grade 
student_grade = task()
print(student_grade)