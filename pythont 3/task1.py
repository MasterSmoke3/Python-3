current_queue = ""
queue_limit = 4
count = 0

while count < queue_limit:
    print("-" * 50)
    print("Введите:")
    print(" - 1, если хотите добавить пациента в очередь;")
    print(" - 2, если хотите посмотреть текущую очередь.")
    print("-" * 50)

    choice = input()

    if choice == "1":
        patient_name = input("Введите ФИО пациента: ")
        if count == 0:
            current_queue = patient_name
        else:
            current_queue += f", {patient_name}"
        count += 1
    elif choice == "2":
        print(f"Текущая очередь - {current_queue}")

print(f"Текущая очередь - {current_queue}")