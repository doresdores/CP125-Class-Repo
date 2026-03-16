# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    count = 0
    f= open(input_file, "r")
    
    


# Test your code here
result = filter_passing_scores("labs/lab08/data/scores.txt", "labs/lab08/data/passing.txt")
print(f"Passing students: {result}")
