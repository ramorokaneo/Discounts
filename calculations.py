def calculate_discount(price, discount_percent):
    # Calculate the final price after applying the discount
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
    else:
        # If discount is less than 20%, no discount is applied
        final_price = price

    # Add tax of 15% to the final price
    final_price_with_tax = final_price * 1.15

    # Return both final price without tax and with tax
    return final_price, final_price_with_tax

def main():
    # Prompt the user to enter the original price of the item
    original_price = float(input("Enter the original price of the item in ZAR: R"))

    # Define list of discount percentages to calculate final prices
    discount_percentages = [20, 30, 50, 75]

    # Iterate through each discount percentage
    for discount_percent in discount_percentages:
        # Calculate final price after applying discount and including tax
        final_price_without_tax, final_price_with_tax = calculate_discount(original_price, discount_percent)

        # Print final prices with currency symbol and discount percentage
        print(f"Final price with {discount_percent}% discount and without tax: R{final_price_without_tax:.2f}")
        print(f"Final price with {discount_percent}% discount and with tax: R{final_price_with_tax:.2f}\n")

if __name__ == "__main__":
    main()
