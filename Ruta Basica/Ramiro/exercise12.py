#mostrar primera y ultima letra de una palabra

word = input("Enter a word: ")
list = list(word)

print(f'The first character is "{list[0]}"', f'and the second one is "{list[-1]}"')