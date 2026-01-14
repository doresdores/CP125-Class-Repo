
def was_backward_detected(waypoints):
    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """
    for i in range(1, len(waypoints)):
        x, y, z = waypoints[i]
        pre_x, pre_y, pre_z = waypoints[i-1]
        if x < pre_x or y < pre_y:
            return True
    
    return False
        


# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
