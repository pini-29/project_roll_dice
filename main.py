import ui
import logic
from update_data import load_game_history

def main():
    while True:
        ui.show_menu()
        choice = input("Choose an option:")
        if choice == "1":
           logic.start_game()
        if choice == "2":
          listi_gaems = load_game_history()
          ui.display_game_history(listi_gaems)
        if choice == "3":
           statics = load_game_history()
           logic.display_statistics(statics)
        if choice == "4":
           break
          
        

        



main()