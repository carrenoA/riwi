#pide palabra y cuenta las vocales

word = input("Enter a word: ")
newList = list(word)
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
total = 0

for i in newList:
    if i in vowels:
        total+=1
    else:
        pass

print(f"Total vowels is: {total}")