def main():
    #escribe tu código abajo de esta línea

a=int(input())
vcot=1
sumar=0

while vcot<a:
    if a%vcot==0:
        sumar+=vcot
    vcot+=1
if a==sumar:
    print("El número es perfecto")
else:
    print("El NO es número perfecto")
if __name__=='__main__':
    main()
