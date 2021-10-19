class Lagrange:
    def __init__(self, x):
        self.x = float(x)
        self.x_list = [-2,0,4]
        self.y_list = [2,-2,1]
        self.size = len(self.x_list)
        self.degree = self.size - 1
    
    def solve_polynomial(self):
        y = 0
        poly_list = []

        for i in range(self.degree + 1):
            polynomial = 1
            for j in range(self.degree + 1):
                if j != i:
                    polynomial *= (self.x - self.x_list[j])/(self.x_list[i] - self.x_list[j])
            y += self.y_list[i] * polynomial
    
        return y