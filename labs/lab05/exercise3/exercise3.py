
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    largest_latency_jump = 0
    hop_index = 0
    for i in range(1, len(traceroute)):
       latency = traceroute[i - 1][1]
       current_latency = traceroute[i][1]

       jump = current_latency - latency
       if jump > largest_latency_jump:
           largest_latency_jump = jump
           hop_index = i - 1

    return hop_index


    
    



# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
