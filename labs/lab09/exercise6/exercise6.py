import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)

    total_product = len(df)
    critical= df[(df["StockLevel"] < df["ReorderThreshold"]) &(df["DaysSinceRestock"] > 30)]
    critical_count = len(critical)
    critical_products = set(critical["ProductName"])
    
    return {
        "total_products": total_product,
        "critical_count": critical_count,
        "critical_products": critical_products
    }
                       
result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)



