from manim import *
from math import gcd

class CoprimeGridStaticBlackMovingWhite(Scene):
    def construct(self):
        # Taille de la grille
        grid_size = 100
        
        # Taille des cellules pour remplir le cadre
        frame_width = config.frame_width
        frame_height = config.frame_height
        cell_size = 2*min(frame_width, frame_height) / grid_size


        # Fonction pour créer une grille avec uniquement les cases blanches
        def create_white_grid():
            white_squares = VGroup()
            for x in range(-grid_size // 2, grid_size // 2):
                for y in range(-grid_size // 2, grid_size // 2):
                    # Vérifie si les coordonnées (x, y) ne sont pas premières entre elles
                    if gcd(x, y) != 1:
                        square = Square(side_length=cell_size)
                        square.move_to(np.array([x * cell_size, y * cell_size, 0]))
                        square.set_fill(WHITE, opacity=1)
                        square.set_stroke(width=0)
                        white_squares.add(square)
            return white_squares

        # Créer et ajouter la grille statique noire en arrière-plan
        #static_black_grid = create_black_grid()
        #self.add(static_black_grid)

        # Créer et ajouter la grille blanche animée par-dessus
        animated_white_grid = create_white_grid()
        static_white_grid = create_white_grid()
        self.add(animated_white_grid)
        self.add(static_white_grid)
        
        
        # Pause pour visualiser la grille de départ
        self.wait(2)
        
        # Animation de déplacement uniquement pour les cases blanches
        animations = [
            square.animate.move_to(square.get_center() * 2)
            for square in animated_white_grid
        ]
        
        # Jouer l'animation en parallèle sur 1 seconde
        self.play(*animations, run_time=1)
        
        # Pause pour voir le résultat final
        self.wait(2)
