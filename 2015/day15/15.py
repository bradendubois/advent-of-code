from sys import stdin
from itertools import product
import numpy

lines = stdin.read().split("\n")

def cookie_score(ingredients, ratios, qualities):

    values = [0] * len(qualities)
    calories = 0

    for i, details in enumerate(ingredients.values()):
        for quality, value in details.items():
            if quality == "calories":
                calories += value * ratios[i]

            else:
                idx = qualities.index(quality)
                values[idx] += value * ratios[i]

    return numpy.prod([max(x, 0) for x in values]), calories


ingredients = dict()
qualities = set()

for line in lines:

    ingredient, details = line.split(": ")
    details = details.split(", ")
    
    ingredients[ingredient] = dict()

    for detail in details:
        name, value = detail.split(" ")
        value = int(value)
    
        ingredients[ingredient][name] = value
        if name != "calories":
            qualities.add(name)


hundred = list(range(101))
ratios = product(*[hundred]*len(ingredients))

qualities = sorted(list(qualities))

best_cookie = 0
best_cookie_500 = 0

for ratio in ratios:

    if sum(ratio) != 100:
        continue

    score, calories = cookie_score(ingredients, ratio, qualities)
    
    if score > best_cookie_500 and calories == 500:
        best_cookie_500 = score

    if score > best_cookie:
        best_cookie = score

print(best_cookie)
print(best_cookie_500)
