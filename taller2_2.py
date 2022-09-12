def funcion2():
    x3=int(input("Ingrese un numero diferente de 0: "))
    while x3==0:
        x3=int(input("Ingrese un numero diferente de 0: "))
    gx=((x3)**2+(x3)**2+2)/(x3)**2
    print("g(x)=((x)^2+(x)^2+2)/(x)^2 siendo x=", x3 , "g(x)= ", gx )
funcion2()