def calculadora (a,b,operación):
    try :
        a = float(a)
        b = float (b)
        if operación == '+':
            resultado = a + b
        elif operación == '-':
            resultado = a - b
        elif operación == '*':
            resultado = a * b
        elif operación == '/':
            resultado =a/b
        elif operación == '**':
            resultado  = a**b
        else :
            raise ValueError ('Ingresaste un valor no válido')
    except ValueError as error : 
        print('Ingresaste un valor no válido')
    except ZeroDivisionError as error:
        print('No puedes dividir un número por cero')
    except TypeError as error:
        print('No se puede realizar operaciones con texto')
    else :
        print(f'El resultado es: {resultado}')
    finally :
        print('Fin de la operación')


calculadora(5, 3, '+')
calculadora(10, 0, '/')
calculadora('hola', 3, '+')
calculadora(2, 3, '**')
calculadora(5, 2, '%')