import re

def validar(expresion_regular, texto):
    if re.match(expresion_regular, texto):
        return 'valido'
    else:
        return 'invalido'

expresion_regular_0 = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])[-/](0[1-9]|1[0-2])[-/]\d{2}(?:\d{2})?$')
expresion_regular_1 = re.compile(r'^(https?://)?(www\.)?youtube\.com/watch\?v=[a-zA-Z0-9_-]{11}(&\S*)?$')
expresion_regular_2 = re.compile(r'^[\d]{1,3}(,\d{3})*(\.\d{1,2})?$')
expresion_regular_3 = re.compile(r'^\w+\.?\w+@alumno\.um\.edu\.ar$')
expresion_regular_4 = re.compile(r'^[+54](\d{3,5})[15](\d{7})?$')
expresion_regular_5 = re.compile(r'^(\d{2})[-](\d{1,8})[-](\d{1})')
expresion_regular_6 = re.compile(r'^(?=.*\d)(?=.*[A-Z])(?=.*\W)(?!.*[\s])(?!.*[a-z]).{8,16}$')

formato_fecha = input('Introducir un estilo de fecha: ')
resultado = validar(expresion_regular_0, formato_fecha)
print(f'Formato de fecha {resultado}', '\n', '#########')

formato_id = input('Introducir un ID de YouTube: ')
resultado = validar(expresion_regular_1, formato_id)
print(f'Formato de ID {resultado}', '\n', '#########')

formato_numero = input('Introducir un numero real con dos decimales: ')
resultado = validar(expresion_regular_2, formato_numero)
print(f'Formato de numero {resultado}', '\n', '#########')

formato_mail = input('Introducir un mail de la Facultad de Mendoza: ')
resultado = validar(expresion_regular_3, formato_mail)
print(f'Formato de mail {resultado}', '\n', '#########')

formato_numero_celular = input('Introducir un numero de celular de Argentina, que contenga el codigo de pais y el 15: ')
resultado = validar(expresion_regular_4, formato_numero_celular)
print(f'Formato de numero {resultado}', '\n', '#########')

formato_cuil = input('Introducir un numero de CUIL: ')
resultado = validar(expresion_regular_5, formato_cuil)
print(f'Formato de CUIL {resultado}', '\n', '#########')

formato_contraseña = input('Introducir contraseña, con al menos: numero, mayuscuscula, caracter especial, long min de 8, long max de 16: ')
resultado = validar(expresion_regular_6, formato_contraseña)
print(f'Formato de contraseña {resultado}', '\n', '#########')