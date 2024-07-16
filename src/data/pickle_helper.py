import pickle
from config import ALREADY_NOTIFIED_PATH

def print_all():
    with open(ALREADY_NOTIFIED_PATH, "rb") as f:
        f = pickle.load(f)

        for line in f:
            print(line)


def check_if_exists(id_to_check=""):
    with open(ALREADY_NOTIFIED_PATH, "rb") as f:
        f = pickle.load(f)

    if id_to_check != "":
        print(f"Checking id: {id_to_check}")
        if id_to_check in f:
            print("YES")
        else:
            print("NO")

def clear_file(pickle_file=ALREADY_NOTIFIED_PATH):
    with open(pickle_file, "wb") as f:
        pickle.dump(set(), f)


def populate_file(pickle_file=ALREADY_NOTIFIED_PATH):
    how_many_elements = 1_000_000
    populate_set = set()
    for _ in range(0, how_many_elements):
        populate_set.add(_)
        if _ % 1_000_000 == 0:
            print(_)

    with open(pickle_file, "wb") as f:
        pickle.dump(populate_set, f)
