# между прочем работы со строками и циклов и словарей и листов не было в лекции >:(
# считаем что это слово и состоит только из гласных и согласных букв, без пробел чисел и другого
s = input()
letter_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for a in s:
    if a in letter_count:
        letter_count[a] += 1
letter_list = [letter_count[i] for i in letter_count]
letter_sum = sum(letter_list)
# не понятно что именно выводить, нет четкого формата.
print("Согласных букв всего", len(s) - letter_sum)
print("Гласных букв всего", letter_sum)
print("Количество каждой из гласных букв:", letter_count)
#без каких либо обьяснений выводим false если нету какой-то гласной
#попробуй ввести "euphoria" ;)
if (min(letter_list) == 0):
    print(False)