import json
DATA_PATH = "game_history.json"
list_of_games = []
dict_of_game={"player_name":None,"rounds":0,"player_score":0,"computer_score":0,"winner":None,"results":[]}
dict_of_round={"round":0,"player_dice":0,"computer_dice":0,"winner":None}
def save_game(game: list):
    with open(DATA_PATH,"w",encoding="utf-8") as file:
        json.dump(game, file, indent=2, ensure_ascii=False)

def load_game_history():
    try:
       with open(DATA_PATH, "r", encoding="utf-8") as file:
           data = json.load(file) 
           return data
    except FileNotFoundError as e:
       print (f"{e} יש שגיאה במציאת הקובץ")
