# Author: SCT (ADMG) 9/28/21

team1_wins = input("Enter team 1s wins:\n")

team1_ties = input("Enter team 1s ties:\n")

team2_wins = input("Enter team 2s wins:\n")

team2_ties = input("Enter team 2s ties:\n")

team1_total = int(team1_ties + (team1_wins * 3))

team2_total = int(team2_ties + (team2_wins * 3))

if team1_total > team2_total:
    print("Team 1 finished with more points")
else:
    print("Team 2 finished with more points")
