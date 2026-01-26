def synchronize_databases(legacy_list, modern_set, blacklist):
    legacy_ids = set()
   
    for id, email in legacy_list:
        if email not in blacklist:
            legacy_ids.add(id)
   
    lost_set = legacy_ids - modern_set
    ghost_set = modern_set - legacy_ids
    
    return (lost_set, ghost_set)
