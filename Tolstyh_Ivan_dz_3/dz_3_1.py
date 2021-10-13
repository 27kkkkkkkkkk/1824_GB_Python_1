def num_translate(num: str):
    """поддержка устаревшей функции"""

    return num_translate_adv(num)


def num_translate_adv(num: str):


    dictionary = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
        "eleven": "одиннадцать",
        "twelve": "двенадцать",
        "thirteen": "тринадцать",
        "fourteen": "четырнадцать",
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять",
        "Six": "Шесть",
        "Seven": "Семь",
        "Eight": "Восемь",
        "Nine": "Девять",
        "Ten": "Десять",
        "Eleven": "Одиннадцать",
        "Twelve": "Двенадцать",
        "Thirteen": "Тринадцать",
        "Fourteen": "Четырнадцать"
    }
    for i in dictionary.items():

        if num == i[0]:
            return i[1]
        elif num == i[1]:
            return i[0]


print(num_translate_adv("Three"), num_translate("seven"))
print(num_translate_adv("Три"), num_translate("семь"))
print(num_translate_adv("eight"), num_translate("восеемь"))





