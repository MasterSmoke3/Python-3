current_queue = []
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
        print("-" * 50)
        print("Введите:")
        print(" - 1, если хотите добавить пациента в конец очереди;")
        print(" - 2, если хотите добавить пациента в начало или середину очереди.")
        print("-" * 50)

        add_choice = input()
        patient_name = input("Введите ФИО пациента: ")
        # Форматирование ФИО
        parts = patient_name.split()
        formatted_name = " ".join([part[0].upper() + part[1:] if len(part) > 1 else part.upper() for part in parts])

        if formatted_name in current_queue:
            print("Такой пациент уже есть в очереди!")
        else:
            if add_choice == "1":
                current_queue.append(formatted_name)
            elif add_choice == "2":
                if len(current_queue) == queue_limit:
                    print("Очередь уже заполнена!")
                else:
                    position = int(input("Введите на какое место очереди хотите вставить пациента: ")) - 1
                    if 0 <= position <= len(current_queue):
                        current_queue.insert(position, formatted_name)
                    else:
                        print("Некорректный номер места в очереди!")

    elif choice == "2":
        print("-" * 50)
        print("Введите:")
        print(" - 1, если хотите удалить пациента по ФИО;")
        print(" - 2, если хотите удалить пациента по его номеру в очереди.")
        print("-" * 50)

        remove_choice = input()

        if remove_choice == "1":
            patient_to_remove = input("Введите ФИО пациента: ")
            # Форматирование ФИО
            parts = patient_to_remove.split()
            formatted_name = " ".join([part[0].upper() + part[1:] if len(part) > 1 else part.upper() for part in parts])
            if formatted_name in current_queue:
                current_queue.remove(formatted_name)
            else:
                print("Такого пациента нет в очереди!")

        elif remove_choice == "2":
            position = int(input("Введите порядковый номер человека в очереди: ")) - 1
            if 0 <= position < len(current_queue):
                del current_queue[position]
            else:
                print("Такого порядкового номера нет в очереди!")

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