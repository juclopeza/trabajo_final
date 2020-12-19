# funcion recursiva para el calculo del factorial
def factorial(n):
    if n==0: # caso base
        return 1
    else: 
        return n *factorial(n-1) #caso recursivo

# crear un bucle for
# hacer una condicion 