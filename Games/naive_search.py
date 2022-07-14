import random
import time


def naive_search(list, objective):

    for i in range(len(list)):
        if list[i] == objective:
            return i
    return -1


if __name__ == '__main__':
    naive_search()
