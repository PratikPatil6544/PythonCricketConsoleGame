# tests/cricket_console_library.py
from typing import List
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cricket.team import Team
from cricket.tournament_manager import TournamentManager

class CricketConsoleLibrary:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self):
        self._teams: List[Team] = []
        self._tm: TournamentManager | None = None

    def create_teams(self, *names: str):
        """Create team objects with auto-filled rosters."""
        self._teams = [Team(n) for n in names]
        for t in self._teams:
            t._ensure_roster()

    def create_tournament(self, overs: int = 5):
        """Initialize the tournament with the prepared teams."""
        if not self._teams:
            raise ValueError("No teams created. Use `Create Teams` first.")
        self._tm = TournamentManager(self._teams, int(overs))

    def print_schedule(self):
        self._require_tm()
        self._tm.print_schedule()

    def play_next_match(self, show_animation: bool = False):
        """Play the next match (animation optional for faster tests)."""
        self._require_tm()
        self._tm.play_next(show_animation=bool(show_animation))

    def simulate_all_matches(self, show_animation: bool = False):
        """Simulate all remaining matches."""
        self._require_tm()
        self._tm.simulate_all(show_animation=bool(show_animation))

    def play_final(self, show_animation: bool = False):
        self._require_tm()
        self._tm.play_final(show_animation=bool(show_animation))

    def show_scoreboard(self):
        self._require_tm()
        self._tm.show_scoreboard()

    def reset_tournament(self):
        self._require_tm()
        self._tm.reset()

    # Internal
    def _require_tm(self):
        if self._tm is None:
            raise RuntimeError("Tournament not created. Use `Create Tournament` first.")
