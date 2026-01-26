def audit_blocklists(list_a, list_b, list_c):
    set_a = set(list_a)
    set_b = set(list_b)
    set_c = set(list_c)

    universal = set_a & set_b & set_c
    redundant = (set_a & set_b) | (set_a & set_c) | (set_b & set_c)
    unique_a = set_a - set_b - set_c

    return universal, redundant, unique_a
