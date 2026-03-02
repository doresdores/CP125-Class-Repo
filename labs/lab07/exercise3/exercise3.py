def compare_prices(store_a, store_b):
    only = []
    a_cheaper =[]
    b_cheaper = []
    for item in store_a :
        if item not in store_b:
            only.append(item)
        elif store_a[item] < store_b[item]:
            a_cheaper.append(item)
        elif store_b[item] < store_a[item]:
            b_cheaper.append(item)

    for item in store_b:
        if item not in store_a:
            only.append(item)
            return {"only_a": only, "a_cheaper":





store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
