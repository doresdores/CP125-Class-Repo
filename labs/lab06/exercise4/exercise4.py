def synchronize_databases(legacy_list, modern_set, blacklist):
    sanitized_legacy_set = set()

    for item in legacy_list:
        if item[1] not in blacklist:
            sanitized_legacy_set.add(item[0])
    
    lost_set = sanitized_legacy_set - modern_set
    ghost_set = modern_set - sanitized_legacy_set

    return (lost_set, ghost_set)
