def main():
    #escribe tu código abajo de esta línea
cont=0
acum=0
while acum<=1000:
    a=int(input())
    acum+=a
    cont+=1
print("suma = ", acum)
print("cantidad de números = ", cont)

if __name__=='__main__':
    main()
