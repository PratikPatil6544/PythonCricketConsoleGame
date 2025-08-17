from typing import List
from .player import Player

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []
        self._total_runs = 0

    def getName(self) -> str:
        return self.name

    def getScore(self) -> int:
        return self._total_runs

    def getTopPlayers(self, n: int = 3) -> List[Player]:
        return sorted(self.players, key=lambda p: p.runs, reverse=True)[:n]

    def addRuns(self, runs: int):
        self._total_runs += runs

    def _ensure_roster(self, size: int = 11):
        if not self.players:
            self.players = [Player(f"{self.name} Player {i+1}") for i in range(size)]
