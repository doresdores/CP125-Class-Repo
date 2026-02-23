#nama:dorothy dores kelas:c02

#fungtion name
def determine_grade(marks):
    if marks >= 80:
        grade = 'A'
    elif marks >= 60:
        grade ='B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return grade

#to get input from user
marks = int(input("Enter the marks obtained:"))
print(f'Grade :{determine_grade(marks)}')
   
