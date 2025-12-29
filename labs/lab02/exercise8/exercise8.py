def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    # TODO: Implement this
    return current_height * 0.8


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    # TODO: Implement this
    return height< 1


def calculate_bounce_count(initial_height,):
    """
    Count how many times the ball bounces.
    """
    # TODO: Implement this
    count = 0
    height = initial_height

    if height == 0:
        return 0

    while True:
        height = calculate_bounce_height(height)
        count += 1
        if is_ball_stopped(height):
            break
    return count


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    # TODO: Implement this
    if initial_height == 0:
        return 0
    
    total_distance = initial_height  
    height = initial_height

    while True:
        height = calculate_bounce_height(height)
        total_distance += height  

        if is_ball_stopped(height):
            break
        
        total_distance += height  
    return total_distance
