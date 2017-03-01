__author__ = 'valeriy'


def make_readable(seconds):
    if seconds < 0 or seconds > 359999:
        raise Exception("error in seconds")
    else:
        HH = "0" if seconds / (60*60) < 10 else ""
        MM = "0" if (seconds % (60*60)) // 60 < 10 else ""
        SS = "0" if seconds % 60 < 10 else ""
        return HH + str(seconds / (60*60)) + ":" + MM + str((seconds % (60*60)) // 60) + ":" \
               + SS + str(seconds % 60)

a = make_readable(5)
print(a)