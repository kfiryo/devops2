names = ["Inbar", "kfir", "dan", "eli"]
print(list(range(3)))
for name in names:
    print(name)

for i in range(len(names)):
    print(i)

a = 0
while a < 5:
    print(a)
    a = a + 1

number = [1, 2, 3]

for n in number:
    if n == 2:
        continue
    else:
        print("number")
