import nltk
from collections import Counter
import random
from nltk.probability import FreqDist
import os


def get_file():
    ls = os.listdir()
    list_txt = [i for i in ls if (i.endswith('.txt'))]
    return list_txt


def show(req):
    k = ""
    flagT = 1
    flagB = 1
    flagM = 1
    while (k != 'exit'):
        try:
            if (req == "Токен"):
                if flagT:
                    print("Статистика корпуса текста")
                    print(f"Всего токенов: {len(tokens)}")
                    print(f"Уникальные токены: {len(unical_tokens)}\n")
                    k = input(
                        f'Введите номер интересующего токена в диапазоне от {-len(tokens)} до {len(tokens) - 1} или "exit" для выхода\n> ')
                    flagT = 0
                assert k != 'exit'
                k = int(k)
                print(tokens[k])

            elif (req == "Биграмма"):
                if flagB:
                    print(f'Количество биграмм: {len(bigrams)}')
                    flagB = 0
                    k = input(
                        f'Введите номер интересующей биграммы в диапазоне от {-len(bigrams)} до {len(bigrams) - 1} или "exit" для выхода\n> ')
                assert k != 'exit'
                k = int(k)
                head, tail = bigrams[k]
                print(f'Голова: {head:15} Хвост: {tail} ')

            elif (req == "Модель Маркова"):
                if flagM:
                    k = input(
                        f'Введите интересующее слово или "exit" для выхода\n> ')
                    flagM = 0
                assert k != 'exit'
                tails = markov[k]
                print(f'Число хвостов для "{k}": {len(tails)}')
                num = int(input('Сколько вы хотите увидеть хвостов для этого слова?\n > '))
                print(f"Head: {k}")
                for tail, count in sorted(tails.items(), key=lambda x: x[1])[::-1]:
                    if (num == 0):
                        break
                    num -= 1
                    print(f"Tail: {tail:15} Count :{count}")

        except AssertionError:
            break
        except TypeError as ex:
            print("TypeError")
        except IndexError as ex:
            print("IndexError. Пожалуйста, введите целое число, которое находится в диапазоне корпуса.")
        except ValueError as ex:
            print("ValueError. Пожалуйста, введите число.")
        except KeyError as ex:
            print("KeyError. Запрашиваемое слово отсутствует в модели. Пожалуйста, введите другое слово.")
        except Exception:
            print("Неизвестная ошибка. Попробуйте ещё раз")
        k = input('> ')
    return menu


def make_sentences(k):
    while k != 'exit':
        while True:
            try:
                num = int(input('Сколько предложений вы хотите сгенерировать?\n > '))
                break
            except ValueError as ex:
                print("ValueError. Пожалуйста, введите число.")

        if (k == '5'):
            for i in range(num):
                sent = []
                while True:
                    head = random.choice(tokens)
                    if (head.isalnum()):
                        break
                sent.append(head.title())
                while len(sent) < 5 or head[-1] not in '.!?':
                    head = random.choices(tuple(markov[head].keys()), tuple(markov[head].values()))[0]
                    sent.append(head)
                print(" ".join(sent))

        elif k == '4':
            for i in range(num):
                sent = ""
                head = random.choice(tokens)
                sent += head
                for j in range(9):
                    # print(markov[head].keys(),markov[head].values())
                    head = random.choices(tuple(markov[head].keys()), tuple(markov[head].values()))[0]
                    sent += " " + head
                print(sent)
        else:
            print("\nНеопознанное слово. Попробуйте ещё раз")

        q = input('\nЧтобы сгенерировать ещё 10 предложений, введите "ещё" или "exit" для выхода\n> ')
        k = (k if q == 'ещё' else q)

    return menu


# open file
while True:
    try:
        list_files = get_file()
        assert list_files
        file_name = input(f"Введите название файла: {' '.join(list_files)} \n> ").strip()
        file = open(file_name, encoding='utf-8')
        print(f"{file_name} успешно открыт")
        break
    except OSError:
        print('Неудачная попытка открыть файл. Попробуйте ещё раз\n')
    except AssertionError:
        print(f'Подходящих txt-файлов для обработки не найдено. Проверьте действующую директорию: {os.getcwd()}')
        exit()

text = file.read()
file.close()

# make tokens
tokens = nltk.regexp_tokenize(text, "[^ \t\n]+")
unical_tokens = FreqDist(tokens)

# make bigrams
bigrams = nltk.bigrams(tokens)
bigrams = list(bigrams)

# make Markov model
markov = {}

for bigram in bigrams:
    head, tail = bigram
    markov.setdefault(head, {})
    markov[head].setdefault(tail, 0)
    markov[head][tail] += 1

menu = """
                 ---> Меню <---
-> Введите номер или тему интересующего задания:
    1. Токены
    2. Биграммы
    3. Модель Маркова
    4. Сгенерировать случайный текст
    5. Сгенерировать предложения
Или exit для завершения программы
"""

task = input(menu + '\n> ')
while (task != 'exit'):
    match task:
        case str() | int() as t if (t == "Токены" or t == '1'):
            print(show('Токен'))
        case str() | int() as t if (t == "Биграммы" or t == '2'):
            print(show("Биграмма"))
        case str() | int() as t if (t == "Модель Маркова" or t == '3'):
            print(show('Модель Маркова'))
        case str() | int() as t if (t == "Сгенерировать случайный текст" or t == '4'):
            print(make_sentences('4'))
        case str() | int() as t if (t == "Сгенерировать предложения" or t == '5'):
            print(make_sentences('5'))
        case _:
            print("-> Не удалось обработать запрос. Пожалуйста, выберите интересующий пункт из ранее предложенных.")
    task = input('> ')


