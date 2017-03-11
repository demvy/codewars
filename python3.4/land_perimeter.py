
"""
Task:

Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
or


should return: "Total land perimeter: 24",
while


['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']


should return: "Total land perimeter: 18"

Good luck!
"""


def land_perimeter(arr):
    s = 0
    for i, line in enumerate(arr):
        for j, el in enumerate(line):
            if el == 'X' and j == 0:
                s += 1
            if el == 'X' and j == len(line) - 1:
                s += 1
            if i == 0 and el == 'X':
                s += 1
            if i == len(arr) - 1 and el == 'X':
                s += 1
            if j < len(line) - 1 and el == 'X' and line[j + 1] == 'O':
                s += 1
            if i > 0 and el == 'X' and arr[i - 1][j] == 'O':
                s += 1
            if i < len(arr) - 1 and el == 'X' and arr[i + 1][j] == "O":
                s += 1
            if j > 0 and el == 'X' and line[j - 1] == 'O':
                s += 1
    return "Total land perimeter: %d" % s


if __name__ == "__main__":
    print (land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]) == "Total land perimeter: 60")
    print(land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]) == "Total land perimeter: 52")
    print(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"])== "Total land perimeter: 40")
    print(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]) == "Total land perimeter: 54")
    print(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]) == "Total land perimeter: 40")
    print(land_perimeter(["OOXOO"]))