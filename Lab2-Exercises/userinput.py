#Write a Python program that prompts the user for his/her amount of money, then
#reports how many Nintendo Wiis the person can afford, and how much more money he/she
#will need to afford an additional Wii.

# Price of one Nintendo Wii
wii_price = 300

# Ask the user for their amount of money
money = float(input("Enter the amount of money you have: $"))

# Calculate how many Wiis the person can afford
num_wiis_affordable = money // wii_price

# Calculate how much more money is needed for an additional Wii
money_needed_for_next_wii = wii_price - (money % wii_price)

# Display the results
print(f"With ${money:.2f}, you can afford {int(num_wiis_affordable)} Nintendo Wiis.")
print(f"To afford an additional Wii, you need ${money_needed_for_next_wii:.2f}.")
