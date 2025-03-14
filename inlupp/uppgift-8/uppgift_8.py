# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

import re

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

def validate_password(password):
    """
    Kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    
    :param password: Sträng som representerar lösenordet
    :return: True om lösenordet är giltigt, annars False
    """
    return len(password) >= 8 and bool(re.search(r'\d', password))

def count_letters(string):
    """
    Returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    
    :param string: Sträng vars bokstäver ska räknas
    :return: Dictionary med bokstäver och deras frekvens
    """
    letter_count = {}
    for char in string:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

# Exempelanvändning
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_odd(num_list)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Test av multiplikationstabell
n = 5
limit = 10
multiplication_result = multiplication_table(n, limit)
print(multiplication_result)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Test av lösenordsvalidering
password = "secure123"
print(validate_password(password))  # Output: True

password = "short1"
print(validate_password(password))  # Output: False

# Test av count_letters
text = "hello world"
print(count_letters(text))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}