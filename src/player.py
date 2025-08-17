class Player:
    def __init__(self, name):
        self.name = name
        self.runs = 0

    def add_runs(self, runs):
        self.runs += runs

    def get_name(self):
        return self.name

    def get_runs(self):
        return self.runs
