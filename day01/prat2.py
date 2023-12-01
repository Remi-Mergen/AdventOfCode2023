"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line.

For example:
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""
"""
wrong answers: 54095, 54007
"""

"""
import re

# Mapping of string digits to their corresponding numeric values
numbers_mapping: dict[str, int] = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def find_first_digit(line) -> str:
    """extracts the first digit from a line of text, as a text or as a number"""
    pos_nbr_letter: int = -1
    pos_nbr_nbr: int = -1
    digits: list[str] = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
    if digits:
        pos_nbr_letter: int = line.find(digits[0])

    for char in line:
        if char.isdigit():
            first_digit = char
            pos_nbr_nbr: int = line.find(first_digit)
            break
    if pos_nbr_letter >= 0 and pos_nbr_nbr >= 0:
        return digits[0] if pos_nbr_letter < pos_nbr_nbr else first_digit
    elif pos_nbr_letter >= 0 and not pos_nbr_nbr >= 0:
        return digits[0]
    elif not pos_nbr_letter >= 0 and pos_nbr_nbr >= 0:
        return first_digit
    else:
        exit("No first digit found")

def find_last_digit(line) -> str:
    """extracts the last digit from a line of text, as a text or as a number"""
    pos_nbr_letter: int = -1
    pos_nbr_nbr: int = -1
    digits: list[str] = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line)
    if digits:
        pos_nbr_letter: int = line.rfind(digits[-1])

    for char in line[::-1]:
        if char.isdigit():
            last_digit = char
            pos_nbr_nbr: int = line.rfind(last_digit)
            break
    if pos_nbr_letter >= 0 and pos_nbr_nbr >= 0:
        return digits[-1] if pos_nbr_letter < pos_nbr_nbr else last_digit
    elif pos_nbr_letter >= 0 and not pos_nbr_nbr >= 0:
        return digits[-1]
    elif not pos_nbr_letter >= 0 and pos_nbr_nbr >= 0:
        return last_digit
    else:
        exit("No last digit found")

def main() -> None:
    try:
        with open("input.txt", "r") as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print("Unknown error:", e)
        return

    first_digit = ""
    last_digit = ""
    result = 0
    i = 0
    for line in lines:
        first_digit = find_first_digit(line)
        last_digit = find_last_digit(line)
        if not first_digit.isdigit():
            first_digit = numbers_mapping[first_digit]
        if not last_digit.isdigit():
            last_digit = numbers_mapping[last_digit]
        concatened_digits = str(first_digit) + str(last_digit)
        result += int(concatened_digits)
    
    print(result)

if __name__ == "__main__":
    main()
"""


num_dict = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

import pandas as pd

df = pd.read_csv('input.txt', header=None, names=['fullstring'])

for key, value in num_dict.items():
    df['fullstring'] = df['fullstring'].replace(key, str(value), regex=True)

df['numbers'] = df['fullstring'].apply(lambda x: [int(num) for num in x if num.isdigit()])
df['combined_numbers'] = df['numbers'].apply(lambda x: x[0]*11 if len(x) == 1 else int(str(x[0]) + str(x[-1])))

print(sum(df['combined_numbers']))