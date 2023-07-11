import nltk

from nltk.probability import FreqDist

file = input('Введите название файла: corpus.txt or other\n> ')

file = 'corpus.txt'
file = open(file, encoding='utf-8')
text = file.read()
file.close()

# region
# tokens = nltk.word_tokenize(text) - токенизация по словам и знакам
# unical_tokens = set(tokens) - словарь уникальных слов
# print(tokens)
# print(unical_tokens)
# endregion

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
