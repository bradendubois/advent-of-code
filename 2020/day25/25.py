from sys import stdin

l = stdin.read().split("\n")

card_public, door_public = int(l[0]), int(l[1])

def transform(subject_number, value=1, loop_size=1):
    temp = value
    for _ in range(loop_size):
        temp *= subject_number
        temp %= 20201227
    return temp


def secret_loop_size(subject_number, public_key):

    seen = set()

    i = 0
    value = 1

    while value != public_key:

        value = transform(subject_number, value)
        
        if value in seen:
            return None
        
        seen.add(value)

        i += 1

    return i


subject_number = 0

while True:

    if loop_card := secret_loop_size(subject_number, card_public):
        subject_card = subject_number
        break

    subject_number += 1

encryption = transform(door_public, loop_size=loop_card)

print(encryption)
