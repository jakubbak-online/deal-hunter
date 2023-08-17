# THIS IS UNUSED SO FAR, THOUGH I MAY NEED IT LATER

import csv


def remove_duplicates(file_name):
    with open(file_name, "r+", newline="", encoding="utf-8") as f:
        csv_read = list(csv.reader(f, delimiter=","))
        # print(csv_read)

        csv_set = set()

        for line in csv_read:
            # print(line)
            csv_set.add(tuple(line))

        csv_write = csv.writer(f, delimiter=",")
        f.truncate(0)
        f.seek(0)

        for line in csv_set:
            csv_write.writerow(line)
        # print((f.readline().split(sep=",")))
        # csv_list = set(csv.reader(f, delimiter=","))
        # print(csv_list)


# remove_duplicates()
