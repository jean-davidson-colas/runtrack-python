"""
Enoncé:
 Écrire un programme qui itère les nombres entiers de 1 à 100. Pour les
multiples de trois, afficher "Fizz" au lieu du nombre et pour les multiples de
cinq afficher "Buzz". Pour les nombres qui sont des multiples de trois et
cinq, afficher "FizzBuzz" """


for i in range(1, 100):                    # Entiers de 1 à 99
    if ((i % 3) == 0) and ((i % 5) == 0):  # Multiple de 3 *et* de 5
        print('FIZZ BUZZ!', end=' ')       # Affichage sans retour à la ligne
    elif (i % 3) == 0:                     # Multiple de 3 uniquement
        print('Fizz!', end=' ')
    elif (i % 5) == 0:                     # Multiple de 5 uniquement
        print('Buzz!', end=' ')
    else:
        print(i, end=' ')
print() 

       