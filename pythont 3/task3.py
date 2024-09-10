current_queue = set()
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
        patient_name = input("Введите ФИО пациента: ")
        # Форматирование ФИО
        parts = patient_name.split()
        formatted_name = " ".join([part[0].upper() + part[1:] if len(part) > 1 else part.upper() for part in parts])
        current_queue.add(formatted_name)

    elif choice == "2":
        patient_to_remove = input("Введите ФИО пациента, которого надо удалить из очереди: ")
        # Форматирование ФИО
        parts = patient_to_remove.split()
        formatted_name = " ".join([part[0].upper() + part[1:] if len(part) > 1 else part.upper() for part in parts])
        if formatted_name in current_queue:
            current_queue.remove(formatted_name)
        else:
            print("Такого пациента нет в очереди!")

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