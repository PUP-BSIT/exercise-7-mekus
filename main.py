def add_to_products(products, product_name, price, quantity):
    total = price * quantity  # Compute the total price of the product
    product = [product_name, price, quantity, total]  # Store product details 
    products.append(product)  # Add product to the products list

def is_senior_citizen(senior_id):
    return senior_id != ""  # Check if senior_id is not empty

def get_grand_total(products, is_senior):
    grand_total = 0  # Initialize the grand total to 0

    # Sum up the total price of all products
    for product in products:
        grand_total += product[3]  
     
    # Apply 10% discount if customer is a senior citizen
    if is_senior:
        grand_total *= 0.90  
    
    return grand_total  # Return the grand total

def display_details(products, customer_name, senior_id, grand_total):
    # Check if senior_id is empty, if so, set it to "N/A"
    if not is_senior_citizen(senior_id):
        senior_id = "N/A"
    
    # Display the listed products
    print("\nLIST OF ITEMS:")
    for counter, product in enumerate(products):
        print(
            f"{counter + 1}. {product[0]}, {product[1]:.2f}, "
            f"{product[2]}, {product[3]:.2f}"
        )

    # Display the customer details
    print(f"\nCUSTOMER NAME: {customer_name}")
    print(f"SENIOR ID NO.: {senior_id}")
    
    # Display the grand total amount
    print(f"GRAND TOTAL: {grand_total:.2f}")

def main():
    # Initialize products list
    products = []

    # Loop to keep adding products
    while True:
        # Prompt user for product details
        product_name = input("ENTER PRODUCT NAME: ")
        product_price = float(input("ENTER PRODUCT PRICE: "))
        product_quantity = int(input("ENTER PRODUCT QUANTITY: "))

        # Add product details to the products list
        add_to_products(products, 
                        product_name, 
                        product_price, 
                        product_quantity)

        # Loop to validate user input ('y' or 'n')
        while True:
            is_add_more = input("DO YOU WISH TO ADD MORE? (y/n): ").lower()
            if is_add_more == 'y' or is_add_more == 'n':
                break

            print("INVALID INPUT. PLEASE ENTER ('y' or 'n').")

        # Checks if the user entered 'n'(no)
        if is_add_more == 'n':
            break
    
    # Prompt user for customer name
    customer_name = input("ENTER CUSTOMER NAME: ")

    # Loop to validate senior ID input (blank or numeric)
    while True:
        senior_id_no = input(
            "ENTER YOUR SENIOR ID NUMBER (LEAVE BLANK IF N/A): "
        )
        if senior_id_no == "" or senior_id_no.isdigit():
            break

        print("INVALID INPUT. MUST BE BLANK OR NUMERIC.")

    # Determine if the customer is a senior citizen
    is_senior = is_senior_citizen(senior_id_no)
    
    # Get the grand total amount
    grand_total = get_grand_total(products, is_senior)
    
    # Display the details of the products and customer
    display_details(products, customer_name, senior_id_no, grand_total)
    
# Execute the main function
main()