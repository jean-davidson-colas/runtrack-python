"""
Enoncé:
Écrire un programme qui affiche un rectangle avec des ‘-’ et des ‘|’ en
fonction des paramètres d’entrées, (width, height), par exemple :
draw_rectangle(10, 3)
"""
import matplotlib.pyplot as plt

def rectangle1(self, event):

        painter = QPainter(self)

        painter.setPen(QPen(Qt.black,  5, Qt.DotLine))

        #painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))

        painter.drawRect(40, 40, 400, 200)

        print(rectangle1())
        plt.show()

        