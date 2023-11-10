import random
import time

with open("skins.txt") as file:
    data = {}
    for line in file:
        skin = line.split(",")[0]
        quant = int(line.split(",")[1])
        data[skin] = quant

skins = []
for skin in data:
    for _ in range(data[skin]):
        skins.append(skin)

print(random.choice(skins))
time.sleep(5)
