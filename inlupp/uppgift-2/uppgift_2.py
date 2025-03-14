# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(numbers): 
    return sum(numbers)
    summan = 0
    for num in numbers: 
        summan = summan + num
        return summan 

print(sum_list([1,2,3]))
print(sum_list([]))
print(sum_list([-1,-1,2]))
print(sum_list([1,2,3,4,5,6]))


