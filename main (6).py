import random

lives = 9
words = ['пицца', "ангел", "мираж", "носки", "выдра", "петух"]
secret_word = random.choice(words)
unknow_letters = len(secret_word)
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index + 1

heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue, unknow_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unknow_letters = unknow_letters - 1
        index = index + 1
        
    return unknow_letters

difficulty = input('Выберите уровень сложности (1, 2 или 3):\n 1 Легкий\n 2 Средний\n 3 трудный ')
difficulty = int(difficulty)

if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 6
    
while lives > 0:
    print(clue)
    print('Осталось жизней: ' + heart_symbol * lives)
    g = input('Угадайте букву или слово целиком: ')
    
    if g == secret_word:
        guessed_word_correctly = True
        if guessed_word_correctly:
            print('Победа! Было загадано слово ' + secret_word)
            break
    
    if g in secret_word:
        unknow_letters = update_clue(g, secret_word, clue, unknow_letters)
    else:
        print('Неправильною Вы теряете жизнь')
        lives = lives - 1
    
    if unknow_letters == 0:
        guessed_word_correctly = True
        if guessed_word_correctly:
            print('Победа! Было загадано слово ' + secret_word)
            break
    if lives == 0:
        print('Проигрыш! Было загадано слово ' + secret_word)