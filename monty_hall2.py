import random

def monty_hall(trials=100_000):
    stay_wins = 0
    switch_wins = 0

    for _ in range(trials):
        # Doors: one car, two goats
        doors = ["car", "goat", "goat"]
        random.shuffle(doors)

        # Player chooses a door
        player_choice = random.randint(0, 2)

        # Monty opens a door with a goat (not player's choice)
        possible_opens = [
            i for i in range(3)
            if i != player_choice and doors[i] == "goat"
        ]
        monty_opens = random.choice(possible_opens)

        # Remaining unopened door
        remaining_door = next(
            i for i in range(3)
            if i not in (player_choice, monty_opens)
        )

        # Outcomes
        if doors[player_choice] == "car":
            stay_wins += 1
        if doors[remaining_door] == "car":
            switch_wins += 1

    print(f"Trials: {trials}")
    print(f"Stay wins:    {stay_wins/trials:.3f}")
    print(f"Switch wins:  {switch_wins/trials:.3f}")

# Run simulation
monty_hall()
