"""
      Pack The Car
      Jimmy McCue
      Program Prints number of Items in the car and prints a sorted list
      05-29-2025
"""
#	Challenge: You plan to go camping and packing the car. Create a list of 
# strings that are items you’re taking with you, for example “tent poles”.
# Print the number of items you have in your car. You will need a lot of things 
# so include 10 items. Print the sorted list.

camping_supplies = ['tent poles', 'firewood', 'matches', 'sleeping bags', 'snacks', 'drinks', 
                    'chairs', 'pillows', 'clothes', 'boots']

camping_supplies.sort()

print(len(camping_supplies))
print(camping_supplies)