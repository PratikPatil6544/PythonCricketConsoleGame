import random
import time
from enum import Enum
from typing import Optional
from .team import Team

class MatchType(Enum):
    Normal = 1
    Final = 2

class Match:
    def __init__(self, mtype: MatchType, teamA: Team, teamB: Team, overs: int):
        self.mtype = mtype
        self.teamA = teamA
        self.teamB = teamB
        self.overs = overs
        self._winner: Optional[Team] = None
        self._tied: bool = False
        self._runsA = 0
        self._runsB = 0

    def getMatchInfo(self) -> str:
        tag = "Final" if self.mtype == MatchType.Final else "Match"
        return f"{self.teamA.getName()} vs {self.teamB.getName()} ({tag})"

    def simulate(self, show_animation: bool = True):
        self.teamA._ensure_roster()
        self.teamB._ensure_roster()

        if show_animation:
            self._loading_animation(f"Simulating {self.teamA.getName()} vs {self.teamB.getName()} 🏏")

        low, high = 2 * self.overs, 12 * self.overs
        self._runsA = random.randint(low, high)
        self._runsB = random.randint(low, high)

        # Small tie nudge
        if random.random() < 0.08:
            self._runsB = self._runsA

        self._distribute_runs(self.teamA, self._runsA)
        self._distribute_runs(self.teamB, self._runsB)

        self.teamA.addRuns(self._runsA)
        self.teamB.addRuns(self._runsB)

        if self._runsA > self._runsB:
            self._winner = self.teamA
        elif self._runsB > self._runsA:
            self._winner = self.teamB
        else:
            self._tied = True

        result = "🤝 Tie" if self._tied else f"🏆 {self._winner.getName()}"
        print(f"Result: {self.teamA.getName()} {self._runsA} / {self.teamB.getName()} {self._runsB} → {result}")

    def isMatchTied(self) -> bool:
        return self._tied

    def getWinner(self) -> Optional[Team]:
        return self._winner

    def _distribute_runs(self, team: Team, total: int):
        weights = [1.6, 1.5, 1.4, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5][:len(team.players)]
        s = sum(weights) if weights else 1.0
        allocated = 0
        for i, p in enumerate(team.players):
            share = int(total * (weights[i] / s))
            p.runs += share
            allocated += share
        if team.players and allocated < total:
            team.players[0].runs += total - allocated

    def _loading_animation(self, text: str):
        print(text, end="", flush=True)
        for _ in range(6):
            print(".", end="", flush=True)
            time.sleep(0.2)
        print()
