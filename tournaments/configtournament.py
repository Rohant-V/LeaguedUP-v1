from tournaments import createT, showtour, edittournament, deletetournament
def run_config_menu():

    print("================================")
    print("CONFIGURATION MENU")
    print("================================")

    while True:
        print("1. Create a new tournament")
        print("2. View ongoing tournaments")
        print("3. Edit tournament")
        print("4. Delete tournament")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            T = createT.createT()
            createT.save_tournament(T)
        elif choice == 2:
            showtour.showtour()
        elif choice == 3:
            edittournament.edit_tournament()
        elif choice == 4:
            deletetournament.delete_tournament()
        elif choice == 5:
            print("Exiting the configuration menu...")
            break
