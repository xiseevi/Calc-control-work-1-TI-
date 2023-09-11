# calc v0.7 module math
# made by Mahmduov A.V., group 4305, SPB GTI(TU).
import math
# import - импорт из библиотек. math - математическая библиотека.
# подключаем математическую библиотеку

print('Калькулятор')
# print('text') - функция вывода текста на экеран

# функция калькулятор
def calc():
    # int - это целочисленное значение (целое чилорс);
    # f - це переменная через котору будем выбирать необходимую функцию калькулятора;
    # input - ввод с клавиатуры;
    # \n"текст" - текст пишется с новой строки;
    f = int(input('Выберите функцию \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в степень -- 5\nЛогарифм -- 6\nОкругление в большую сторону до N знака после запятой -- 7\nОкругление в меньшую сторону до N знака после запятой -- 8\n'))
    # if (If-elif-else) - условная конструкция (if f == 1: если Ф ровно одному, то используется функция сложения)
    # == (два ровно) - математический оператор который означает ровно(=), проверяет одинаковы ли объекты
    if f == 1:
        try:
            ch1 = int(input('Введите первое число: '))
        except:
            print('Введенный элемент не является числом, введите первый элемент:')
            ch1 = int(input('Введите первое число: '))
        try:
            ch2 = int(input('Введите второе число: '))
        except:
            print('Введенный элемент не является числом, введите второй элемент:')
            ch2 = int(input('Введите второе число: '))
        r = ch1 + ch2
        print('Ваш результат:',r)
        # r - переменная которая в данном случае является результатом сложения значений А+Б
        # print('text', x) - с помощью функции ввывода текста на экран можно выводить значение переменной, разные переменные между собой надо разделять запятой.
    
    elif f == 2:
    # elif f == 2 используется функция вычитанмия.
        try:
            ch1 = int(input('Введите первое число: '))
        except:
            print('Введенный элемент не является числом, введите первый элемент:')
            ch1 = int(input('Введите первое число: '))
        try:
            ch2 = int(input('Введите второе число: '))
        except:
            print('Введенный элемент не является числом, введите второй элемент:')
            ch2 = int(input('Введите второе число: '))
        r = ch1 - ch2
        print('Ваш результат:',r)
        # в данном случае переменная "r" результат вычитания.

    elif f == 3:
    # elif f == 3 - функция умножения.
        try:
            ch1 = int(input('Введите первое число: '))
        except:
            print('Введенный элемент не является числом, введите первый элемент:')
            ch1 = int(input('Введите первое число: '))
        try:
            ch2 = int(input('Введите второе число: '))
        except:
            print('Введенный элемент не является числом, введите второй элемент:')
            ch2 = int(input('Введите второе число: '))
        r = ch1 * ch2
        # * (ЗВЕЗДОЧКА) - оператор умножения.
        print('Ваш результат:',r)
        # в данном случае переменная "r" результат умножения.
        
    elif f == 4:
    # elif f == 4 - функция деления.     
        try:
            ch1 = int(input('Введите первое число: '))
        except:
            print('Введенный элемент не является числом, введите первый элемент:')
            ch1 = int(input('Введите первое число: '))
        try:
            ch2 = int(input('Введите второе число: '))
        except:
            print('Введенный элемент не является числом, введите второй элемент:')
            ch2 = int(input('Введите второе число: ')
        if ch2 != 0:
        # != 0 запрет конкретого значения, в данном случае нуля, т.к. делить на ноль нельзя!
            r = float(ch1 / ch2)
        else:
            print('На ноль делить нельзя')
            ask = input('Продолжить?(Да/Нет): ')
            # ask - переменная в которой мы спрашиваем, хотим ли продолжить использовать сея произведения кодинга.
            if ask == 'Да' or ask == 'да':
                calc()
                # если вводится ответ Да/да, мы возвращаемся в начало операции.   
            else:
                g = int(input('<=== To be continued...')) 
        
        # / (дробь, наклоненая палочка на 45 градусов относительно строки) - оператор деления.
        # // - оператор целочисленного деления, дает ТОЛЬКО целое число.
        # float - значение с плавоющей точкой. напрнимер 3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091....
        print('Ваш результат:',r)
        
    elif f == 5:
    # элиф ф == 5 функция возведения в степень. (типо маленькая цифорка над больной висит).
        try:
            ch1 = int(input('Введите первое число: '))
        except:
            print('Введенный элемент не является числом, введите первый элемент:')
            ch1 = int(input('Введите первое число: '))
        try:
            ch2 = int(input('Введите второе число: '))
        except:
            print('Введенный элемент не является числом, введите второй элемент:')
            ch2 = int(input('Введите второе число: '))
        r = ch1 ** ch2
        # ** (две звездочки, не одна, не три, а две) - оператор возведения в стпень. возвращает число X возведенное в степень Y (X**Y).
        print('Ваш результат:',r)
        
    elif f == 6:
    # эльф Ф == 6 - функция логарифма (я в душе не ебу что такое логарифм =) ).     
        try:
            ch1 = int(input('Введите логарифм: '))
        except:
            print('Введенный элемент не является числом, введите логарифм:')
            ch1 = int(input('Введите логарифм: '))
        try:
            ch2 = int(input('Введите основание: '))
        except:
            print('Введенный элемент не является числом, введите основание:')
            ch2 = int(input('Введите основание: '))
        r = math.log(ch1, ch2)
        print(f'Ваш результат: log{ch2}({ch1}) = {r}')
            # .log(x, base) - функция в модуле 'math' для вычесления логарифма.
            # у меня есть небольшие подозрения, что логарифм он не правильно считает, но я хз, поэтому и так сойдет)))
            
    elif f == 7:
    # эльф ф == 7 - функция округления числа в большую сторону, до ближайшего целого числа.    
        try:
            ch1 = float(input('Введите число: '))
        except:
            print('Введенный элемент не является числом, введите элемент:')
            ch1 = float(input('Введите число: '))
        r = math.ceil(ch1)
        # .ceil - функция из модуля math которая округляет значения в большую сторону.
        print('Ваш результат:',r)
        
    elif f == 8:
    # эльф ф == 8 - округление в меньшую сторону.    
        try:
            ch1 = float(input('Введите число: '))
        except:
            print('Введенный элемент не является числом, введитe элемент:')
            ch1 = float(input('Введите число: '))
        r = math.floor(ch1)
        # .floor - функция из модуля math которая округляет значения в меньшую сторону. 
        print('Ваш результат:',r)
        
    ask = input('Продолжить?(Да/Нет): ')
    # ask - переменная в которой мы спрашиваем, хотим ли продолжить использовать сея произведения кодинга.
    if ask == 'Да' or ask == 'да':
        calc()
        # если вводится ответ Да/да, мы возвращаемся в начало операции.   
    else:
        g = int(input('<=== To be continued...')) 
    # кастыль для удобства закрытия программы.    
calc()
# ебать, оно работает!
