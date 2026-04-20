import random

def play_turn(player_name):
    total = 0
    print(f"\n{player_name}'s turn:")
    
    for i in range(1, 4):  # 3 chances
        input(f"Press Enter to roll dice (Chance {i})...")
        roll = random.randint(1, 6)
        print(f"Rolled: {roll}")
        total += roll
    
    print(f"{player_name}'s total score: {total}")
    return total

print(" Dice Game: 2 Players, 3 Chances Each ")

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

score1 = play_turn(player1)
score2 = play_turn(player2)

print("\n Result:")
if score1 > score2:
    print(f"{player1} wins!")
elif score2 > score1:
    print(f"{player2} wins!")
else:
    print("It's a tie!")