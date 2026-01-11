import random

def monty_hall_30_cards(trials=100_000):
    stay_wins = 0
    switch_wins = 0
    num_cards = 30

    for _ in range(trials):
        # Create cards: 1 winner, 29 losers
        cards = ["WIN"] + ["LOSE"] * (num_cards - 1)
        random.shuffle(cards)

        # Player picks one card
        player_choice = random.randint(0, num_cards - 1)

        # Host reveals 28 losing cards (not player's choice, not winner)
        possible_reveals = [
            i for i in range(num_cards)
            if i != player_choice and cards[i] == "LOSE"
        ]
        revealed = random.sample(possible_reveals, num_cards - 2)

        # Find the remaining unrevealed card
        remaining_card = next(
            i for i in range(num_cards)
            if i != player_choice and i not in revealed
        )

        # Stay strategy
        if cards[player_choice] == "WIN":
            stay_wins += 1

        # Switch strategy
        if cards[remaining_card] == "WIN":
            switch_wins += 1

    print(f"Trials: {trials}")
    print(f"Stay win rate:   {stay_wins / trials:.4f}")
    print(f"Switch win rate: {switch_wins / trials:.4f}")

if __name__ == "__main__":
    monty_hall_30_cards()