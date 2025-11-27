import os

def analyze_data(filename):
    # 1. DATA STRUCTURES
    sales_by_country = {}  # Dictionary (Key: Country, Value: Count)
    product_sales = {}     # Dictionary (Key: Product, Value: Quantity)
    total_revenue = 0.0
    total_orders = 0       # This tracks the number of orders

    # 2. FILE I/O
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        return

    # 3. PARSING LOOP
    # Skip the header row (index 0)
    for line in lines[1:]:
        line = line.strip() # Remove whitespace
        if not line:
            continue 

        # Manual CSV parsing
        parts = line.split(',')
        # parts is a List: ['101', 'AlarmClock', '29.99', '2', 'USA']
        
        # Extract data (Type casting is essential!)
        product = parts[1]
        price = float(parts[2])
        quantity = int(parts[3])
        country = parts[4]

        # 4. LOGIC & MATH
        # Revenue
        total_revenue += (price * quantity)
        
        # Track number of orders (This counts every line processed)
        total_orders += 1

        # Country Count logic
        if country in sales_by_country:
            sales_by_country[country] += 1
        else:
            sales_by_country[country] = 1
        
        # Product Quantity Count logic
        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

    # 5. FIND MAX (The Algorithm)
    best_product = ""
    max_sales = 0
    
    for product, qty in product_sales.items():
        if qty > max_sales:
            max_sales = qty
            best_product = product

    # 6. REPORTING
    print("----------- STARTUP METRICS REPORT -----------")
    print(f"Total Revenue:      ${total_revenue:.2f}")
    print(f"Total Orders:       {total_orders}") 
    print(f"Best Selling Item:  {best_product} ({max_sales} units)")
    
    # --- YOUR HOMEWORK STARTS HERE ---
    # Calculate Average Order Value (Revenue / Orders)
    if total_orders > 0:
        average_order_value = total_revenue / total_orders
        print(f"Average Order Value: ${average_order_value:.2f}")
    else:
        print("Average Order Value: $0.00")
    # --- YOUR HOMEWORK ENDS HERE ---
    
    print("\nSales by Country:")
    for country, count in sales_by_country.items():
        print(f"  - {country}: {count}")
    print("----------------------------------------------")

# Create dummy data for testing
def create_dummy_data():
    content = """ID,Product,Price,Quantity,Country
101,SmartAlarm_Basic,49.99,1,USA
102,SmartAlarm_Pro,89.99,2,UK
103,SmartAlarm_Basic,49.99,1,USA
104,Cable_USB_C,9.99,5,Germany
105,SmartAlarm_Pro,89.99,1,UK
106,SmartAlarm_Basic,49.99,3,France
"""
    with open("startup_data.csv", "w") as f:
        f.write(content)

if __name__ == "__main__":
    create_dummy_data()
    analyze_data("startup_data.csv")