i = 100
while i > 0:
    print(' 1.Вычислить n-е четное число \n 2.Вычислить n-е нечетное число \n 3.Сколько человек между i-м и k-v в очереди \n 5.Сколько полных часов минут и секунд в x секундах \n 6.в доме 9 этажей, на каждом этаже одного подъезда по 4 квартиры. В каком подъезде и на каком этаже n-я квартира \n 7. Старинными русскими денежными еденицами являются: 1 рубль=100 копеек, 1 гривна=10 копеек, 1 алтын=3 копейки, 1 полушка=0,25 копейки. Имеется А копеек \n 8. СТрелка вращается с постоянной скоростью - угол поворота в нулевой момент времени примем за 0. Каков угол поворота через t секунд \n 9.вы стоите на краю дороги и от вас до длижайшего фонаря x метров. Растояние между столбами - y метров. На каком расстоянии от вас n-й столб \n 10. Ситуация из 9 задачи. Длина вашего шага z метров. Мимо скольких столбов вы пройдете следав n шагов \n 11.X-вещественное число - запишите выражение позволяющее выделить его дробную часть. \n 12. округлит до сотых долей. \n 13. От бревна длиной L отпиливают куски лдиной x. Сколько уелый кусков отпилят \n 14. Бревно длиной L распилил в n местах. Какова сердняя длина куска \n 15.Резиновое кольцо диаметром d разрезали в n местах. Сердняя длина куска \n 0.Выход \n')
    i = int(input('Выберете задачу: '))
    if i == 1:
        n = int(input('Введите n: '))
        print('%d-е четное число: %d' %(n, (n * 2)))
        input("Нажмите ENTER")
    elif i == 2:
         n = int(input('Введите n: '))
         print('%d-е нечетное число: %d ' %(n, (n * 2 - 1)))
         input("Нажмите ENTER")
    elif i == 3:
         i3 = int(input('i-й человек: '))
         k3 = int(input('k-й человеа: '))
         print("Между %d-м и %d-м человеком стоит %d человек(а)" %(i3,k3,(abs(k3 - i3)-1)))
         input("Нажмите ENTER")
    elif i == 5:
         x5=int(input("ВВедите x: "))
         h5=x5//3600
         mt=x5-h5
         m5=x5%3600//60
         s5=x5%3600%60
         print("В %d Секундах - %d часов, %d минут, %d -секунд" %(x5,h5,m5,s5))    
         input("Нажмите ENTER")
    elif i == 6:
         r6=int(input("Введите номер квартры: "))
         p6=(r6-1)//36+1
         f6=(r6-1)%36//4+1
         print("%d квартира находится в %d подъезде на %d этаже" %(r6,p6,f6))    
         input("Нажмите ENTER")
    elif i == 7:
         k7=int(input("Введите количесвто копеек: "))
         r7=k7//100
         g7=k7%100//10
         a7=k7%100%10//3
         p7=k7%100%10%3//0.25
         print("В %d копейках - %d рублей %d гривенников %d алтынов и %d полушек" %(k7,r7,g7,a7,p7))    
         input("Нажмите ENTER")
    elif i == 9:
         m9=int(input("Сколько метров до ближайшего столба: "))
         r9=int(input("Сколько метров между столбами: "))
         s9=int(input("До какого столба считаем: "))
         t9=m9+r9*(s9-1)
         print("До %d столба - %d метров" %(s9, t9))    
         input("Нажмите ENTER")
    elif i == 10:
         m10=int(input("Сколько метров до ближайшего столба: "))
         r10=int(input("Сколько метров между столбами: "))
         l10=float(input("Длина шага: "))
         n10=int(input("Сколько шагов идем: "))
         t10=(n10*l10-m10)//r10
         print("Пройдено %d столбов" %t10)    
         input("Нажмите ENTER")
    elif i == 11:
         n11=float(input("Введите вещественное число:"))
         print("Целая часть числа %f  (int(%f)) и составляет %d " %(n11, n11, int(n11)))    
         input("Нажмите ENTER")
    elif i == 12:
         n12=float(input("Введите вещественное число:"))
         print("Округление до сотых через round(%f, 2).Число %f при округлении получим %.2f" %(n12, n12, round(n12, 2)))    
         input("Нажмите ENTER")
    elif i == 13:
         b13=float(input("Длина бревна: "))
         x13=float(input("Длина куска: "))
         print("Можно отпилить %d цельных кусков" %(b13//x13))    
         input("Нажмите ENTER")
    elif i == 14:
         b14=float(input("Длина бревна: "))
         x14=int(input("количество распилов: "))
         print("Средняя длина куска %.2f метров" %(b14/(x14+1)))    
         input("Нажмите ENTER")
    elif i == 15:
         d15=float(input("Введите диаметр кольца: "))
         r15=int(input("Введите количество разрезов: "))
         print("Средняя длина разрезов %f" %(3.14*d15/r15))    
         input("Нажмите ENTER")
