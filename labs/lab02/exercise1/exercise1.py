def is_budget_sufficient(one_way_km, km_per_litter,Price_per_litter,budget):
    two_way_km =one_way_km * 2
    litres_needed = two_way_km / km_per_litter
    total_cost = litres_needed * Price_per_litter
    if total_cost <= budget:
        return True
    else:
        return False
    


