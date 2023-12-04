import numpy as np

# configuration

rgb = np.array([12, 13, 14])  # max cubes for r,g,b

datafile = "input.txt"

with open(datafile, "r") as f:
    games = [game.strip() for game in f.readlines()]

# parse the entries to 2d array
def parse_game(game: str):
    game_id, playstates_string = game.split(":")
    game_id = int(game_id.split(" ")[1])

    playstates_string = playstates_string.split(";")
    playstates = []
    for element in playstates_string:
        playstates.append(parse_playstate(element.strip()))

    return game_id, np.vstack(playstates)

# parse input like "3 red, 5 green" to (3,5,0)
def parse_playstate(state: str):
    basis_vecs = {
        "red": np.array([1,0,0]),
        "green": np.array([0,1,0]),
        "blue": np.array([0,0,1])
    }
    vec = np.zeros(3)

    for entry in state.split(","):
        entry = entry.strip()

        factor, base_vec = entry.split(" ")
        vec += int(factor) * basis_vecs[base_vec]
    return vec

# part 1
sum_ids = 0
for game in games:
    game_id, playstates = parse_game(game)
    # if all playstates are possible with the given rgb values
    if (playstates <= rgb).all():
        sum_ids += game_id


print("Sum of possible game ids:", sum_ids)

# part 2
sum_powers = 0
for game in games:
    game_id, playstates = parse_game(game)
    min_cubes = playstates.max(axis=0)
    power = min_cubes.prod()
    sum_powers += power


print("Sum of powers:", int(sum_powers))
