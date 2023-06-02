import unittest

def automata(entrada):

    tabla = [[2, 1, 1, " ", " ", " "],
            [2, " ", " ", " ", " ", " "],
            [2, " ", " ", 3, 5, 8],
            [4, " ", " ", " ", " ", " "],
            [4, " ", " ", " ", 5, 8],
            [7, 6, 6, " ", " ", " "],
            [7, " ", " ", " ", " ", " "],
            [7, " ", " ", " ", " ", 8],
            ["acepta", "acepta", "acepta", "acepta", "acepta", "acepta"]]
    
    cadena = entrada + "$"
    estado = 0
    simbolos=["+", "-", ".", "e", "$"]
    columna = 0

    for i in cadena:
        try:
            if i in simbolos:
                columna = simbolos.index(i)+1
            elif i.isdigit()== True:
                columna = 0
            else:
                return "error"
        except:
            return "error"
        
        estado = tabla[int(estado)][columna]
            #print(estado)
        if estado == " ":
            return "error"
        elif estado==8:
            return "aceptar"

            
class TestAutomata(unittest.TestCase):
    def test_1(self):
        resultado = automata("5")
        self.assertEqual(resultado, "aceptar")

    def test_2(self):
        resultado = automata("-")
        self.assertEqual(resultado, "error")

    def test_3(self):
        resultado = automata("$55$")
        self.assertEqual(resultado, "error")

    def test_4(self):
        resultado = automata("+5")
        self.assertEqual(resultado, "aceptar")

    def test_5(self):
        resultado = automata("+5.78$")
        self.assertEqual(resultado, "aceptar")
    
    def test_6(self):
        resultado = automata("+5.78e$")
        self.assertEqual(resultado, "error")
    
    def test_7(self):
        resultado = automata("e")
        self.assertEqual(resultado, "error")
    
    def test_8(self):
        resultado = automata("ab$")
        self.assertEqual(resultado, "error")

if __name__ == '__main__':
    unittest.main()


    