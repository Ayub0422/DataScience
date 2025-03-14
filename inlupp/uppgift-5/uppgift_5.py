# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

# def funktions_namn(variabel_namn: datatyp) -> returtyp:
    
def filter_odd(numbers):
    """
    Returnerar en lista med alla jämna tal från den givna listan.
    
    :param numbers: Lista med heltal
    :return: Lista med jämna tal
    """
    return [num for num in numbers if num % 2 == 0]

# Exempelanvändning
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_odd(num_list)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

