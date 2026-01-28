def audit_blocklists(list_a, list_b, list_c):
    universal_set = list_a & list_b & list_c
    redundant_set = (list_a & list_b) | (list_b & list_c) | (list_a & list_c)
    unique_A_set = list_a - (list_b | list_c)

    return (universal_set, redundant_set, unique_A_set)
