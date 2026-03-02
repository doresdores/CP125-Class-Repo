# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    import csv

    f = open(products_file, "r", newline="")
    reader = cvs.reader(f)
    products_file ={}

    for row in reader:
        product_id = row[0]
        price = float(row[2])
        products_file[product_id] = price
    f.close()
    grand_total = 0.0
    
    f = open (order_file, "r", newline="")
    reader = csv.reader(f)
    total = []
    for row in reader:
        product_id = row[0]
        quantity = int(row[1])
        price = products_file(product_id)
        total_price = Price * quantity
        total.append([product_id, quantity, total_price])
        grand_total += total_price
    f.close()

    f = open (output_file, "w", newline="")
        
    





# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
