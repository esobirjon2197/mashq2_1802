# 1-m
numbers = [12, -5, 7, -3, 0, 25, -11, 8]

musbatlar = [x for x in numbers if x >= 0]

print(musbatlar)


# 2-m
numbers = [45, 12, 78, 3, 56, 89, 23]

print(numbers)

print(max(numbers))

print(min(numbers))


# 3-m
numbers = [1, 2, 3, 4, 5, 6]

print(numbers)

print(numbers[::-1])


# 4-m
numbers = [14, 7, 22, 9, 31, 18, 5]

juft = 0
toq = 0

for son in numbers:
    if son % 2 == 0:
        juft += 1
    else:
        toq += 1

print(juft)
print(toq)


# 5-m
list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = [4, 5, 6, 7, 8]
print(list2)

list3 = list1 + list2
print(list3)

list3 = set(list3)
print(list3)


# 6-m
numbers = [10, 20, 30, 40, 50]

print(numbers)

ortacha = sum(numbers)
print(ortacha)


# 7-m
numbers = [5, 3, 7, 3, 9, 3, 1]

print(numbers)

print(numbers.count(3))


# 8-m
numbers = [2, 4, 5, 7, 9, 11, 15]

print(numbers)


# 9-m
numbers = [29, 10, 14, 37, 13]

print(numbers)

numbers.sort()
print(numbers)


# 10-m
numbers = [4, 6, 2, 6, 8, 4, 6, 2]

print(numbers)

print(numbers.count(6))


# 11-m
words = ["python", "java", "c++", "golang"]

print(words)

words = str(words)
print(words.upper())


# 12-m
nested = [[1, 2], [3, 4], [5, 6]]

print(nested)


# 13-m
numbers = [100, 200, 300, 400]

print(numbers)


# 14-m
roy = []

for i in range(6):
    x = int(input("Son kirit: "))
    if x >0:
        roy.append(x)
print(roy)


# 15-m
words = ["apple", "banana", "kiwi", "strawberry"]

eng_uzun = max(words, key=len)
print(eng_uzun)

