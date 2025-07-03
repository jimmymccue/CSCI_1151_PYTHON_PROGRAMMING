# Instructions:
# 1. Add a try...except block within the 'calculate_average' function
#    to handle TypeError when elements in the list are not numbers.
# 2. Within the same try...except block, if a TypeError occurs,
#    convert the non-numeric element to 0 and continue the calculation.
# 3. Add a try...except block in the 'process_data' function to handle
#    ZeroDivisionError when 'calculate_average' returns None.
# 4. If a ZeroDivisionError occurs in 'process_data', print a message
#    indicating that the data list resulted in a division by zero.
# 5. Why: Demonstrates handling multiple exception types,
#    error recovery, and preventing program crashes in data processing.




def calculate_average(data: list[float]) -> float:
    """Calculates the average of a list of numbers.

    Args:
        data (list[float]): A list of numbers.

    Raises: 
        TypeError: if an element is not a number
        ZeroDivisionError: if data is empty 
           
    Returns:
        The average of the numbers in the list, or zero if all elements are converted to 0.
    """
    total = 0
    for item in data:
        total += item
    return total / len(data)


def process_data(data_list: list[float | int | str]) -> None:
    """Processes a list of data lists and calculates their averages.

    Args:
        data_list: A list of lists, where each inner list contains numbers
                   or other types that may cause errors.
    
    """
    for data in data_list:
        average = calculate_average(data)
        print(f"Average: {average}")




data_set = [
    [1, 2, 3], 
    [4, "five", 6], 
    [], 
    [0.2, 5.9]
    ]

process_data(data_set)


