print('"Строка: Мы обязательно научимся программировать!"')
s="Мы обязательно научимся программировать!"
print("Третий символ стоки: %s" %(s[2]))
print("Предпоследний элемент: %s" %(s[-2])) 
print("Первые 5 символов : %s" %(s[0:5]))
print("Вся строка кроме последних 2 символов: %s" %(s[:-2]))
print("Все четные элементы:  %s" %(s[1::2]))
print("Все нечетные элементы: %s" %(s[::2]))
print("4 символа из цетра строки: %s" %(s[16:20]))
print("Символы с индексами кратные 3: %s" %(s[3::3]))
print("Строка в обратном порядке: %s" %(s[::-1]))
st=s[::-1]
print("Все символы через один в обратном порядке: %s" %(st[::2]))
print("Удалить второе слово: %s" %(s.replace(" обязательно ", " ")))
print("Заменить второе слово на ' никогда не ': %s" %(s.replace("обязательно","никогда не")))
print("добавить в конец строки 'на Python': %s" %('{}{}'.format(s, "на Python")))
st=s.split()
st1='{0} {1} {2} {3}'.format(st[3], st[0],st[1],st[2])
print("Последнее слово первым в строке: %s" %(st1))
print("Длина строки: %d" %(len(s)))
