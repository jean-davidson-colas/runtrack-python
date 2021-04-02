"""
Enoncé:
Écrire un programme qui affiche un rectangle avec des ‘-’ et des ‘|’ en
fonction des paramètres d’entrées, (width, height), par exemple :
draw_rectangle(10, 3)
"""
width = input("entrer la longueur")

height = input("entrer la largeur")
AB = "-"
ba = "|"
def draw_rectangle(width,height):
 AB * width
 ba * height
 print("la longueur ")* width
 print("la largeur ")* height
 

draw_rectangle(width,height)