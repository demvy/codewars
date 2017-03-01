__author__ = 'valeriy'

gal = 3.785411784
mile = 1.609344


def lp100km2mpg(liter):
    if liter <= 0 or not isinstance(liter, int) and not isinstance(liter, float):
        return 0
    else:
        m = 100/mile
        g = liter/gal
        return round(m/g, 2)


def mpg2lp100km(miles):
    if miles <= 0 or not isinstance(miles, int) and not isinstance(miles, float):
        return 0
    else:
        kilometrs = miles*mile
        liter = 100*gal
        return round(liter/kilometrs, 2)

p = lp100km2mpg(9)
print p
b = mpg2lp100km(42)
print b