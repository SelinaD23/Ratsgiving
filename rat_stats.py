"""
STAT OPTIONS:
    Size: Small, Regular, Large
    Speed: Poor, Normal, Good
    Vision: Poor, Normal, Good
    Balance: Poor, Normal, Good
    Hearing: Poor, Normal, Good
"""
from random import randint

SMALL = randint(1, 4)
REGULAR = randint(5, 8)
LARGE = randint(9, 12)
POOR = randint(2, 5)
NORMAL = randint(6, 9)
GOOD = randint(10, 12)

BREEDS = {
    "Standard": {
        "Size": randint(5, 8),
        "Speed": randint(5, 8),
        "Vision": randint(5, 8),
        "Balance": randint(5, 8),
        "Hearing": randint(5, 8)
    },
    "Rex": {
        "Size": randint(5, 8),
        "Speed": randint(5, 8),
        "Vision": randint(5, 8),
        "Balance": randint(1, 4),
        "Hearing": GOOD
    },
    "Satin": {
        "Size": randint(1, 4),
        "Speed": GOOD,
        "Vision": randint(1, 4),
        "Balance": randint(5, 8),
        "Hearing": randint(5, 8)
    },
    "Dumbo": {
        "Size": LARGE,
        "Speed": randint(1, 4),
        "Vision": randint(5, 8),
        "Balance": randint(1, 4),
        "Hearing": GOOD
    },
    "Tailless": {
        "Size": randint(1, 4),
        "Speed": randint(1, 4),
        "Vision": GOOD,
        "Balance": randint(1, 4),
        "Hearing": GOOD
    },
    "Hairless": {
        "Size": randint(1, 4),
        "Speed": GOOD,
        "Vision": randint(5, 8),
        "Balance": randint(1, 4),
        "Hearing": GOOD
    },
    "Bristle Coat": {
        "Size": LARGE,
        "Speed": GOOD,
        "Vision": POOR,
        "Balance": POOR,
        "Hearing": randint(5, 8)
    }
}
BREED_NUMS = {
    1: "Standard",
    2: "Rex",
    3: "Satin",
    4: "Dumbo",
    5: "Tailless",
    6: "Hairless",
    7: "Bristle Coat"
}
BANNER = "============================================================================="
SPACES = 4 * 6


def print_breeds():
    print("SELECT YOUR BREED: (STAT VALUES: 1 - Lowest, 12 - Highest)")
    print(BANNER)

    stats = ["Name", "Size", "Speed", "Vision", "Balance", "Hearing"]
    breeds = [["Standard [1]", "Rex [2]", "Satin [3]"],
              ["Dumbo [4]", "Tailless [5]", "Hairless [6]", "Bristle Coat [7]"]]
    for i in range(len(breeds)):
        for stat in stats:
            if stat == "Name":
                for breed in breeds[i]:
                    breed_str = " " * 4 + stat + ": " + breed
                    if breed != "Bristle Coat [7]":
                        breed_str += " " * (SPACES - len(breed_str))
                    print(breed_str, end="")
            else:
                for breed in breeds[i]:
                    breed = breed[:-4]
                    stat_str = " " * 8 + stat + ": " + str(BREEDS[breed][stat])
                    stat_str += " " * (SPACES - len(stat_str))
                    print(stat_str, end="")
            print()

    print(BANNER)
