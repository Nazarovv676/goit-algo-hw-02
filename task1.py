import queue
import random
import time

# Створити чергу заявок
requests_queue = queue.Queue()

# Унікальний номер для заявок
request_id = 1

def generate_request():
    """Функція для створення нової заявки та додавання її до черги."""
    global request_id
    request = f"Заявка #{request_id}"
    requests_queue.put(request)
    print(f"Створено: {request}")
    request_id += 1

def process_request():
    """Функція для обробки заявок із черги."""
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Обробляється: {request}")
        # Імітація часу обробки заявки
        time.sleep(1)
        print(f"Оброблено: {request}")
    else:
        print("Чергa порожня. Немає заявок для обробки.")

def main():
    """Головний цикл програми."""
    print("Програма для обробки заявок.")
    print("Для виходу натисніть Ctrl+C.\n")
    
    # Створення початкових заявок
    generate_request()
    generate_request()
    generate_request()
    
    try:
        while True:
            # Імітація генерації нових заявок
            if random.random() > 0.5:  # 50% шанс створення нової заявки
                generate_request()
            
            # Обробка заявок
            process_request()

            # Затримка перед наступною ітерацією
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nПрограма завершена.")

# Запуск програми
if __name__ == "__main__":
    main()