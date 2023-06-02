import re


class Parser:
    def __init__(self, expression):
        self.tokens = re.findall(r'\d+|\S', expression)
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens[0]
            self.tokens = self.tokens[1:]
        else:
            self.current_token = None

    def parse(self):
        result = self.expr()
        if self.current_token:
            raise SyntaxError('Syntax error')
        return result

    def expr(self):
        result = self.term()
        while self.current_token in ['+', '-', '%']:
            if self.current_token == '+':
                self.next_token()
                result += self.term()
            elif self.current_token == '-':
                self.next_token()
                result -= self.term()
            elif self.current_token == '%':
                self.next_token()
                result %= self.term()
        return result

    def term(self):
        if self.current_token == '(':
            self.next_token()
            result = self.expr()
            if self.current_token != ')':
                raise SyntaxError('Syntax error: No has cerrado los paréntesis')
            self.next_token()
            return result
        elif self.current_token.isnumeric():
            result = int(self.current_token)
            self.next_token()
            return result
        else:
            raise SyntaxError('Syntax error: token inválido')

def calculate(expression):
    parser = Parser(expression)
    result = parser.parse()
    return result

while True:
    expression = input("Ingrese una expresión aritmética (o deje vacío para salir): ")
    if not expression:
        break
    try:
        result = calculate(expression)
        print(f"Resultado: {result}")
    except SyntaxError as e:
        print(f"Error de sintaxis: {str(e)}")

