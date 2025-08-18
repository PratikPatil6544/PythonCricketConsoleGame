Library    Process

${PYTHON}


Intro And Setup Order
    [Documentation]    Verifies intro appears and prompts in order; uses fully valid inputs to avoid EOF.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2
    ...    3
    ...    1
    ...    T1
    ...    P1
    ...    P2
    ...    P3
    ...    T2
    ...    Q1
    ...    Q2
    ...    Q3
    ...    0
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    =========== IAV - CRICKET TOURNAMENT ===========
    Should Contain    ${result.stdout}    Enter number of teams:
    Should Contain    ${result.stdout}    Enter number of players per team:
    Should Contain    ${result.stdout}    Enter number of overs:
    Should Contain    ${result.stdout}    Enter name for team 1:

Rejects Empty Names
    [Documentation]    Ensures blank team and player names are rejected and re-prompted; provide complete valid follow-ups.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2                 # teams
    ...    3                 # players/team (min 3)
    ...    1                 # overs
    ...                      # team 1 blank -> re-prompt
    ...    Alpha             # team 1 valid
    ...                      # player 1 blank -> re-prompt
    ...    A1                # player 1 valid
    ...    A2
    ...    A3
    ...    Beta              # team 2
    ...    B1
    ...    B2
    ...    B3
    ...    0                 # exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    ⚠️ Please enter a non-empty value.

Invalid Menu Choice Warning During League
    [Documentation]    While league fixtures remain, entering 9 should warn with 0–4 range; then exit cleanly.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2
    ...    3
    ...    1
    ...    Alpha
    ...    A1
    ...    A2
    ...    A3
    ...    Beta
    ...    B1
    ...    B2
    ...    B3
    ...    9                 # invalid menu choice
    ...    0                 # exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    ⚠️ Enter a number between 0 and 4.

Play Next Match Updates Scoreboard
    [Documentation]    Playing one match should produce non-empty Match Results; then show scoreboard.
    ${input}=    Catenate    SEPARATOR=\n
    ...    3                 # teams
    ...    3                 # players/team
    ...    1                 # overs
    ...    Tigers
    ...    T1
    ...    T2
    ...    T3
    ...    Lions
    ...    L1
    ...    L2
    ...    L3
    ...    Eagles
    ...    E1
    ...    E2
    ...    E3
    ...    3                 # Play Next Match
    ...    1                 # Show Scoreboard
    ...    0                 # Exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    Match Results:
    Should Not Contain    ${result.stdout}    No matches played yet
    Should Contain    ${result.stdout}    Points Table
    Should Contain    ${result.stdout}    Top Players

Simulate Remaining, Show Scoreboard, Play Final
    [Documentation]    Simulate league, verify scoreboard sections, then play final and see winner line.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2
    ...    3
    ...    1
    ...    Alpha
    ...    A1
    ...    A2
    ...    A3
    ...    Beta
    ...    B1
    ...    B2
    ...    B3
    ...    4                 # Simulate Remaining Matches
    ...    1                 # Show Scoreboard
    ...    3                 # Play Final
    ...    0                 # Exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    Points Table
    Should Contain    ${result.stdout}    Top Players
    Should Contain    ${result.stdout}    FINAL → Winner

Option 4 Hidden After League Ends
    [Documentation]    After simulating league, option 4 is hidden; entering 4 should warn with 0–3 range.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2
    ...    3
    ...    1
    ...    A
    ...    A1
    ...    A2
    ...    A3
    ...    B
    ...    B1
    ...    B2
    ...    B3
    ...    4                 # Simulate Remaining Matches (finishes league)
    ...    4                 # Try option 4 again (should be invalid now)
    ...    0                 # Exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    All league matches completed
    Should Contain    ${result.stdout}    ⚠️ Enter a number between 0 and 3.

Winner Announced Before Menu After Final
    [Documentation]    After final, winner banner prints before the next menu.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2
    ...    3
    ...    1
    ...    X
    ...    X1
    ...    X2
    ...    X3
    ...    Y
    ...    Y1
    ...    Y2
    ...    Y3
    ...    4                 # Simulate Remaining Matches
    ...    3                 # Play Final
    ...    0                 # Exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Match Regexp    ${result.stdout}    >>> Tournament Winner: .* <<<[\\s\\S]*===== CRICKET TOURNAMENT MENU

Restart Flow Shows Intro Again
    [Documentation]    After final, choosing Restart prints the intro banner again; then start a new valid tournament.
    ${input}=    Catenate    SEPARATOR=\n
    ...    2
    ...    3
    ...    1
    ...    P
    ...    P1
    ...    P2
    ...    P3
    ...    Q
    ...    Q1
    ...    Q2
    ...    Q3
    ...    4                 # Simulate Remaining Matches
    ...    3                 # Play Final
    ...    3                 # Restart Tournament
    ...    2                 # New tournament: teams
    ...    3                 # players/team
    ...    1                 # overs
    ...    R
    ...    R1
    ...    R2
    ...    R3
    ...    S
    ...    S1
    ...    S2
    ...    S3
    ...    0                 # Exit
    ${result}=    Run Process    ${PYTHON}    -u    -m    src.main    stdin=${input}    stdout=PIPE    stderr=PIPE
    Log    ${result.stdout}
    Should Contain    ${result.stdout}    =========== IAV - CRICKET TOURNAMENT ===========
