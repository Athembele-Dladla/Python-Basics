fruits = ["apple", "banana", "cherry","date"]

for fruit in fruits:
    if fruit == "cherry":
        break #exit the loop is cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue #skips the cherry and move to the iteration
    print(fruit)
    
    # print()

for fruit in fruits:
    if fruit == "cherry":
        pass #placeholder, no action is needed for the cherry
    print(fruit)