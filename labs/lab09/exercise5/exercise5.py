import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)
    
    subjects = ["Math", "Science", "English", "Physics", "Chemistry"]
    high_perf = df[(df[subjects] > 85).all(axis=1)]
    names = set(high_perf["Name"])
   
    
    result = {
        "count": len(names),
        "names": names
    }
    
    return result

result = high_performers("labs/lab09/data/students.csv")
print(result)

