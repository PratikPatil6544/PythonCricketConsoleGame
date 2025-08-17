from .match import Match, MatchType
from .team import Team

class MatchFactory:
    @staticmethod
    def create(mtype: MatchType, teamA: Team, teamB: Team, overs: int) -> Match:
        return Match(mtype, teamA, teamB, overs)
