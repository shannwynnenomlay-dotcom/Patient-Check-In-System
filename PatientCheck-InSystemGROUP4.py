patients = {}

print('WELCOME TO CHECK-IN SYSTEM')

while True:
    print('\n What should we do?')
    print('1 Add New Patient')
    print('2 Check In Patient')
    print('3 See all Patient')
    print('4 Exit')

    choice = input('\n Enter your Choices 1-4:')
    
    if choice == "1":
        while True:
            print('\n ADD NEW PATIENT ')

            name = input('Enter Patient Name: ')
            patient_id = input('Enter Patient ID: ')

            if not patient_id.isdigit():
                print("\n INVALID! ID must contain numbers!")
                continue
        
            patients[patient_id] = {
                "name": name,
                "status": "NOT YET"
            }
            print(f" I Added {name} Successfully")

            again = input("\n Add another patient? YES or NO: ").upper()
            if again != "YES":
                print("\n Returning...")
                break
        
    elif choice == "2":
        print("\n CHECK IN PATIENT ")
        patient_id = input("Enter Patient ID:")

        if patient_id in patients:
            patients[patient_id]["status"] = "CHECKED IN!"
            print(f"{patients[patient_id]['name']} is now checked in!")
        else:
            print('Not Found, Please add Patient')

    elif choice == "3":
        print('\n -ALL PATIENTS- ')

        if not patients:
            print('No Patients Found')
        else:
            for pid, info in patients.items():
                print(f"ID: {pid} | Name: {info['name']} | {info['status']}")

    elif choice == "4":
        print("\n Thank You!")
        break

    else:
        print("\n INVALID! please Enter 1,2,3, and 4 ONLY!")
