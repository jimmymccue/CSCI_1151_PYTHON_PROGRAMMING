"""
    Tip Calculator
      Jimmy McCue
      The program calculates and prints out tips for 15 and 20 percent
      05-28-2025

"""

# 1.	You are the owner of a restaurant. Ask one of your employees to write a program which
#     takes a total from a bill for dinner and prints out suggestions for a 15% tip and 20% tip. 
#     Then gives the total for the meal with the 15% tip and another with the 20% tip. Use F-strings.

restaurant_name = "Jimmy's Restaurant"
bill_subtotal = 85.00
TAX = .07
bill_tax = bill_subtotal * TAX
bill_total = bill_subtotal + bill_tax
reciept_line = "----------------------------------"
tip_15 = .15
tip_20 = .20

print(f"\n\t{restaurant_name}")
print(reciept_line)
print(f"Subtotal = {bill_subtotal}")
print(f"Tax      = {bill_tax}\n")
print(f"Total    = {bill_total}")
print(reciept_line)
print("Suggested Gratuity:\n")
print(f"15% - {bill_subtotal * tip_15}\tTotal: {bill_total + bill_subtotal *tip_15}")
print(f"20% - {bill_subtotal * tip_20}\tTotal: {bill_total + bill_subtotal *tip_20}")

