#TODO: Implement a function that adds an item to a products list
# Assigned to: Agulto, Jermaine Razehl

def is_senior_citizen(senior_id):
    if senior_id.isdigit() == True:
        return True
    else:
        return False

#TODO: Implement a function that totals the price of the items in the products 
# list.
# MUST Take into account the senior citizen discount
# Assigned to: Dazo, Rollan

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
    senior_id_no = input("ENTER YOUR SENIOR ID NUMBER (LEAVE BLANK IF N/A): ")

main()