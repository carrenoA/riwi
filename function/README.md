Basic:
-

- area: (base * height) / 2
- even numbers: n%2==0
- celsius to fahrenheit: (c * 9/5) + 32

Intermediate:
-   

- Increase 1by1: n+=1
- Do nothing in else: pass
- Sort Array: array.sort(reverse=True) or array.reverse()
- Factorial:  
  limit = 1 \
  for i in range(1, n + 1): \
        limit *= i
- Return boolean with some conditionals: all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
- Calculate the square root: n**0.5
- Array to string: "".join(array)
- Split words/sentences: text.split(character for separation)

Intermediate plus:
-

- Item not in the list: not in
- Dictionary key: dictionary[key]
- Count and add each item in a dictionary:     

      for i in texto:
        
          if i in dictionary:
              dictionary[i] += 1
          else:
              dictionary[i] = 1
- Traverse an array with index and value: for i, valor in enumerate(lista)
- Validations, isupper(): at least one uppercase - isalnum(): alphanumeric

Hard:
-

- Recursividad:     
  - https://ellibrodepython.com/recursividad#recursividad
  - https://elpythonista.com/recursion-en-python-funciones-recursivas-con-ejemplos-practicos-guia-2025
- Validate if "i" is in another array: isinstance(i, list)
- Count lines in a .txt file: sum(2 for _ in open(nombre, 'r', encoding='utf-8'))
  - sum(increase value)
  - for _ in: count each line
  - open(name): open the file
  - r: just for reading
  - encoding="utf-8": interpret most of the characters
  - leer_archivo("/home/caki/hola.txt"): call the file
- Lambda function: lambda x:x/2