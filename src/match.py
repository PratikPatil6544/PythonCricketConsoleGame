class Match:
    def __init__(self, team1, team2, overs):
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.winner = None
        self.loser = None
        self.is_tie = False

    def simulate(self):
        raise NotImplementedError

    def get_match_info(self):
        return f"{self.team1.get_name()} vs {self.team2.get_name()}"

class NormalMatch(Match):
    def simulate(self):
        self.team1.play_innings(self.overs)
        self.team2.play_innings(self.overs)

        if self.team1.get_score() > self.team2.get_score():
            self.winner = self.team1
            self.loser = self.team2
        elif self.team2.get_score() > self.team1.get_score():
            self.winner = self.team2
            self.loser = self.team1
        else:
            self.is_tie = True

class FinalMatch(Match):
    def simulate(self):
        self.team1.play_innings(self.overs)
        self.team2.play_innings(self.overs)

        if self.team1.get_score() > self.team2.get_score():
            self.winner = self.team1
            self.loser = self.team2
        elif self.team2.get_score() > self.team1.get_score():
            self.winner = self.team2
            self.loser = self.team1
        else:
            self.is_tie = True
