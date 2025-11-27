import random

palavras = [
    'ABACATE', 'ELEFANTE', 'COMPUTADOR', 'PROGRAMACAO', 'PYTHON',
    'GIRAFA', 'HIPOPOTAMO', 'CHOCOLATE', 'BRASIL', 'FUTEBOL',
    'GUITARRA', 'BATERIA', 'DADO', 'JAZZ', 'ROCK',
    'SKATE', 'LIBRARY', 'FRAMEWORK', 'GITHUB', 'INTERFACE',
    'MONITOR', 'TECLADO', 'MOUSE', 'PROCESSADOR', 'MEMORIA',
    'ANDROID', 'IPHONE', 'WINDOWS', 'LINUX', 'DEVELOPER'
]
secreta = random.choice(palavras)
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
            print(f'Game over! A palavra correta era {secreta}!')
            break
         
