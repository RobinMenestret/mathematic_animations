from manim import *

class GCDScene(MovingCameraScene):
    def construct(self):
        width = 157
        height = 30
        rectangle = Rectangle(width=width, height=height)
        scale = max(width, height)/16
        # Reculer la caméra en réduisant l'échelle de la frame de la caméra
        self.camera.frame.set_width(2*max(rectangle.width, rectangle.height))  # Augmentez ce facteur pour plus de recul
        self.play(self.camera.frame.animate.move_to(ORIGIN))  # Centrer la caméra après l'échelle

        
        # Réduire l'échelle de l'objet pour le rendre visible dans le cadre
         # Ajustez l'échelle pour bien voir le rectangle
        rectangle.move_to(ORIGIN)  # Centrer le rectangle au centre de la scène
        
        n=0
        end = False
        while not end :
            n+=1
            if max(rectangle.width, rectangle.height)%min(rectangle.width, rectangle.height) == 0 :
                end = True

            # Afficher le rectangle
            self.play(Create(rectangle))

            # Ajouter des étiquettes pour les dimensions du rectangle
            width_label = MathTex(str(int(rectangle.width))).scale(scale)
            height_label = MathTex(str(int(rectangle.height))).scale(scale)

            # Positionner les étiquettes
            width_label.next_to(rectangle, UP, buff=0.2)  # Positionner l'étiquette à droite
            height_label.next_to(rectangle, LEFT, buff=0.2)  # Positionner l'étiquette en haut

            # Afficher les étiquettes
            self.play(Write(width_label), Write(height_label))

            side_length = min(rectangle.width, rectangle.height)

            # Remplir le rectangle de carrés de côté 8 par la gauche
            for i in range(int(rectangle.width // (side_length))):  # Calcul du nombre de carrés en largeur
                for j in range(int(rectangle.height // side_length)):  # En hauteur
                    square = Square(side_length=side_length)
                    square.move_to(rectangle.get_corner(DL) + RIGHT * ((i+1/2) * side_length) + UP * ((j+1/2) * side_length))
                    square.set_fill(RED, opacity=0.5)
                    self.play(Create(square))
            if n%2 == 1:
                rectangle = Rectangle(width=rectangle.width%rectangle.height, height = rectangle.height)
                rectangle.set_fill(BLUE, opacity=0.5)
                rectangle.move_to(square.get_corner(DR) + RIGHT * rectangle.width/2 + UP * rectangle.height/2) 
            else :
                rectangle = Rectangle(width=rectangle.width, height = rectangle.height%rectangle.width)
                rectangle.set_fill(BLUE, opacity=0.5)
                rectangle.move_to(square.get_corner(UL) + RIGHT * rectangle.width/2 + UP * rectangle.height/2) 

        self.play(self.camera.frame.animate.shift(RIGHT * 5 * scale), run_time=1)

        # Ajouter des étiquettes pour les dimensions du rectangle

        gcd_label = MathTex("PGCD(" + str(width) + ", " + str(height) + ") = " + str(int(max(rectangle.width, rectangle.height)))).scale(scale)

        # Positionner les étiquettes
        gcd_label.move_to(14*RIGHT*scale)  # Positionner l'étiquette à droite

        # Afficher les étiquettes
        self.play(Write(gcd_label))

        self.wait(2)
