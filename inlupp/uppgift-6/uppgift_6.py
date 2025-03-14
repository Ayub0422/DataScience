# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def filter_odd(numbers):
    """
    Returnerar en lista med alla jämna tal från den givna listan.
    
    :param numbers: Lista med heltal
    :return: Lista med jämna tal
    """
    return [num for num in numbers if num % 2 == 0]

def multiplication_table(n, limit):
    """
    Returnerar multiplikationstabellen för n upp till limit i en lista.
    
    :param n: Heltal vars multiplikationstabell ska skapas
    :param limit: Det sista talet som ska multipliceras med n
    :return: Lista med multiplikationstabellen
    """
    return [n * i for i in range(1, limit + 1)]

# Exempelanvändning
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_odd(num_list)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Test av multiplikationstabell
n = 5
limit = 10
multiplication_result = multiplication_table(n, limit)
print(multiplication_result)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]