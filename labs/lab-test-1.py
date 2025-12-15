#dorothy dores , kelas: c02

#for fungtion
def  determine_grade(mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade 

#for input and call fungtion
mark = float(input("Enter the student's mark:"))
grade = determine_grade(mark)

print ('Mark:', mark , ', Grade', grade)
