import random

aleatorio = random.randrange(0,99,1)
print(aleatorio)
print("estas seguro que hoy te encuentras con suerte \n " +
    "pongamoslo a prueba \n que comiencen los juegos del hambre \n "+
    "tienes 10 oportunidades para adivinar el numero que estoy pensando \n ")
for i in range (10):
    a=input("Que numero estoy pensando, cavernicola :  ")
    b=abs(int(a)-aleatorio)
    
    print(a, b)
    if (b==0):
        if (i==1):
            print("Eres el sinsajo, por lograr conservar tus alas\n"+
                "vuela ")
        if(i<=3 and i>1):
            print("eso es una lagrima, tan delicada la flor, pero ya vas de salida ")
        if (i>3 and i<=5):
            print("yo me queda cone sta parte de tu orgullo, ya largate")
        if (i>5 and i<=8):
            print("Ven aca, esta carne que estamos fritando sabe bueno \n la sacamos de tu cerebro, no quieres quedarte un pco mas")
        if (i==9):
            print("ya te vas, que cosas este pierna sabe bueno, casi seguimos con la otra, \n a llorar a la cama nenita")
        if (i==10):
            print("aunq e lograste salir con vida\n recuerdaras mi cara todos las noches\n "+
            "dulces sueños\nos vemos esta noche\n "+
            "Jua Jua Jua, corre que esta noche estare en tus sueños")
        if (i<10):
            print(" por lo visto esta noche  irulais tendra que comer, ven aca pedazo de escoria\n eres mio\n Has perdido")
        break

    print( b<10)
    if (b>0 and b<=10):
        print("Rata de dos patas casi me dejas con una pata pero aun te falta, ")
    if (b>10 and b<=20):
        print("crees que con eso armaras para una sopa, mereces la muerte por Snu Snu")
    if (b>20 and b<=40):
        print("huele a sangre, maldito y adivina solo te quedan ", i, " y seras la comida de mis sabuesos")
    if (b>40 ):
        c=input("ya rindete, perdedor asi nunca lo lograras estas muy lejos \n solo tienes que escribir \"me rindo\" y el sufrimiento acabara \n"+
        "o deseas seguir intentandolo escribe \"seguir\"  ")
        
        while c != "seguir":
            print("ni siquiera eso puedes hacer, pedazo de escoria Lilipudiente \n escribe bien pedazo de porqueria")
            c=input("no es dificil solo escribe, \"me rindo\" o \"seguir\"  vez que no es dificil UGA UGA: ")
            if (c== "me rindo"):
                print(" por lo visto esta noche  firulais tendra que comer, ven aca pedazo de escoria\n eres mio\n Has perdido")
                break
        if (c== "me rindo"):
            break
    
print("Fin Del Juego")    