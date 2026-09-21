from tournaments.tournamentclass import Tournament
import json

def createT():
    name = input("Enter the name of the tournament: ")
    game = input("Enter the game of the tournament: ")
    T_size = int(input("Enter the size of the tournament: "))
    reg_fee = float(input("Enter the registration fee of the tournament: "))
    ppool = float(input("Enter the prize pool of the tournament: "))
    tournament = Tournament(name, game, T_size, reg_fee, ppool)
    print("Tournament created successfully!")

    return tournament

def save_tournament(tournament):
    tournament_data={
        "name" : tournament.name,
        "game" : tournament.game,
        "T_size" :tournament.T_size,
        "reg_fee" : tournament.reg_fee,
        "ppool": tournament.ppool
    }
    with open("tournament.json","r")as file:
        data=json.load(file)
    data.append(tournament_data)
    with open("tournament.json","w") as file:
        json.dump(data,file,indent=4)
