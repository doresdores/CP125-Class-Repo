import pandas as pd

def promotion_candidates(filename):
    df = pd.read_csv(filename)

    average_performance = round(df["PerformanceScore"].mean(), 1)
    candidates = df[(df["PerformanceScore"] > average_performance) & (df["YearsOfService"] >2)]
    candidate_count = len(candidates)
    candidate_names = set(candidates["EmployeeName"])
    
    return {
        "average_performance": average_performance,
        "min_years_required": 2,
        "candidate_count": candidate_count,
        "candidate_names": candidate_names
    }

result = promotion_candidates("labs/lab09/data/employees.csv")
print(result)
