import random
import unicodedata
from time import sleep


# pegar palavras aleatorias de um tema só, faer multi tema seria mt chato
# pedir um input de dinheiro e sortear a palavra, pedir input do usuario
# sanitizar todos os input e garantir que os de letra desconsidere acentos
# fazer um sistema que mostre a forca
# TODO nova: fazer uma var streak, que aumente conforme o jogador ganhe e faça ele perder conforme vai ganhando


def remover_acentos(string):
    nfkd = unicodedata.normalize('NFKD', string)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])


words = [
    "algoritmo", "variavel", "função", "laço", "execução",
    "condição", "lista", "desenvolvimento", "dados", "lógica",
    "sistema", "erro", "idea", "programar", "código"
]
hard_words = [
    "polimorfismo", "concorrência", "serialização",
    "transpilador", "desserialização", "inicializador",
    "singleton", "backpropagation", "criptografia",
    "encapsulamento", "recursividade", "multiplexação"
]


def randomWord(difficulty):
    if difficulty == 1:
        return random.choice(words).lower()
    else:
        return random.choice(hard_words).lower()


def printHang(chance):
    man = ['\\', '/', '\\', '/', '|', '(_)', ]
    for i in range(0, 6 - chance):
        if i == 6 - chance:
            man[i] = ' X'
        else:
            man[i] = 'X'
    print(f"""
 _________
 |/      |
 |      {man[5]}
 |      {man[3]}{man[4]}{man[2]}
 |      {man[1]} {man[0]}
 |
_|___
    """)


streak = 1
while True:
    money = int(input('Digite o valor a aposta R$'))
    chance = 6
    while money <= 0:
        print('Digite um valor valido.')
        money = int(input('Digite o valor a aposta R$'))
    print('Sorteando uma palavra com base em seu bônus de sorte...')
    sleep(1)
    if money >= 50:
        diff = 2
    else:
        diff = 1
    word = randomWord(diff + streak // 3)
    # Cheat
    print(word)
    display_word = word
    word = remover_acentos(word)
    known_chars = []
    win = False
    while chance != 0:
        letter = '-1'
        if chance == 1:
            last_try = str(input('Última tentativa, diga qual é a palavra: '))
            if remover_acentos(last_try) == word:
                win = True
                chance = 0
                break
            else:
                chance = 0
                break
                """
                if len(last_try) == 1:
                    #FIXME: O dislay das letras é depois de testar se a letra ta na palavra.
                    letter = last_try
                    pass
                else:
                    chance = 0
                    break
                 """

        print('-' * (8 + 1 + 2 + 2 * len(display_word)))
        printHang(chance)
        print('Palavra:', end=' ')
        for char in display_word:
            if remover_acentos(char) in known_chars:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print('')
        print('-' * (8 + 1 + 2 + 2 * len(display_word)))

        if letter == '-1':
            letter = str(input('Tente uma letra ou a palvra toda:')).strip().lower()
        letter = remover_acentos(letter)

        if len(letter) == 0:
            print('Entrada invalida, tente somente uma letra!')
            sleep(1)
            continue
        if len(letter) > 1:
            if letter == word:
                win = True
                print('Parabéns você acertou a palavra!')
                for char in word:
                    if char not in known_chars:
                        known_chars.append(char)
                break
            else:
                chance -= 2
                print('Você chutou incorretamente e perdeu uma tentativa adicional!')
                sleep(1)
                continue
        if letter in word:
            if letter not in known_chars:
                known_chars.append(letter)
            print('Você acertou mais uma letra!')
            if len(known_chars) == len(''.join(dict.fromkeys(word))):
                win = True
                break
        else:
            chance -= 1
            print(f'Não há nenhuma letra "{letter}"!')
        sleep(1)

    printHang(chance)
    print('Palavra:', end=' ')
    for char in display_word:
        if remover_acentos(char) in known_chars:
            print(char, end=' ')
        else:
            print('_', end=' ')
    print('')
    if win:
        print('-' * 50)
        print(f'Parabéns, você apostou R${money} e ganhou R${money * (chance + 1) * streak}')
        print(f'No entanto, devido as taxas e custeamento do serviço, seu saldo liquido é R${money + 1:.2f}')
        print(f'Seu bônus de sorte foi aumentado em 0.15%')
        print(f'Coeficiente de continuidade atual: {streak}')
        print(f'Voce ganhou {6 + 1 - chance } tentativas.')
        print('-' * 50)
        streak += 1
    else:
        print('Você perdeu, mas não se preocupe você pode tentar novamente, bônus de sorte: 2x')
        streak = 1
