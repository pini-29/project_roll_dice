import random
import update_data
import validition
def roll_dice():
    return random.randint(1,6)


def play_round(i,name):
          dict_of_round={"round":0,"player_dice":0,"computer_dice":0,"winner":None}
          player = roll_dice()
          computer = roll_dice()
          win_name = name
          

          if player > computer:
            win_name = name
            update_data.dict_of_game["player_score"] += 1
          elif player < computer:
            win_name = "Computer"
            update_data.dict_of_game["computer_score"] += 1
          elif player == computer:
            win_name = "Draw"
          print(f"---------- ROUND {i+1} ----------")
          print(f" {name}:    🎲 {player}")
          print(f"Computer: 🎲 {computer} ")
          print(f"{win_name} wins this round!")
          update_data.dict_of_round["round"]=i + 1
          update_data.dict_of_round["player_dice"]=player
          update_data.dict_of_round["computer_dice"]=computer
          update_data.dict_of_round["winner"]=win_name
          update_data.dict_of_game["results"].append(update_data.dict_of_round)

def start_game():
      dict_of_game={"player_name":None,"rounds":0,"player_score":0,"computer_score":0,"winner":None,"results":[]}

      name = validition.get_name()
    

      rounds = validition.get_num()
      for i in range(rounds):
          play_round(i,name)
      update_data.dict_of_game["player_name"] = name
      update_data.dict_of_game["rounds"] = rounds
      if update_data.dict_of_game["player_score"] > update_data.dict_of_game["computer_score"]:
          update_data.dict_of_game["winner"] = name
      elif update_data.dict_of_game["player_score"] < update_data.dict_of_game["computer_score"]:
          update_data.dict_of_game["winner"] = "computer"
      
      if update_data.dict_of_game["player_score"] > update_data.dict_of_game["computer_score"]:
          print (f"WINNER: {name}")
      elif update_data.dict_of_game["player_score"] < update_data.dict_of_game["computer_score"]:
          print(f"WINNER: computer")
      
     
      update_data.list_of_games.append(update_data.dict_of_game)
      update_data.save_game(update_data.list_of_games)
      
      print ("Game saved successfully!")

def display_statistics(history: list):
    player_win = 0
    computer_win = 0
    draw_win = 0
    games = len(history)
    for dicti in history:
        if dicti["winner"] == "Computer":
            computer_win += 1
        elif dicti["winner"] == None:
            draw_win += 1
        else:
            player_win += 1
    print (f"""the statics is:
               playes of play: {games}
               players win:{player_win}
               computer win:{computer_win}
               the draw: {draw_win}
""")
               
        
       


                    



    
          



   

