current_queue = ""
queue_limit = 4
count = 0

while True:
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите посмотреть текущую очередь.")
    print(" - 3, если хотите прекратить работу программы и посмотреть получившуюся очередь.")
    print("-" * 50)

    choice = input()

    if choice == "1":
        patient_name = input("Введите ФИО пациента: ")
        # Форматирование ФИО
        parts = patient_name.split()
        formatted_name = " ".join([part[0].upper() + part[1:] if len(part) > 1 else part.upper() for part in parts])
        if count == 0:
            current_queue = formatted_name
        else:
            current_queue += f", {formatted_name}"
        count += 1
    elif choice == "2":
        if current_queue:
            print(f"Текущая очередь - {current_queue}")
        else:
            print("Очередь пустая!")
    elif choice == "3":
        break

if count == queue_limit:
    print("Очередь наполнена!")
print(f"Текущая очередь - {current_queue}")