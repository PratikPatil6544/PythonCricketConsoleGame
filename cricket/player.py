from dataclasses import dataclass

@dataclass
class Player:
    name: str
    runs: int = 0

    def getName(self) -> str:
        return self.name

    def getRuns(self) -> int:
        return self.runs
