# Первое задание

duration = int(input('Введите количество секунд: '))
days = duration // 86400
hours = (duration % 86400) // 3600
minutes = ((duration % 86400) % 3600) // 60
sec = ((duration % 86400) % 3600) % 60
if days > 0:
    print(days, "дн", hours, "час", minutes, "мин", sec, "сек")
elif hours > 0:
    print(hours, "час", minutes, "мин", sec, "сек")
elif minutes > 0:
    print(minutes, "мин", sec, "сек")
else:
    print(sec, "сек")