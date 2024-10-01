from Polynomial import Polynomial

class Menu:
    def __init__(self, Polynomial):
        self.poly = Polynomial()


    def view_principal_menu(self):
        """
        Metodo que permite ver el menu principal
        """
        option = input("""
    ---------- Menu Polynomial ----------
            
                1. Initiate
                2. Exit
                option: """)
        
        if option == "1":
            self.view_polynomial_menu()
            
        elif option == "2":
            pass
        
        else:
            print("             Invalid option")
            self.view_principal_menu()
            
            
    def view_polynomial_menu(self):
        """
        Metodo que permite ver el menu del polinomio
        """
        print()
        print("    -------------------------------------")
        print()
        
        self.poly.print_polinomial()
        
        option = input(""" 
    ---------- Menu Polynomial ----------
            1. Add term 
            2. Organizatate polynomial 
            3. Simplify polynomial 
            4. Exit 
            Option: """)
        
        print()
        
        if option == "1":
            coefficient = input("Coefficient: ")
            exponent = input("Exponent: ")
            if coefficient.isdigit() and exponent.isdigit():
                self.poly.add_term(int(coefficient), int(exponent))
                self.view_polynomial_menu()
            else:
                print("Incorrect")
                self.view_polynomial_menu()
            
        elif option == "2":
            self.poly.organize_polynomial()
            self.view_polynomial_menu()
        
        elif option == "3":
            self.poly.simplify_polynomial()
            self.view_polynomial_menu()
            
        elif option == "4":
            pass
                         
        else:
            print("             Invalid option")
            self.view_polynomial_menu()