def reverse_number(n: int):
    s = str(n)

    return int(s[::-1])

print(reverse_number(1234)) # 4321

"""
Description:

This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s):
    res = ""

    for i in range(len(s)):
        for j in range(i+1):
            if j == 0:
                res += s[i].upper()
            else:
                res += s[i].lower()
        if i != len(s)-1:
            res += "-"
    return res


"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


"""
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""


def duplicate_count(text):
    text = text.lower()
    count = 0
    for letter in set(text):
        if text.count(letter) > 1:
            count += 1
    return count
