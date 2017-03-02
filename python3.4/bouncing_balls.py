__author__ = 'valeriy'


def bouncingBall(h, bounce, window):
    h = float(h)
    sum = 0
    bounce = float(bounce)
    window = float(window)
    if h > 0 and 0 < bounce < 1:
        while h > window:
            sum += 1
            h *= bounce
        return sum + sum - 1
    else:
        return -1


if __name__ == "__main__":
    print(bouncingBall(30, 0.66, 1.5))
    print(bouncingBall(3, 0.66, 1.5))