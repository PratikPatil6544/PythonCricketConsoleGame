import random
from .team import Team
from .utils import get_simple_input, get_integer_input

class TournamentManager:
    def __init__(self):
        self.teams = []
        self.points_table = {}
        self.match_results = []
        self.league_fixtures = []  # list of (i, j) team indices
        self.num_players = 0
        self.num_overs = 0
        self.final_played = False
        self.final_pair = None
        self.final_winner = None

    # -------------------- Setup & intro --------------------

    def show_intro_message(self):
        print()
        print("=========== IAV - CRICKET TOURNAMENT ===========")
        print()
        print("Welcome to the IAV Cricket Simulator!")
        print()
        print("Games are simulated, so random runs will be generated.")
        print("The team with the highest score wins each match.")
        print("1 match win = 2 points.")
        print("If match is tied, both teams get 1 point.")
        print("If two teams have equal points, the team with")
        print("the highest total score will qualify for the final.")
        print()
        print("Instructions:")
        print("1. Enter number of teams")
        print("2. Enter number of players per team")
        print("3. Enter number of overs")
        print("4. Enter name for each team")
        print("5. Enter name for each player in every team")
        print()
        print("Tournament matches are scheduled randomly")
        print("so that each team plays the same number of matches.")
        print()
        print("Menu Options:")
        print("1. Show Scoreboard - Displays match results, points table, and top players")
        print("2. Show Teams and Players - Lists all teams and their players")
        print("3. Play Next Match / Final / Restart")
        print("4. Simulate Remaining Matches")
        print("0. Exit - Ends the program")
        print()
        print("================ TOURNAMENT START ================")
        print()

    def setup_tournament(self):
        self.teams.clear()
        self.points_table.clear()
        self.match_results.clear()
        self.league_fixtures.clear()
        self.final_played = False
        self.final_pair = None
        self.final_winner = None

        num_teams = get_integer_input("Enter number of teams: ", 2, 20)
        self.num_players = get_integer_input("Enter number of players per team: ", 3, 11)
        self.num_overs = get_integer_input("Enter number of overs: ", 1, 50)

        for i in range(num_teams):
            tname = get_simple_input(f"Enter name for team {i+1}: ")
            team = Team(tname)
            team.input_players(self.num_players)
            self.teams.append(team)
            self.points_table[tname] = 0

        self._build_random_round_robin_fixtures()

    def _build_random_round_robin_fixtures(self):
        pairs = []
        n = len(self.teams)
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append((i, j))
        random.shuffle(pairs)
        self.league_fixtures = pairs

    # -------------------- Simulation --------------------

    def _simulate_innings(self, team):
        choices = [0, 1, 2, 3, 4, 6]
        weights = [10, 30, 22, 6, 20, 12]  # sums arbitrary; favors 1s/2s/4s
        player_idx = 0
        balls = self.num_overs * 6

        team.reset_scores()

        for _ in range(balls):
            runs = random.choices(choices, weights=weights, k=1)[0]
            team.add_runs(player_idx, runs)
            player_idx = (player_idx + 1) % len(team.players)

    def _play_head_to_head(self, team_a, team_b):
        self._simulate_innings(team_a)
        score_a = team_a.get_score()

        self._simulate_innings(team_b)
        score_b = team_b.get_score()

        if score_a > score_b:
            self.points_table[team_a.get_name()] += 2
            outcome = f"{team_a.get_name()} won"
        elif score_b > score_a:
            self.points_table[team_b.get_name()] += 2
            outcome = f"{team_b.get_name()} won"
        else:
            self.points_table[team_a.get_name()] += 1
            self.points_table[team_b.get_name()] += 1
            outcome = "Draw"

        return score_a, score_b, outcome

    def play_next_match(self):
        if self.league_fixtures:
            i, j = self.league_fixtures.pop(0)
            team_a = self.teams[i]
            team_b = self.teams[j]
            score_a, score_b, outcome = self._play_head_to_head(team_a, team_b)
            result_line = f"{team_a.get_name()} vs {team_b.get_name()} → {outcome}"
            self.match_results.append(result_line)
            print(f"Played: {result_line} ({score_a} - {score_b})")
            return

        if not self.final_played:
            self.play_final()
            return

        print("No more matches to play. Tournament finished.")

    def simulate_remaining_league(self):
        while self.league_fixtures:
            self.play_next_match()
        if not self.league_fixtures and not self.final_played:
            print("All league matches completed. Use option 3 to Play Final.")

    def _rank_teams_for_final(self):
        return sorted(
            self.teams,
            key=lambda t: (self.points_table[t.get_name()], t.get_score()),
            reverse=True,
        )

    def play_final(self):
        if self.final_played:
            print("Final already played.")
            return

        if self.league_fixtures:
            print("League not finished. Simulate remaining matches first.")
            return

        ranked = self._rank_teams_for_final()
        if len(ranked) < 2:
            print("Not enough teams to play the final.")
            return

        a, b = ranked[0], ranked[1]
        self.final_pair = (a, b)
        print(f"\nFINAL → {a.get_name()} vs {b.get_name()}")

        score_a, score_b, outcome = self._play_head_to_head(a, b)

        if outcome == "Draw":
            winner = a if a.get_score() >= b.get_score() else b
        else:
            winner = a if outcome.startswith(a.get_name()) else b

        self.final_winner = winner.get_name()
        self.final_played = True

        self.match_results.append(
            f"FINAL: {a.get_name()} vs {b.get_name()} → Winner {self.final_winner}"
        )

        print(f"FINAL → Winner: {self.final_winner}")
        print(f"Final Score: {a.get_name()} {score_a} - {b.get_name()} {score_b}")

    def get_winner_name(self):
        if self.final_played and self.final_winner:
            return self.final_winner
        # Before final, the current table leader:
        ranked = self._rank_teams_for_final()
        return ranked[0].get_name() if ranked else ""

    # -------------------- Displays --------------------

    def show_scoreboard(self):
        print("\n==================== SCOREBOARD ====================")

        print("\nMatch Results:")
        print("-------------------------------------------------------------")
        print("{:<30}|| {}".format("Match", "Result"))
        print("-------------------------------------------------------------")
        if not self.match_results:
            print("{:<30}|| {}".format("-", "No matches played yet"))
        else:
            for result in self.match_results:
                parts = result.split(" → ")
                match_name = parts[0]
                outcome = parts[1] if len(parts) > 1 else ""
                print("{:<30}|| {}".format(match_name, outcome))
        print("-------------------------------------------------------------")

        print("\nPoints Table:")
        print("-------------------------------------------------------------")
        print("{:<20}|| {:<9}|| {}".format("Team Name", "Points", "Total Runs"))
        print("-------------------------------------------------------------")
        for team in sorted(
            self.teams,
            key=lambda t: (self.points_table[t.get_name()], t.get_score()),
            reverse=True,
        ):
            points = self.points_table.get(team.get_name(), 0)
            print("{:<20}|| {:<9}|| {}".format(team.get_name(), points, team.get_score()))
        print("-------------------------------------------------------------")

        print("\nTop Players:")
        print("-------------------------------------------------------------")
        print("{:<20}|| {:<20}|| {}".format("Team", "Player", "Runs"))
        print("-------------------------------------------------------------")
        for team in self.teams:
            for player in team.get_top_players():
                print("{:<20}|| {:<20}|| {}".format(team.get_name(), player.get_name(), player.get_runs()))
        print("-------------------------------------------------------------")

        if self.final_played and self.final_winner:
            print(f"\n>>> Tournament Winner: {self.final_winner} <<<")

        print("===============================================================")

    def show_teams_and_players(self):
        print("\n==================== TEAMS & PLAYERS ====================")
        for team in self.teams:
            print(f"\nTeam: {team.get_name()}")
            for idx, player in enumerate(team.players, start=1):
                print(f"  {idx}. {player.get_name()}")
        print("=========================================================")
