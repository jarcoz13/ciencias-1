import numpy as np

def calcularSlice(bloque):
  z, y, x = bloque//9*3, (bloque//3)%3*3, bloque%3*3 
  return z,y,x

def sliceBlock(a,bloque):
    z,y,x=calcularSlice(bloque)           
    return a[z:z+3 , y:y+3 , x:x+3]

if __name__ == "__main__":
    a = np.arange(729).reshape(9,9,9)
    print("Array Completo:")
    print(a)
    while(True):
        print("Digite -1 si quiere salir")
        bloque = int(input("Digite el indice del cubo: "))
        print("-------------------------------")
        if(bloque == -1):
            break
        else:
            print(sliceBlock(a,bloque),"\n")
            print(calcularSlice(bloque))

   
  


 
