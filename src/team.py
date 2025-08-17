from .player import Player
from .utils import get_simple_input

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.total_runs = 0

    def reset_scores(self):
        self.total_runs = 0
        for p in self.players:
            p.runs = 0

    def add_player(self, player):
        self.players.append(player)

    def input_players(self, num_players):
        for i in range(num_players):
            pname = get_simple_input(f"Enter name for player {i+1} in team {self.name}: ")
            self.add_player(Player(pname))

    def add_runs(self, player_idx, runs):
        self.players[player_idx].add_runs(runs)
        self.total_runs += runs

    def get_score(self):
        return self.total_runs

    def get_name(self):
        return self.name

    def get_top_players(self):
        return sorted(self.players, key=lambda p: p.get_runs(), reverse=True)
