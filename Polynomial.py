class Polynomial:
    def __init__(self):
        self.terms = []

    def add_term(self, coefficient, exponent):
        """
        Método para añadir un término al polinomio.
        """
        self.terms.append([coefficient, exponent])
    
    
    def heapsort(self):
        """
        Metodo para ordenar el polinomio usando Heapsort
        """
        n = len(self.terms)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.terms[i], self.terms[0] = self.terms[0], self.terms[i]
            self.heapify(i, 0)
            
            
    def heapify(self, n, i):
        """
        Función para convertir un subárbol en un heap
        """
        largest = i  
        left = 2 * i + 1 
        right = 2 * i + 2  
        
        if left < n and self.terms[left][1] > self.terms[largest][1]:
            largest = left

        if right < n and self.terms[right][1] > self.terms[largest][1]:
            largest = right

        if largest != i:
            self.terms[i], self.terms[largest] = self.terms[largest], self.terms[i]
            self.heapify(n, largest)


    def organize_polynomial(self):
        self.heapsort()


    def simplify_polynomial(self):
        """
        Metodo para simplificar el polinomio combinando términos semejantes.
        """
        simplified = {}
        
        for coef, exp in self.terms:
            if exp in simplified:
                simplified[exp] += coef
            else:
                simplified[exp] = coef

        new_terms = []
        for exp, coef in simplified.items():
            if coef != 0:
                new_terms.append([coef, exp])

        self.terms = new_terms


    def print_polinomial(self):
        """
        Método para mostrar el polinomio.
        """
        if not self.terms:
            print("P(x) = 0")
            return

        view_terms = []
        for coef, exp in self.terms:
            if exp == 0:
                view_terms.append(f"{1}")
            else:
                view_terms.append(f"{coef}x^{exp}")

        result = " + ".join(view_terms)
        print(f"P(x) = {result}")