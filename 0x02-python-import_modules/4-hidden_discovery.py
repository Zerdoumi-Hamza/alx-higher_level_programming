#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)
    names1 = [names[i] for i in range(len(names)) if names[i][0] != "_"]
    names1.sort()

    for i in range(len(names1)):
        print(names1[i])
