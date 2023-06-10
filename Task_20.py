# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

alphabet = ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т', 'д', 'к', 'л', 'м', 'п', 'у', 'б', 'г', 'ё', 'ь', 'я', 'й', 'ы', 
           'ж', 'з', 'х', 'ц', 'ч', 'ш', 'э', 'ю', 'ф', 'щ', 'ъ'] 

letters = []
word = input('Введите слово: ')
for i in word:
    letters.append(i)

count = 0

for i in range(len(letters)):
    for j in range(len(alphabet)):
        if letters[i] == alphabet[j]:
            if j > 0 and j <= 8:
                count += 1
            elif j > 8 and j <= 14:
                count += 2
            elif j > 14 and j <= 19:
                count += 3
            elif j > 19 and j <= 24:
                count += 4
            elif j > 24 and j <= 26:
                count += 5
            elif j > 26 and j <= 29:
                count += 8
            elif j > 29 and j <= 32:
                count += 10

print(f'Слово {word} весит {count} баллов')