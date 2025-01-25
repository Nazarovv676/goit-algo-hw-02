def check_brackets(expression):
    """Перевіряє симетричність дужок у рядку."""
    stack = []  # Стек для відкритих дужок
    brackets = {')': '(', '}': '{', ']': '['}  # Пара відкритих і закритих дужок
    
    for char in expression:
        if char in brackets.values():  # Якщо це відкрита дужка
            stack.append(char)
        elif char in brackets.keys():  # Якщо це закрита дужка
            if stack and stack[-1] == brackets[char]:  # Перевіряємо, чи відповідає пара
                stack.pop()  # Видаляємо відкриту дужку зі стека
            else:
                return "Несиметрично"  # Якщо пари немає, рядок несиметричний

    # Якщо стек порожній після перевірки, всі дужки симетричні
    return "Симетрично" if not stack else "Несиметрично"

# Тестування програми
if __name__ == "__main__":
    test_expressions = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",  # Симетрично
        "( 23 ( 2 - 3);",            # Несиметрично
        "( 11 }",                    # Несиметрично
        "((()))",                    # Симетрично
        "[{()}]",                    # Симетрично
        "({[})",                     # Несиметрично
    ]

    for expr in test_expressions:
        result = check_brackets(expr)
        print(f'"{expr}": {result}')