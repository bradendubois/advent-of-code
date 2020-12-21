from sys import stdin
from lark import Lark, LarkError

l = stdin.read().split("\n\n")

rules = l[0].split("\n")
messages = l[1].split("\n")

def solve(rules, messages):

    translated = []
    for rule in rules:
        translated.append(rule.translate(str.maketrans('0123456789', 'abcdefghij')))

    parser = Lark("\n".join(translated), start='a')

    t = 0
    for msg in messages:
        try:
            parser.parse(msg)
            t += 1

        except LarkError:
            continue

    return t


# Part One
print(solve(rules, messages))

# Part Two
if '8: 42' in rules:
    rules.remove('8: 42')
rules.append('8: 42 | 42 8')

if '11: 42 31' in rules:
    rules.remove('11: 42 31')
rules.append('11: 42 31 | 42 11 31')

print(solve(rules, messages))
