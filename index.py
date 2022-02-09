import random 

arrayExample = [1,2,3,4,5]

for i in range(5):
    arrayExample[i-1] = int(random.uniform(100,200))
    print(arrayExample[i-1])

varinput = int (input("ingresa un valor: "))
print(int(varinput))

for i in  range(5):
    if arrayExample[i] > varinput :
        print ("El valor del arreglo es mayor")
    else :
        print ("El valor del arreglo es menor")
        print (str(arrayExample[i]) + ">" + str(varinput))