
"""
##Overview

Write a helper function that takes in a Time object and converts it to a more human-readable format. You need only go up to '_ weeks ago'.

to_pretty(0) => "just now"

to_pretty(40000) => "11 hours ago"
##Specifics

The output will be an amount of time, t, included in one of the following phrases: "just now", "[t] seconds ago", "[t] minutes ago", "[t] hours ago", "[t] days ago", "[t] weeks ago".
You will have to handle the singular cases. That is, when t = 1, the phrasing will be one of "a second ago", "a minute ago", "an hour ago", "a day ago", "a week ago".
The amount of time is always rounded down to the nearest integer. For example, if the amount of time is actually 11.73 hours ago, the return value will be "11 hours ago".
Only times in the past will be given, with the range "just now" to "52 weeks ago"

"""

import timeit


def in_range(x, start, end):
    return x >= start and x < end


def to_pretty(seconds):
    if seconds == 0:
        return "just now"
    sec = [lambda x: in_range(x, 1, 60), 1]
    min = [lambda x: in_range(x, 60, 3600), 60]
    hours = [lambda x: in_range(x, 3600, 86400), 3600]
    days = [lambda x: in_range(x, 86400, 604800), 86400]
    weeks = [lambda x: in_range(x, 604800, 99999999), 604800]
    dct = {"second": sec, "minute": min, "hour": hours, "day": days, "week": weeks}
    for key, val in dct.items():
        if val[0](seconds):
            number = int(seconds / val[1])
            if number == 1:
                return "a{} {} ago".format("n" if key == "hour" else "", key)
            return "{} {}{} ago".format(number, key, "s" if number > 1 else "")


if __name__ == "__main__":
    start = timeit.default_timer()
    print(to_pretty(1))
    print(to_pretty(30))
    print(to_pretty(440))
    print(to_pretty(240))
    print(to_pretty(74093))
    print(to_pretty(6635722))
    print(to_pretty(4657))
    print(to_pretty(0))
    print(to_pretty(604900))
    print(to_pretty(568833))
    print(to_pretty(10281599))
    elapsed = timeit.default_timer() - start
    print("time = {}".format(elapsed))