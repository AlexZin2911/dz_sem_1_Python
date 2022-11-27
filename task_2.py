# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите число x:'))
y = int(input('Введите число y:'))
z = int(input('Введите число z:'))

if (x == 0 and y == 0 and z == 0):
    print ('Выражение истинно')
else:
    if (x == 0 and y == 0 and z == 1):
        print ('Выражение истинно')
    else:
        if (x == 0 and y == 1 and z == 0):
            print ('Выражение истинно')
        else:
            if (x == 0 and y == 1 and z == 1):
                print ('Выражение истинно')
            else:
                if (x == 1 and y == 0 and z == 0):
                    print ('Выражение истинно')
                else:
                    if (x == 1 and y == 0 and z == 1):
                        print ('Выражение истинно')
                    else:
                        if (x == 1 and y == 1 and z == 0):
                            print ('Выражение истинно')
                        else:
                            if (x == 1 and y == 1 and z == 1):
                                print ('Выражение истинно')
                            else:
                                print('Выражение ложно')