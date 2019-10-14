import random

heads = 0
tails = 0
coins = 0
placeholder = 0
x = 0

print("How many coins do you want flipped?")
coins = input()

for i in coins:
    placeholder = random.randint(0, 1)

    if placeholder == 0:
        heads = heads + 1
        placeholder = 0

    elif placeholder == 1:
        tails = tails + 1
        placeholder = 0

    else:
        print("An error has occured, sorry.")

x = 100/(int(heads)+int(tails))

print(coins, "coins have been flipped")
print(tails, "of them where tails,")
print(heads, "of them where heads")
print(str(tails*x) + "% where tails")
print(str(heads*x) + "% where heads")