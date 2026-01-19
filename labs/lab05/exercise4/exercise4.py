import math
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    if not times :
        return[]

    total = 0
    for i in times:
        total += i
    mean = total / len(times)

    total_variance = 0
    for i in times:
        total_variance += (i - mean) ** 2
    variance = total_variance / len(times)

    std_dev = math.sqrt(variance)
    upper_limit = mean + std_dev
   
    filtered_times = []
    for i in times:
        if i <= upper_limit:
            filtered_times.append(i)


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
