import pandas as pd

def explore_data(filename):
    df = pd.read_cvs(filename)
    total_students = len(df)
    math_average = df["Math"].mean()
    highest_math_student = df.loc[df["Math"],]
    
    return {
        "total_students": total_students,
        "subjects": subject,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }

