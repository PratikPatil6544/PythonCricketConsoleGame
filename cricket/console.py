import random
from .team import Team
from .tournament_manager import TournamentManager

def quick_team(name: str, size: int = 11) -> Team:
    t = Team(name)
    t._ensure_roster(size)
    return t

def main():
    random.seed()  # change seed each run

    print("====================================")
    print("  🏏 Cricket Tournament (Console)  ")
    print("====================================")

    names = ["Mumbai", "Pune", "Nagpur", "Nashik"]
    teams = [quick_team(n) for n in names]
    overs = 5

    tm = TournamentManager(teams, overs)

    while True:
        print("\nMenu:")
        print(" 1) 📅 Show schedule")
        print(" 2) ▶️  Play next match")
        print(" 3) ⏩ Simulate all matches")
        print(" 4) 👑 Play final")
        print(" 5) 📊 Show scoreboard")
        print(" 6) 🔁 Reset tournament")
        print(" 7) ❌ Quit")
        choice = input("Select option: ").strip()

        if choice == "1":
            tm.print_schedule()
        elif choice == "2":
            tm.play_next(show_animation=True)
        elif choice == "3":
            tm.simulate_all(show_animation=True)
        elif choice == "4":
            tm.play_final(show_animation=True)
        elif choice == "5":
            tm.show_scoreboard()
        elif choice == "6":
            tm.reset()
            print("🔁 Tournament reset.")
        elif choice == "7":
            print("Goodbye! 👋")
            break
        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()
