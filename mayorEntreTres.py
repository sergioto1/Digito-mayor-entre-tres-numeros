"""
Leer tres números enteros de dos dígitos cada uno y determinar 
en cuál de ellos se encuentra el mayor dígito.
< >
"""

def mayorEntreTres () -> int: 
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    
    if (a >= 10 and a <= 99) and (b >= 10 and b <= 99) and (c >= 10 and c <= 99):
        r1 = a % 10 # Segunda cifra del primer numero
        c1 = a // 10 # Primera cifra del segundo numero 
        r2 = b % 10 # Segunda cifra del segundo numero
        c2 = b // 10 # Primera cifra del segundo numero
        r3 = c % 10 # Segunda cifra del tercer numero
        c3 = c // 10 # Primera cifra del tercer numero
        
        if (r1 > c1) and (r1 > r2) and (r1 > c2) and (r1 > r3) and (r1 > c3):
            return "El digito mayor es ", r1
        elif (c1 >r1) and (c1 > r2) and (c1 > c2) and (c1 > r3) and (c1 > c3):
            return "El digito mayor es ", c1
        elif (r2 >r1) and (r2 > c1) and (r2 > c2) and (r2 > r3) and (r2 > c3):
            return "El digito mayor es ", r2
        elif (c2 >r1) and (c2 > c1) and (c2 > r2) and (c2 > r3) and (c2 > c3):
            return "El digito mayor es ", c2
        elif (r3 >r1) and (r3 > c1) and (r3 > r2) and (r3 > c2) and (r3 > c3):
            return "El digito mayor es ", r3
        elif (c3 >r1) and (c3 > c1) and (c3 > r2) and (c3 > c2) and (c3 > r3):
            return "El digito mayor es ", c3
        else:
            return ("Es posible que haya digitado numeros repetidos")
    else:
        return ("Uno de los numeros ingresados no es de dos cifras.")
    
print ("Hola")

print(mayorEntreTres())

        
