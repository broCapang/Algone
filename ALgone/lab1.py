for x in range (2,30,4):
    print(x)

animal = ["cat","tiger","horse"]
print(animal)

numbers = [11,3,7,5,4]
numbers.sort()
print(numbers)
sorted = list(numbers)
print(sorted)

name = input("What is your name?")
print(name)


a = [1,4,9,16,25,36, 49, 64, 81, 100]
b = list()
for x in a:
    if(x%2==0):
        b.append(x)

print(b)