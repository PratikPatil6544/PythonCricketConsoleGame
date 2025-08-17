*** Settings ***
Library    cricket_console_library.py

*** Test Cases ***
Run Full Tournament And Show Scoreboard
    [Documentation]    Creates teams, runs all matches and final, then shows the scoreboard.
    Create Teams    Mumbai    Pune    Nagpur    Nashik
    Create Tournament    5
    Print Schedule
    Simulate All Matches
    Play Final
    Show Scoreboard

Run Match By Match
    [Documentation]    Demonstrates step-by-step match progression using keywords.
    Create Teams    Delhi    Chennai    Kolkata
    Create Tournament    3
    Print Schedule
    Play Next Match
    Show Scoreboard
    Play Next Match
    Show Scoreboard
    Simulate All Matches
    Show Scoreboard
