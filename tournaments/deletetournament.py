import json
def delete_tournament():
    tournament_name = input("Enter the name of the tournament you want to delete: ")
    with open("tournament.json", "r") as file:
        tournament_data = json.load(file)
    
    for tournament in tournament_data:
        if tournament["name"] == tournament_name:
            tournament_data.remove(tournament)
            print("Tournament deleted successfully!")
            break
    else:
        print("Tournament not found.")

    with open("tournament.json", "w") as file:
        json.dump(tournament_data, file, indent=4)