from os import system

print("Welcome to the secret auction program.")
isStillPlaying = "yes"

list_of_players = []

while isStillPlaying.lower() == 'yes':
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))  # Directly convert bid to float
    isStillPlaying = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    system("clear")

    # Append the player dictionary with "name" and "bid" keys
    list_of_players.append({"name": name, "bid": bid})

# Find the highest bid
highest_bid = 0
winner = ""

for player in list_of_players:
    if player["bid"] > highest_bid:
        highest_bid = player["bid"]
        winner = player["name"]

print(f"The winner is {winner} with a bid of ${highest_bid:.2f}.")