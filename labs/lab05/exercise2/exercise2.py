
def find_largest_drop(readings):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    largest_drop = 0
    for i in range(1, len(readings)):
        difference = readings[i-1] - readings[i]
        if difference > largest_drop:
            largest_drop = difference
    
    return largest_drop



# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
