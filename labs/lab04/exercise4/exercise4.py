
def analyze_performance(lap_times):
    mid = (len(lap_times))// 2
    first_half = lap_times[:mid]
    second_half = lap_times[mid:]
     
    

    first_avg = sum(first_half) / len(first_half)
    second_avg = sum(second_half) / len(second_half)

    return first_avg < second_avg
  

# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
