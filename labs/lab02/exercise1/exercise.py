def is_budget_enough(distance, fuel_cost, fuel_price):
    total_distance = distance * 2
    litres_needed = total_distance / fuel_cost
    total_cost = litres_needed * fuel_price
    return total_cost

if is_budget_enough(7,5,0.5):
   print("You have enough money for the round trip!")
else:
    print("DOESN'T ENOUDH MONEY.")
 