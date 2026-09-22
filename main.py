print("================================")
print("LEAGUED UP VERSION 1.0")
print("================================")
from tournaments import createT, showtour, edittournament, deletetournament

while(1):
    print("1. create a new tournament")
    print("2. enter a tournament")
    print("3. view ongoing tournaments")
    print("4. edit tournament")
    print("5. delete tournament")
    print("6. exit")
    print("Enter your choice (1-6):")

    choice = int(input())
    if choice == 1:
        T=createT.createT()
        createT.save_tournament(T)
    elif choice == 2:
        print("soon")
    elif choice == 3:
        showtour.showtour()
    elif choice == 4:
        edittournament.edit_tournament()
    elif choice == 5:
        deletetournament.delete_tournament()
    elif choice == 6:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")