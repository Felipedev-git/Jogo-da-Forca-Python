secreta = 'BANANA'
lista = ["_"] * len(secreta)
vidas = 6

while True:
    l1 = input('Chute uma letra: ').upper()
    for i in range(len(secreta)):
        if l1 == secreta[i]:
            lista[i] = l1            
    print(lista)
    if "_" not in lista:
        print('Você ganhou! ')
        break
    if l1 not in secreta:
        vidas = vidas - 1
        print(f'Restam {vidas} vidas!')
        if vidas == 0:
            print('Game over')
            break
         
