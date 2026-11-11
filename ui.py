def show_menu():
    print("================================")
    print("           ROLL DICE            ")
    print("================================")

    print("1. Start New Game")
    print("2. View Game History")
    print("3. View Statistics")
    print("4. Exit")


def display_game_history(history: list):
    
    for dicti in history:
        if len(dicti) == 0:
                print("Have a zero games")
        print (f""" player_name: {dicti["player_name"]}, rounds: {dicti["rounds"]},
                    player_score: {dicti["player_score"]}, computer_score: {dicti["computer_score"]},
                    winner: {dicti["winner"]}""")
