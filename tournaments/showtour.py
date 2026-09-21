from tournaments.createT import createT
import json
def showtour():
    with open ("tournament.json","r") as file:
        tournament_data = json.load(file)
        for tournament in tournament_data:
            print("Tournament Name:", tournament["name"])
            print("Game:", tournament["game"])
            print("Tournament Size:", tournament["T_size"])
            print("Registration Fee:", tournament["reg_fee"])
            print("Prize Pool:", tournament["ppool"])
            print("-------------------------")
