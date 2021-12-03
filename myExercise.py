import sys

with open("students.txt", "r+") as file:
    dic = {}
    for Iter in file:
        if Iter[-1] == "\n":
            dic[Iter.split(":")[0]] = str(Iter[:-1].split(":")[1:])[2:-2].split(",")
        else:
            dic[Iter.split(":")[0]] = str(Iter.split(":")[1:])[2:-2].split(",")

    names = sys.argv[1]
    names = names.split(",")
    for name in names:
        try:
            print(f"{name},{dic[name][0]},{dic[name][1]}")

        except KeyError:
            print(f"No record of {name} was found!")
