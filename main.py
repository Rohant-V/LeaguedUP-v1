print("================================")
print("LEAGUED UP VERSION 1.0")
print("================================")
import tournaments.createT
import tournaments.showtour

while(1):
    print("1. create a new tournament")
    print("2. enter a tournament")
    print("3. view ongoing tournaments")
    print("4. exit")
    print("Enter your choice (1-3):")

    choice = int(input())
    if choice == 1:
        T=tournaments.createT.createT()
        tournaments.createT.save_tournament(T)
    elif choice == 2:
        print("soon")
    elif choice == 3:
        tournaments.showtour.showtour()
    elif choice == 4:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")