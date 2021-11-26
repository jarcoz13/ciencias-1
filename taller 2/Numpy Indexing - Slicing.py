import numpy as np

def calcularSlice(bloque):
    z, y, x = bloque//9*3, (bloque//3)%3*3, bloque%3*3 
    return tuple(slice(i, i+3) for i in (z, y, x))

def cambiarBloques(a,bloque1,bloque2):
    z1, y1, x1 = calcularSlice(bloque1)
    z2, y2, x2 = calcularSlice(bloque2)
    temp = a[z1 , y1 , x1].copy()
    a[z1 , y1 , x1] = a[z2 , y2 , x2]
    a[z2 , y2 , x2] = temp
    return a    

if __name__ == "__main__":
    a = np.arange(729).reshape(9,9,9)
    print("Intercambio de posiciones de subArrays 3x3x3")
    print("Array Original:","\n")
    print(a,"\n")
    while(True):        
        bloque1 = int(input("Digite el indice del primer subArray: "))
        bloque2 = int(input("Digite el indice del segundo subArray: "))
        cambiarBloques(a,bloque1,bloque2)
        print("Se han intercambiado las posiciones")
        print("Array Nuevo:","\n\n",a,"\n")
        salir = input("Digite -1 si quiere salir, luego enter \nO solo presione enter para continuar:  ")
        if(salir == "-1"):
            break
        print("-------------------------------")
        
            

   
  


 
