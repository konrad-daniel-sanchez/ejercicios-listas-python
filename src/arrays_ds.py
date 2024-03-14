# https://www.hackerrank.com/challenges/arrays-ds/problem
# Versión Python3

def reverseArray(a):
    # Primera solución:
    respuesta = []
    for i in range(len(a)-1, -1, -1):
        respuesta.append(a[i])
    return respuesta

    # Otra posible solución (In place):
    '''
    for i in range(int(len(a)/2)):
        a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]
    return a
    '''
    
    # Esta es otra posible solución (Python List Slicing):
    # return a[::-1]
