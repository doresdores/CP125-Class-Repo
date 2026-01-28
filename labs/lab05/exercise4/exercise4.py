
def filter_query_times(times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    if len(times) == 0:
        return []
    
    copy_times = times

    mean = sum(times) / len(times)
    variance = calc_variance(times, mean)

    standard_deviation = variance ** 0.5
    upper_limit = mean + standard_deviation

    for i in copy_times:
        if i > upper_limit:
            times.remove(i)
    
    
    return sorted(times)

def calc_variance(times, mean):
    sum = 0
    for i in times:
          variance = (i - mean) ** 2
          sum += variance
    
    return sum / len(times)





# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
