def audit_zero_trust(baseline_set, current_log_list):
    
    current_log =set(current_log_list)
   
    authorized = baseline_set & current_log
    inactive = baseline_set - current_log
    alert = current_log -baseline_set

    return (authorized, alert, inactive)

    



