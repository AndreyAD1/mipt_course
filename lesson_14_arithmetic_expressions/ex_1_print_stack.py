import random


stack = random.sample(range(100), 10)
print(stack)
for number in range(len(stack)):
    print(stack.pop(-1))
