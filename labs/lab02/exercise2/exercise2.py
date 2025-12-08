# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    food_cost = participants * meal_price
    tent = math.ceil(participants / tent_capacity)
    cost_of_tent = tent_price * tent 
    total_budget = food_cost + cost_of_tent
    return total_budget
    

# Test your code here

