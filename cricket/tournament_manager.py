import random
from typing import List, Dict
from .team import Team
from .match import MatchType
from .factory import MatchFactory

class TournamentManager:
    def __init__(self, teams: List[Team], overs: int):
        self.teams = teams
        self.overs = overs
        self.matches = []
        self.results: List[str] = []
        self.points: Dict[str, int] = {}
        self.finalPlayed = False
        self._schedule_round_robin()

    def _schedule_round_robin(self):
        pairs = []
        n = len(self.teams)
        for i in range(n):
            for j in range(i + 1, n):
                pairs.append((self.teams[i], self.teams[j]))
        random.shuffle(pairs)
        for a, b in pairs:
            self.matches.append(MatchFactory.create(MatchType.Normal, a, b, self.overs))

    def print_schedule(self):
        print("\n📅 Match Schedule")
        print("-" * 40)
        for m in self.matches:
            print(f" - {m.getMatchInfo()}")

    def play_next(self, show_animation: bool = True):
        if not self.matches:
            print("No more matches to play.")
            return
        match = self.matches.pop(0)
        match.simulate(show_animation=show_animation)
        if match.isMatchTied():
            a, b = match.teamA.getName(), match.teamB.getName()
            self.points[a] = self.points.get(a, 0) + 1
            self.points[b] = self.points.get(b, 0) + 1
            self.results.append(f"{a} vs {b} → 🤝 Tie")
        else:
            w = match.getWinner().getName()
            self.points[w] = self.points.get(w, 0) + 2
            self.results.append(f"{match.teamA.getName()} vs {match.teamB.getName()} → 🏆 {w}")

    def simulate_all(self, show_animation: bool = True):
        while self.matches:
            self.play_next(show_animation=show_animation)

    def play_final(self, show_animation: bool = True):
        if self.finalPlayed or len(self.teams) < 2:
            self.finalPlayed = True
            return
        ranked = sorted(self.teams, key=lambda t: (self.points.get(t.getName(), 0), t.getScore()), reverse=True)
        final = MatchFactory.create(MatchType.Final, ranked[0], ranked[1], self.overs)
        final.simulate(show_animation=show_animation)
        if final.isMatchTied():
            self.results.append(f"{final.teamA.getName()} vs {final.teamB.getName()} (Final) → 🤝 Tie")
        else:
            self.results.append(f"{final.teamA.getName()} vs {final.teamB.getName()} (Final) → 👑 {final.getWinner().getName()}")
        self.finalPlayed = True

    def show_scoreboard(self):
        print("\n📊 Scoreboard")
        print("-" * 40)
        print("Results:")
        for r in self.results:
            print(f" - {r}")
        print("\nPoints Table:")
        for t in self.teams:
            pts = self.points.get(t.getName(), 0)
            print(f" - {t.getName():15} {pts} pts | Runs: {t.getScore()}")
        if self.finalPlayed:
            winner = self.get_winner_name()
            if winner:
                print(f"\n🏆 Tournament Winner: {winner}")

    def show_teams(self):
        print("\n🧢 Teams & Top Players")
        print("-" * 40)
        for t in self.teams:
            print(f"{t.getName()}:")
            for p in t.getTopPlayers(3):
                print(f"  • {p.getName()} — {p.getRuns()} runs")

    def get_winner_name(self) -> str:
        ranked = sorted(self.teams, key=lambda t: (self.points.get(t.getName(), 0), t.getScore()), reverse=True)
        return ranked[0].getName() if ranked else ""

    def reset(self):
        self.matches.clear()
        self.results.clear()
        self.points.clear()
        self.finalPlayed = False
        self._schedule_round_robin()
