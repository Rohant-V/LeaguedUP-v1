print("================================")
print("LEAGUED UP VERSION 1.0")
print("================================")
from tournaments.configtournament import run_config_menu
while(1):
    print("1. Host Tournament")
    print("2. register for Tournament")
    print("3. Exit")

    input_choice = int(input("Enter your choice (1-3): "))

    if input_choice == 1:
        run_config_menu()
    elif input_choice == 2:
        print("Registering for tournament...")
    elif input_choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")