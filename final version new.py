list_word = {'Информатика', 'Динозавр', 'Компьютер', 'Архитектура', 'Вселенная', 'Экзамен', 'Бесконечность', 'Питон', 'Банан', 'Кожура', 'Облако', 'Асфальт'}
word = list_word.pop()
print('Привет, обитатель интернета!')
print('Давай сыграем в игру: Я загадаю слово, а ты попытаешься его отгадать.')
print('Ты можешь либо угадать слово полностью, либо по буквам')
print('Чтобы угадать слово целиком - пиши с заглавной буквы!')
print('Не вводите пустые строки!')
secret = '?' * len(word)
secret_new = ''
print('Если вдруг тебе понадобится помощь, напиши /help, чтобы узнать, какую помощь я могу тебе предложить')
print(secret)
attemps = 20
letter = input('Введи русскую букву: ')
count_attemps = 0
set_letters = set()

#Дополнительная переменная, нужная для определения букв, которые пользователь уже угадал.
secret_new_res = ''

#Переменная unusable_symbols содержит в себе все цифры и английские буквы для дальнейшего сравнения с ней переменной letter.
#Так как мы - русские пользователи, то вряд ли мы захотим вводить, например, китайские или арабские символы.
#Следовательно, я учитываю только то, что может ввести обычный русский пользователь при помощи стандартной клавиатуры.
unusable_symbols = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.!"№;%:?*()_+=@#$%^&\|-'

#Цикл основан на количестве попыток, и пока оно не равно нулю, цикл будет работать
#Так же цикл не воспринимает пустые строки.
while attemps != 0 and len(letter) != 0:

    #Проверяется переменная, вводимая пользователем, на наличее команды
    if letter == '/help':
        print('Я могу тебе помочь следующим:')
        print('/show_letters - показывает все буквы, которые используются в слове')
        print('/attemps - показывает количество оставшихся возможностей написать неправильную букву')
        print('/rules - показывает правила игры')
        print('/surrender - если у тебя не получается отгадать слово, ты можешь сдаться')
        
    #Проверяется переменная, вводимая пользователем, на наличее команды
    if letter == '/show_letters':
        print(set(word))

    #Проверяется переменная, вводимая пользователем, на наличее команды
    if letter == '/attemps':
        print(attemps)

    #Проверяется переменная, вводимая пользователем, на наличее команды
    if letter == '/rules':
        print('Ты должен вводить либо по одной букве, либо все слово целиком. Если пишешь слово целиком - пиши с заглавной буквы!')
        print('Если ты не правильно указываешь букву, то количество попыток уменьшается')
        print('Если же ты неправильно указываешь слово целиком, то автоматически проигрываешь')
        print('Вводи русские буквы!')

    #Проверяется переменная, вводимая пользователем, на наличее команды
    if letter == '/surrender':
        attemps = 0
        break

    #Переменная letter проверяется на наличие полного слова и длины, большей единицы.
    if letter == word and len(letter) > 1:
        print('Ага! Подсмотрел код и сразу написал правильный ответ! Я так не играю. Попыток затрачено:', count_attemps)
        print('Ответ:', word)
        break

    #Для определения ввода нерусской буквы моя программа проверяет только первый символ строки.
    #Проверка на ввод русской буквы.
    if letter[0] in unusable_symbols:
        print('Введи РУССКУЮ букву! Пропиши /rules чтобы узнать больше.')
        letter = input('Введи букву: ')

    #Проверка на повторно выведенную букву
    if letter in set(secret_new_res):
        print('Вы уже угадали эту букву! Повторяю:')

    #Переменная letter проверяется на наличие только одной буквы, наличием ее в слове (регистр не учитывается) и отсутствием ее в переменной а.
    if len(letter) == 1 and (letter in word or (chr(ord(letter) + 32) in word) or (chr(ord(letter) - 32) in word)) and letter[0] not in unusable_symbols:
        for i in word:
            #Переменная letter проверяется на полное несовпадение с буквой слова и отсутствием ее в множестве угаданных букв пользователем
            if i != letter and i != chr(ord(letter) - 32) and i != chr(ord(letter) + 32) and i not in set_letters:
                print('?', end='')
            else:
                #По ходу цикла составляется слово, и когда множество его букв будет равно множеству букв изначального слова, то-есть мы составим исходное слово, цикл завершится
                secret_new += i
                secret_new_res += letter
                #К множеству введенных пользователем букв добавляется буква из слова, совпадающая с введенной
                set_letters.add(i)
                print(i, end='')
        print('')

    #Переменная letter проверяется на полное отсутствие ее в слове
    if letter[0] not in unusable_symbols and len(letter) == 1 and letter[0] != '/' and letter not in word and chr(ord(letter) - 32) not in word and chr(ord(letter) + 32) not in word:
        attemps -= 1
        print('Ха! не угадал. Буквы', '"' + letter + '"', 'нет в слове')
        print('Попыток осталось:', attemps)
        count_attemps += 1

    #Сравниваются множества букв слова и слова, составленного по ходу цикла для того, чтобы понять, когда завершать действие программы
    if set(word) == set(secret_new):
        print('Ты угадал! Чтож, ты победил. Удачи, обитатель интернета! Ответ:', word + '.', 'Попыток затрачено:', count_attemps)
        break

    #Переменная letter проверяется на команду, длину большей единицы и отсутствием полного слова в ней.
    if len(letter) > 1 and letter != word and letter[0] != '/' and letter[0] not in unusable_symbols:
        print('Поспешишь - людей насмешишь! Ты проиграл! Ответ:', word)
        #Если пользователь введет не то слово или просто несколько случайных русских букв, то он автоматом проиграет
        break

    #Переменная letter проверяется на отсутствие ее в "запрещенных" символов и несовпадением с загаданным словом. 
    if letter[0] not in unusable_symbols and letter != word:
        letter = input('Введи букву: ')

if len(letter) == 0:
    print('Предупреждал же! Не вводи пустые строки!')
    
#Если количество попыток сравнялось с нулем, то программа выведет следующее:
if attemps == 0:
    print('Ты проиграл! Ответ:', word + '.', 'Не хочешь сыграть еще раз?')
