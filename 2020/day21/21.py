from sys import stdin
from lark import Lark, LarkError
import math
import numpy as np
import itertools

l = stdin.read().split("\n")

ingredients = set()
allergens = set()

ing_occurrences = dict()

instance_see = dict()

for food in l:
    
    food_ingredients, food_allergens = food.split(" (contains ")

    food_ingredients = [x.strip() for x in food_ingredients.split(" ")]
    food_allergens = [x.strip(")") for x in food_allergens.split(", ")]

    ingredients.update(set(food_ingredients))
    allergens.update(set(food_allergens))

    for ing in food_ingredients:
        if ing not in ing_occurrences:
            ing_occurrences[ing] = 0
        ing_occurrences[ing] += 1

    for aller in food_allergens:
                
        if aller not in instance_see:
            instance_see[aller] = []
        instance_see[aller].append(food_ingredients)


safe = set()
dangerous = { ingredient: set() for ingredient in ingredients }

for ingredient in ingredients:

    bad = False

    for allergen in allergens:

        if all(ingredient in occur for occur in instance_see[allergen]):
            bad = True
            dangerous[ingredient].add(allergen)

    if not bad:
        safe.add(ingredient)

# Part One
print(sum([ing_occurrences[c] for c in safe]))

# Part Two
dangerous = { k: v for k, v in dangerous.items() if k not in safe }

identified = set()

while any(len(x) > 1 for x in dangerous.values()):

    for x in dangerous:
        if len(dangerous[x]) == 1:
            identified.update(dangerous[x])

        else:
            dangerous[x] -= identified

dangerous = { list(v)[0]: k for k, v in dangerous.items() }
k = [ dangerous[k] for k in sorted(dangerous.keys())]

print(",".join(k))
