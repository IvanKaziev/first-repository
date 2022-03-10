# first-repository
## <h1>Русский</h1>

Игра называется "Поле чудес". 
Здесь программа загадывает слово, а Вы пытаетесь его отгадать. Во время игры программа периодически будет говорить Вам о чем-либо.

*Правила*
- Вы можете допустить ошибку ровно 20 раз.
- В учет идут либо одиночные русские буквы, либо все слово целиком с заглавной буквы.
- Если Вы вводите русскую букву, которой нет в загаданном слове, то количество попыток уменьшается.
- Вы можете попросить помощи у программы, введя /help. Эта команда даст информацию о других командах, которые могут вам помочь.
- Нельзя вводить пустые строки. Иначе программа выведет соответствующее сообщение.

Итак, Вы запустили игру. Сначала выводится некий текст, а в конце строка, состоящая только из символов "?".
На месте каждой из этих звездочек в реальности стоит буква, которую Вам предстоит отгадать.
Вы вводите по одной русской букве.
Если Вы угадали букву, то выведется соответствующее сообщение и строка со звездочками и буквой(ами), которую(ые) Вы отгадали.
Иначе программа сообщит о том, что введенной буквы нет в слове и количество попыток уменьшено.
Иногда бывает так, что с каждой новой угаданной буквой все меньше понимаешь, что за слово загадала программа.
На такие случаи существует команда /help, которая даст информацию о других командах, которые могут вам помочь.
И вот, момент настал: Вы поняли, какое слово загадала программа. Вводите последнюю букву и побеждаете. 
Программа Вас поздравит и закончит свою работу.
Но не всегда же побеждать. Если у Вас закончатся попытки, или Вы введете больше одной русской буквы за раз, и это не будет загаданное слово, то Вы проиграете.
В таком случае не расстраивайтесь. Программа предложит сыграть Вам еще раз.

*Команды*
 - /help - дает информацию о других командах
 - /show_letters - покажет все буквы, которые есть в слове
 - /attempts - показывает оставшееся количество попыток
 - /rules - показывает правила игры
 - /show_word_now - показывает все угаданные на данный момент буквы в строке из звездочек
 - /surrender - позволяет закончить игру и сдаться
*Важно!*
 - В игре нельзя вводить более одной русской буквы, если она не является загаданным словом. В противном случае Вы проиграете автоматически!
 - Программа не воспринимает пустые строки
 - Ввод не чувствителен к регистру


## <h1>English</h1>

This game is called "The field of miracles".
The program chooses a word from a list and you try to guess it. During the game, the program will sometimes talk to you.

*Rules*
 - You can only make a mistake 20 times.
 - If you enter a russian letter that isn't present in the hidden word, then the number of attempts decreases
 - You can ask the program to help you by entering /help. This command will give information about other commands that can help you.
 - You can't enter empty lines. Otherwise, the program will react accordingly.

So, you have launched the game. At first you will see some text. After it there will be a line consisting only of characters "?"
In each place of these characters is a letter, that you have to guess.
You enter one russian letter at a time.
If you guessed the letter right, then the message about it and the letters you have already guessed will be displayed in the line with characters "?".
Otherwise, the program will tell you about your mistake and the number of attempts will be reduced.
Sometimes it happens that with each new guessed letter, you understand less and less what word the program has chosen.
For such cases, there is the /help command, which will give information about other commands that can help you.
When you have guessed the word, the program will tell you that you have won and stop running.
But also you can lose. If you run out of attempts, or you entered more than one Russian letter at a time, then you will lose.
If you have lost, then don't worry. You can play again.

*Commands*
 - /help - gives information about other commands that can help you.
 - /show_letters - shows all the letters that are in the hidden word
 - /attempts - shows the remaining number of attempts
 - /rules - shows rules of the game
 - /show_word_now - shows all guessed letters in the line of characters "?"
 - /surrender - you give up and the game ends
*Important!*
 - You can't enter more than one Russian letter unless it's the hidden word. Otherwise, you will lose automatically!
 - The program does not accept empty lines
 - Input isn't sensitive to capitalization
