# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        final_price = price - (price * discount_percentage / 100)
        return final_price
    else:
        return price


# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
    

original_price = int(input("Price of an item: "))
discount_price = int(input("Discount Price: "))
final_price = calculate_discount(original_price, discount_price)

print(f"The final price is: {final_price}")