# Второе задание
agenda_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(agenda_list):
    if agenda_list[i].isdigit() or agenda_list[i][1:].isdigit():
       agenda_list[i] = agenda_list[i].zfill(2)
       agenda_list.insert(i + 1, ' "')
       agenda_list.insert(i, '" ')
       i += 1
       agenda_list[i] = agenda_list[i].replace('+5', '+05', 1)
    i += 1
agenda_list = ' '.join(agenda_list)
print(agenda_list.replace('  ', ''))






