from collections import deque

def is_palindrome(string):
    """Перевіряє, чи є рядок паліндромом."""
    # Видалити пробіли та привести рядок до нижнього регістру
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Створити двосторонню чергу
    char_deque = deque(cleaned_string)
    
    # Порівнювати символи з обох кінців
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не співпадають, це не паліндром
    
    return True  # Якщо всі символи співпали, це паліндром

# Тестування функції
if __name__ == "__main__":
    test_strings = [
        "А роза упала на лапу Азора",  # Паліндром
        "12321",                      # Паліндром
        "Python",                     # Не паліндром
        "Able was I, I saw Elba",     # Паліндром
        "Не паліндром"                # Не паліндром
    ]

    for s in test_strings:
        result = is_palindrome(s)
        print(f'"{s}" - {"паліндром" if result else "не паліндром"}')