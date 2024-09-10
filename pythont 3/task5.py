current_queue = {}
queue_limit = 4

while True:
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите удалить пациента из очереди;")
    print(" - 3, если хотите посмотреть текущую очередь;")
    print(" - 4, если хотите прекратить работу программы и посмотреть получившуюся очередь.")
    print("-" * 50)

    choice = input()

    if choice == "1":
        time_and_name = input("Введите время и ФИО пациента (через запятую и пробел - \"08:00, Иванов А.А.\"): ")
        time, patient_name = time_and_name.split(", ")
        # Форматирование ФИО
        parts = patient_name.split()
        formatted_name = " ".join([part[0].upper() + part[1:] if len(part) > 1 else part.upper() for part in parts])
        
        if time in current_queue:
            print("Это время уже занято!")
        elif formatted_name in current_queue.values():
            print("Такой пациент уже есть в очереди!")
        else:
            current_queue[time] = formatted_name

    elif choice == "2":
        time_to_remove = input("Введите время пациента, которого нужно удалить из очереди (например, 08:00 или 10:15): ")
        if time_to_remove in current_queue:
            del current_queue[time_to_remove]
        else:
            print("Это время не занято!")

    elif choice == "3":
        if current_queue:
            print(f"Текущая очередь - {current_queue}")
        else:
            print("Очередь пустая!")

    elif choice == "4":
        break

if len(current_queue) == queue_limit:
    print("Очередь наполнена!")
print(f"Текущая очередь - {current_queue}")