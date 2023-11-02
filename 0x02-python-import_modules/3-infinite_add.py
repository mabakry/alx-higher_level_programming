#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    x = 0
    for i in range(1, len(argv)):
        x += int(argv[i])
    print("{}".format(x))
