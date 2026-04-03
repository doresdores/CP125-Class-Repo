import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)

    AVG = {
         "Math": round(df["Math"].mean(), 1),
        "Science": round(df["Science"].mean(), 1),
        "English": round(df["English"].mean(), 1)
    }

    best_subject = max(AVG, key=AVG.get)
    worst_subject = min(AVG, key=AVG.get)

    AVG["best_subject"] = best_subject
    AVG["worst_subject"] = worst_subject

    return AVG


