"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

def open_file(file_name) -> str:
    with open(file_name, 'r') as f:
        return f.read()

def sum_by_line(line: str) -> str:
    """
    Extracts the first and last digits from a line of text
    """
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in line[::-1]:
        if char.isdigit():
            last_digit = char
            break
    return first_digit + last_digit

def main():
    file_name = 'input.txt'
    file = open_file(file_name)
    file = file.split('\n')
    sum = 0
    for line in file:
        sum += int(sum_by_line(line))
    print(sum)

if __name__ == '__main__':
    main()
