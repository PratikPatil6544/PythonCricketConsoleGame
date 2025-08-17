IAV Cricket Tournament – Python Console Game

Welcome to the IAV Cricket Simulator!
- Simulation: Matches are simulated with random runs per ball. The team with the higher total wins.
- Points: 1 match win = 2 points; a tie gives both teams 1 point.
- Final qualification: If two teams level on points, the team with the higher total runs qualifies for the final.
- Tournament scheduling: A full round‑robin league is scheduled randomly so each team plays the same number of matches.

You will first see an intro banner, then the setup prompts, then the tournament menu.

How to Play
- Setup order:
- Number of teams (within allowed range)
- Players per team (within allowed range)
- Number of overs (within allowed range)
- Team and player names (blank names are rejected; you’ll be re‑prompted)
- Menu options:
- Show Scoreboard – Match Results, Points Table, Top Players. After the final, also shows the tournament winner.
- Show Teams and Players – List all teams and their players.
- Context action:
- Play Next Match while league fixtures remain
- Play Final after league completes
- Restart Tournament after the final
- Simulate Remaining Matches – Visible only during league phase
- Exit
- Randomness:
- Runs per ball are random; results vary per run.
- Structure, prompts, and formatting are consistent for testing.

Quick Start with Makefile

Prerequisites

Git, Python 3.8+ (3.10+ recommended), make.

Steps
- Clone the repo git clone https://github.com/<your-username>/<your-repo>.git cd <your-repo>
- Install dependencies in a virtual environment make install
- Run the game make run
- Run all Robot Framework tests make test
- Run a single test by name make test-one NAME="Intro And Setup Order"
- Build a standalone binary (optional) make build
- Clean build artifacts make clean

Run make by itself to see the list of available targets.

Manual Setup (Without Makefile)
- Create and activate venv:
- Linux/macOS: python3 -m venv venv source venv/bin/activate
- Windows (PowerShell): python -m venv venv venv\Scripts\Activate.ps1
- Install dependencies: pip install --upgrade pip pip install -r requirements.txt
- Run the game (from project root):
- Linux/macOS: venv/bin/python -u -m src.main
- Windows: venv\Scripts\python.exe -u -m src.main
- Run tests (from project root): robot tests/tournament_tests.robot

Project Structure

├── src/ 
    ├── init.py 
    ├── main.py 
    ├── match.py
    ├── player.py 
    ├── team.py 
    ├── tournament.py 
    └── utils.py 
├── tests/ 
│   └── tournament_tests.robot 
├── Makefile 
├── requirements.txt 
└── README.md

Requirements

- Runtime: Python 3.8+
- Game: no third‑party libraries required
- Tests: Robot Framework (listed in requirements.txt)
