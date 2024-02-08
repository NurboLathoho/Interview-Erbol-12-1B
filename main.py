# Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована. 1
# Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой. Результат: "AAiddialneat” 1
# Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

# 1
# for number in range(1, 6):
#     print(f'0:{number}')


# 2
name = 'Aidana'
name2 = 'Adilet'

def mix_names(name1, name2):
    mixed_name = ''
    for char1, char2 in zip(name1, name2):
        mixed_name += char1 + char2
    return mixed_name

name1 = "Aidana"
name2 = "Adilet"
result = mix_names(name1, name2)
# print(result)

# 3
def count_words(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = "Money, money, money, it’s always sunny, in the richmen’s world"
word_counts = count_words(sentence)
for word, count in word_counts.items():
    print(f"{word}: {count}")