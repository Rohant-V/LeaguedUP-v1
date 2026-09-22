import json
def edit_tournament():
    tournament_name = input("Enter the name of the tournament you want to edit: ")
    with open("tournament.json", "r") as file:
        tournament_data = json.load(file)
    
    for tournament in tournament_data:
        if tournament["name"]== tournament_name:
            print("Tournament Name:", tournament["name"])
            print("Game:", tournament["game"])
            print("Tournament Size:", tournament["T_size"])
            print("Registration Fee:", tournament["reg_fee"])
            print("Prize Pool:", tournament["ppool"])
            print("-------------------------")

        new_name = input("Enter the new name of the tournament: ")
        new_game = input("Enter the new game of the tournament: ")
        new_T_size = int(input("Enter the new size of the tournament: "))
        new_reg_fee = float(input("Enter the new registration fee of the tournament: "))
        new_ppool = float(input("Enter the new prize pool of the tournament: "))

        if new_name:
            tournament["name"] = new_name
        if new_game:
            tournament["game"] = new_game
        if new_T_size:
            tournament["T_size"] = new_T_size
        if new_reg_fee:
            tournament["reg_fee"] = new_reg_fee
        if new_ppool:
            tournament["ppool"] = new_ppool

    with open("tournament.json","w") as file:
        json.dump(tournament_data,file,indent=4)