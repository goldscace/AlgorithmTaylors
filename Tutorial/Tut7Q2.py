file=open("student.txt")
students=file.readlines()

average=[]

for student in students:
    student=student.strip().split("//")
    id=student[0]
    name=student[1]
    gpa=student[2:]
    for i in gpa:
        i=float(i)
        average.append(i)
    cgpa=sum(average)/4
    print(name,"(Student ID:",id,") have a",cgpa,"CGPA")
    average=[]


