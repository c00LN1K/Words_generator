import nltk

from nltk.probability import FreqDist

while True:
    try:
        file = input('Введите название файла: corpus.txt\n> ')
        file = 'corpus.txt'
        file = open(file, encoding='utf-8')
        print("Файл успешно открыт")
        break
    except Exception as ex:
        print('Неудачная попытка открыть файл. Попробуйте ещё раз\n')

text = file.read()
file.close()

tokens = nltk.regexp_tokenize(text, "[^ \t\n]+")

unical_tokens = FreqDist(tokens)

print("Статистика корпуса текста")
print(f"Всего токенов: {len(tokens)}")
print(f"Уникальные токены: {len(unical_tokens)}\n")

k = input(
    f'Введите номер интересующего токена в диапазоне от {-len(tokens)} до {len(tokens) - 1} или exit для выхода\n> ')
while (k != 'exit'):
    try:
        k = int(k)
        print(tokens[k])
    except TypeError as ex:
        print("TypeError")
    except IndexError as ex:
        print("IndexError. Пожалуйста, введите целое число, которое находится в диапазоне корпуса.")
    except ValueError as ex:
        print("ValueError. Пожалуйста, введите число.")
    finally:
        k = input('> ')

bigrams = nltk.bigrams(tokens)
bigrams = list(bigrams)
print(f'Количество биграмм: {len(bigrams)}')

k = input(
    f'Введите номер интересующей биграммы в диапазоне от {-len(bigrams)} до {len(bigrams) - 1} или exit для выхода\n> ')
while (k != 'exit'):
    try:
        k = int(k)
        head, tail = bigrams[k]
        print(f'Голова: {head:10}\tХвост: {tail} ')
    except TypeError as ex:
        print("TypeError")
    except IndexError as ex:
        print("IndexError. Пожалуйста, введите целое число, которое находится в предложенном диапазоне.")
    except ValueError as ex:
        print("ValueError. Пожалуйста, введите число.")
    finally:
        k = input('> ')
