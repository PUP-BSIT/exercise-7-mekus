def add_to_products(products,product_name, price, quantity):
    total = price * quantity
    product = [product_name, price, quantity, total]
    products.append(product)

def is_senior_citizen(senior_id):
    return senior_id == ""

def get_grand_total(products, is_senior):
    grand_total = 0

    for product in products:
        grand_total += product[3]  
     
    if is_senior:
        grand_total *= 0.90  
    
    return grand_total 

#TODO: Implement a function that displays the the following details:
# - Items(product name, price, quantity, total)
# - Customer Name
# - Senior ID no.
# - Grand Total
# Assigned to: Olazo, John Albert

def main():
    # Initialize products list
    products = []

    # Loop to keep adding products
    while True:
        # Prompt user for product details
        product_name = input("ENTER PRODUCT NAME: ")
        product_price = float(input("ENTER PRODUCT PRICE: "))
        product_quantity = int(input("ENTER PRODUCT QUANTITY: "))

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
    
    customer_name = input("ENTER CUSTOMER NAME: ")

    # Loop to validate user input (blank, number, or invalid input)
    while True:
        senior_id_no = input(
            "ENTER YOUR SENIOR ID NUMBER (LEAVE BLANK IF N/A): "
        )
        if (senior_id_no == "" 
                or senior_id_no.isdigit() 
                and len(senior_id_no) > 9 
                and len(senior_id_no) < 13):
            break

        print("INVALID INPUT. PLEASE ENTER 10-12 DIGITS OR LEAVE IT BLANK.")

    is_senior = is_senior_citizen(senior_id_no)

main()