from json import load
from sys import argv

with open(argv[1]) as f:
    data = load(f)

total = 0

queue = []

if isinstance(data, list):
    queue.extend(data)
else:
    queue.append(data)

while len(queue) > 0:

    current_item = queue.pop()

    if isinstance(current_item, int):

        total += int(current_item)

    elif isinstance(current_item, str):

        try:
            total += int(current_item)
        except Exception:
            pass

    elif isinstance(current_item, dict):

        for key in current_item:

            queue.append(key)
            queue.append(current_item[key])

    elif isinstance(current_item, list):

        queue.extend(current_item)
    
    else:

        print(type(current_item))

print(total)
