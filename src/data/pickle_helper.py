import pickle


def print_all():
    with open("already_notified.pickle", "rb") as f:
        f = pickle.load(f)

        for line in f:
            print(line)


def check_if_exists(id_to_check=""):

    with open("already_notified.pickle", "rb") as f:
        f = pickle.load(f)

    if id_to_check != "":
        print(f"Checking id: {id_to_check}")
        if id_to_check in f:
            print("YES")
        else:
            print("NO")


def clear_file(pickle_file="already_notified.pickle"):
    with open(pickle_file, "wb") as f:
        pickle.dump(set(), f)


clear_file()
