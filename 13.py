# age = int(input("enter your age: "))
# if age > 18:
#     print("you are legal")
# else:
#     print("you are still a ch")
#

# biggest_age = 0
# current_age = 0
#
# i = 0
# while i < 5:
#     current_age = int(input("enter your age:"))
#     if current_age > biggest_age:
#         biggest_age = current_age
#     i += 1
#
# print("biggest age is " + str(biggest_age))

names = []


def get_name(name):
    while name != "moshe":
        names.append(name)
        name = input("give me another name: ")
    else:
        return names


print(get_name(input("give me your name: ")))
