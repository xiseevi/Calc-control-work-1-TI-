# calc v0.6 no_module
print('Калькулятор')
# print('text') - функция вывода текста на экеран
# функция калькулятор
def calc():
    # int - это целочисленное значение (целое чилорс);
    # f - це переменная через котору будем выбирать необходимую функцию калькулятора;
    # input - ввод с клавиатуры;
    # \n"текст" - текст пишется с новой строки;
    f = int(input('Выберите функцию \nСложение -- 1\nВычитание -- 2\nУмножение -- 3\nДеление -- 4\nВозведение в степень -- 5\nЛогарифм -- 6\nОкругление в большую сторону до N знака после запятой -- 7\nОкругление в меньшую сторону до N знака после запятой -- 8\n'))

    if f == 1:
    # if (If-elif-else) - условная конструкция (if f == 1: если Ф ровно одному используется функция сложения)
    # == (два ровно) - математический оператор который означает ровно(=), проверяет одинаковы ли объекты    
        try:
            ch1 = int(input('Введите первое число: '))
        except:
            print('Введенный элемент не является числом, введите первый элемент:')
            ch1 = int(input('Введите первое число: '))
        # try & except - це проверка на исключение, т.е. при не верном значении, просит повторить попытку и ввести число сново.    
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
            ch2 = int(input('Введите второе число: '))
        r = float(ch1 / ch2)
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
        ch1_approx = 0.0
        n = 100
        for i in range(1, n+1):
            # for i in range(1, n+1) - цикл повторения, где n кол-во повторений. В данном случае это цилк для обчесления логарифма.    
                ch1_approx = ((-1) ** (i - 1)) * ((ch1 - 1) ** i) / i
                # ch1_approx - формула вычесления натурального логарифма.
        x = ch1_approx
        ch2_approx = 0.0
        n = 100
        for i in range(1, n+1):
                ch2_approx = ((-1) ** (i - 1)) * ((ch2 - 1) ** i) / i
        base = ch2_approx
        result = x / base
        # result - результат логарифма где X, он же ch1 аргумент, а ch2 основание.
        print(f'Ваш результат: log {ch2}({ch1}) = {result}')
        # тест в выодимый на экран можно добавлять переменные, для этого надо добавт Ф перед текстом, а сами переменные писать в ковычки {переменная}.
    elif f == 7:
    # эльф ф == 7 - функция округления числа в большую сторону, до ближайшего целого числа.    
        try:
            ch1 = float(input('Введите число: '))
        except:
            print('Введенный элемент не является числом, введите элемент:')
            ch1 = float(input('Введите число: '))
        r = round(ch1)
        # round(не целое число) - функция округления числа.
        print('Ваш результат:',r)
        
    elif f == 8:
    # эльф ф == 8 - округление в меньшую сторону.    
        try:
            ch1 = float(input('Введите число: '))
        except:
            print('Введенный элемент не является числом, введитe элемент:')
            ch1 = float(input('Введите число: '))
        r = int(ch1)
        # int - это не только целочисленное значение (целое число), а так же функция преобразования действительных значений целому путем округления в сторону нуля.
        print('Ваш результат:',r)
        
    ask = input('Продолжить?(Да/Нет): ')
    # ask - переменная в которой мы спрашиваем, хотим ли продолжить использовать сея произведения кодинга.
    if ask == 'Да' or ask == 'да':
        calc()
    # если вводится ответ Да/да, мы возвращаемся в начало операции.    
    else:
        g = int(input('Конець')) 
     # кастыль для удобства закрытия программы.    
calc()
# ебать, оно работает!
