# main.py

from .tournament import TournamentManager
from .utils import get_integer_input

def main():
    tm = TournamentManager()
    tm.show_intro_message()
    tm.setup_tournament()

    # Show the winner once before the first menu after the final
    announced_winner = False

    while True:
        # If final finished, announce winner before showing the menu
        if tm.final_played and tm.final_winner and not announced_winner:
            print(f">>> Tournament Winner: {tm.final_winner} <<<")
            announced_winner = True

        # Build dynamic menu
        print("\n===== CRICKET TOURNAMENT MENU =====")
        print("1. Show Scoreboard")
        print("2. Show Teams and Players")

        if tm.league_fixtures:
            opt3 = "Play Next Match"
        elif not tm.final_played:
            opt3 = "Play Final"
        else:
            opt3 = "Restart Tournament"
        print(f"3. {opt3}")

        # Show option 4 only while league matches remain
        show_opt4 = bool(tm.league_fixtures)
        if show_opt4:
            print("4. Simulate Remaining Matches")

        print("0. Exit")

        max_choice = 4 if show_opt4 else 3
        choice = get_integer_input("Enter choice: ", 0, max_choice)

        if choice == 1:
            tm.show_scoreboard()
        elif choice == 2:
            tm.show_teams_and_players()
        elif choice == 3:
            if tm.league_fixtures:
                tm.play_next_match()
            elif not tm.final_played:
                tm.play_final()
            else:
                # Restart tournament: reset the announcement flag too
                tm.show_intro_message()
                tm.setup_tournament()
                announced_winner = False
        elif choice == 4 and show_opt4:
            tm.simulate_remaining_league()
        elif choice == 0:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
