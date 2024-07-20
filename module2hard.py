import random

print(random)

field1 = random.randint(3, 20)
print(field1)
result = []
for i in range(1, field1 + 1):

    for j in range(i, field1 + 1):

        if field1 % (i + (j + 1)) == 0:
            result.append(i)
            result.append(j + 1)

result = ''.join(str(number) for number in result)
print(result)
