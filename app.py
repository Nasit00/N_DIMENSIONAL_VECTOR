from N_Dimensional_Vector.Class import n_dimensional_Vector
class App:
    def run(self):
        vector1 = n_dimensional_Vector(1, 2, 3)
        vector2 = n_dimensional_Vector(4, 5, 6)
        print("Vector 1:", vector1)
        print("Vector 2:", vector2)
        print("Addition:", vector1 + vector2)
