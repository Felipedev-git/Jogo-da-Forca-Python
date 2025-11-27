# 🔤 Jogo da Forca - Python

Projeto desenvolvido durante minha jornada de aprendizado em Lógica de Programação e Python. O objetivo foi recriar o clássico jogo da forca via terminal, aplicando conceitos de manipulação de listas, loops e validação de dados.

## 🚀 Evolução e Funcionalidades (v2.0)

Este projeto foi refatorado para incluir uma experiência de usuário robusta e "à prova de falhas".

### ⚙️ Mecânicas Implementadas:
- [x] **Banco de Palavras Aleatório:** Utilização da biblioteca `random` para sortear palavras de uma lista interna, garantindo que cada partida seja única (Rejogabilidade).
- [x] **Feedback Visual (ASCII Art):** O jogo desenha a forca e o boneco progressivamente a cada erro, utilizando uma lista de desenhos mapeada pelo número de vidas.
- [x] **Sistema de Vidas:** O jogador inicia com 6 chances. O jogo encerra automaticamente (Game Over) se as vidas chegarem a zero.

### 🛡️ Tratamento de Erros e UX (Porteiros):
O jogo possui validações para garantir que a entrada do usuário seja válida:
1.  **Bloqueio de Números/Símbolos:** O sistema verifica se o input é alfabético (`.isalpha()`).
2.  **Histórico de Tentativas:** O jogo memoriza todas as letras já chutadas e avisa caso o jogador tente repetir uma letra, sem penalizar a vida.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Biblioteca Random** (Standard Library)
* **Git & GitHub** (Versionamento)

## 💻 Como rodar o projeto

Certifique-se de ter o Python instalado em sua máquina.

```bash
# Clone este repositório
git clone [https://github.com/Felipedev-git/Jogo-da-Forca-Python.git](https://github.com/Felipedev-git/Jogo-da-Forca-Python.git)

# Entre na pasta
cd Jogo-da-Forca-Python

# Execute o jogo
python forca.py
Aprendizados
Durante o desenvolvimento deste projeto, aprofundei conhecimentos em:

Manipulação avançada de Listas e Índices.

Estruturas de repetição (while, for) e condicional (if/elif/else).

Uso de operadores de pertinência (in, not in).

Importação e uso de bibliotecas padrão.

Desenvolvido por Felipe de Campos 🦁
