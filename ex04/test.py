import ai42.progressbar
import sys
import time


if __name__ == "__main__":
    listy = range(100)
    ret = 0
    for elem in ai42.progressbar.ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.1)
    print()
    print(ret)
