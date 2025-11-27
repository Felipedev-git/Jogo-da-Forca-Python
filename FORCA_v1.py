import random

forca_desenhos = [
    """
       _______
      |/      |
      |     (x_x)
      |      \|/
      |       |
      |      / \\
      |
    __|___
    """,
    # 1 vida
    """
       _______
      |/      |
      |      (_)
      |      \|/
      |       |
      |      / 
      |
    __|___
    """,
    # 2 vidas
    """
       _______
      |/      |
      |      (_)
      |      \|/
      |       |
      |
      |
    __|___
    """,
    # 3 vidas
    """
       _______
      |/      |
      |      (_)
      |      \|/
      |
      |
      |
    __|___
    """,
    # 4 vidas
    """
       _______
      |/      |
      |      (_)
      |      \|
      |
      |
      |
    __|___
    """,
    # 5 vidas
    """
       _______
      |/      |
      |      (_)
      |
      |
      |
      |
    __|___
    """,
    # 6 vidas (Início)
    """
       _______
      |/      |
      |
      |
      |
      |
      |
    __|___
    """
]

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
historico = []

while True:
    print(forca_desenhos[vidas])
    l1 = input('Chute uma letra: ').upper()
    if not l1.isalpha():
        print('Digite apenas letras! ')
        continue
    if l1 in historico:
        print('Você já chutou essa, esqueceu?')
        continue
    historico.append(l1)
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
            print(forca_desenhos[0])
            print(f'Game over! A palavra correta era {secreta}!')
            break    
