# calc v0.8.5 module math
# Махмудовъ Андрей, сынъ Владиміра. 
# Группа 4305, Ленинградскій ордена ​Октяборьской​ революціи и ордена Трудового Краснаго Знамени технологическій институтъ имени ​Ленсовѣта​.
import math
# import - импортъ изъ библіотекъ. math - математическая библіотека.
# подключаемъ математическую библіотеку.

print('Калькоулѧторъ:')
# print('text') - функція вывода текста на экранъ 


def calc():
# функция калькулятор
    while True:
    # зацикливаем программу.
        try:
            f = int(input('Выберите фоункцїю: \nСложенїѥ -- 1\nВычитанїѥ -- 2\nОумноженїѥ -- 3\nДеленїѥ -- 4\nВоzведенїѥ в степень -- 5\nЛогарифмъ -- 6\nѺкрѫглениѥ ​въ​ большоую страноу до N ​zнака​ послѣ zапѧтои -- 7\nѺкрѫгленїѥ ​въ​ меньшоую страноу до N ​zнака​ послѣ zапѧтои -- 8\nИли ​любои​ дрѫгои ​не​ численыи сvмволъ длѧ ​выхода.\n'))
        except ValueError:
            print("выходъ")
            break  
            # вꙑходъ иꙁъ ​цикла​ при ​ввѫде​ нечислового ꙁначѥнїꙗ;
            # int - ​ѥто​ целочисленноѥ ​ꙁначенїѥ​ (цѣлоѥ чилорсъ);
            # f - цѣ прѣменнаꙗ чрѣꙁъ ​котороу​ бѫдемъ вꙑбирать неѻбходимоую фоункцїю калькоулѧтора;
            # input - ​ввѫдъ​ съ клавїꙗтоурꙑ;
            # \n"​текстъ​" - ​текстъ​ пишетсѧ съ новои ​строкꙑ​;

        if f == 1:
            # if (If-elif-else) - Ѻоусловнаꙗ констроукцїꙗ (if f == 1: ꙗще ​ф​ ​ровно​ ѻдномоу ​то​ испольꙁоуѥтсѧ фоункцїꙗ ​сложенїꙗ​);
            # == (два ​ровно​) - математическꙑи ѻператоръ которꙑи ѡꙁначаѥтъ ​ровно​(=) проверѧѥтъ ѻдинаковꙑ ли ѻбъѥктꙑ;
            try:
                ch1 = int(input('Введите первоѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = int(input('Введите первоѥ число: '))
            try:
                ch2 = int(input('Введите ​втраѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch2 = int(input('Введите ​втраѥ число: '))
            r = ch1 + ch2
            print('Вашъ реzоультатъ:',r)
            # r - прѣменнаꙗ ​котораꙗ​ ​въ​ ​данномъ​ ​слѫчаѥ​ ꙗвлѧѥтсѧ реꙁоультатомъ ​сложенїꙗ​ ​ꙁначенїи​ А+Б.
            # print('text' x) - съ помощїю фоункцїи ввꙑвѫда ​текста​ на ѥкранъ можно ​вꙑвѫдить​ ​ꙁначенїѥ​ прѣменнои ​раꙁнꙑѥ​ прѣменнꙑѥ междоу ​собои​ надо раꙁделѧть ꙁапѧтои.
    
        elif f == 2:
        # elif f == 2 испольꙁоуѥтсѧ фоункцїꙗ вꙑчитанмїꙗ.
            try:
                ch1 = int(input('Введите первоѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = int(input('Введите первоѥ число: '))
            try:
                ch2 = int(input('Введите ​втраѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch2 = int(input('Введите ​втраѥ число: '))
            r = ch1 - ch2
            print('Вашъ реzоультатъ:',r)
            # ​Въ​ ​данномъ​ ​слѫчаѥ​ прѣменнаꙗ "r" реꙁоультатъ вꙑчитанїꙗ.

        elif f == 3:
        # elif f == 3 - фоункцїꙗ ​Ѻоумножѥнїꙗ​.
            try:
                ch1 = int(input('Введите первоѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = int(input('Введите первоѥ число: '))
            try:
                ch2 = int(input('Введите ​втраѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch2 = int(input('Введите ​втраѥ число: '))
            r = ch1 * ch2
            # * (ЗВЕЗДОЧКА) - ѻператоръ ​ѻоумножѥнїꙗ​.
            print('Вашъ реzоультатъ:',r)
            # в данном случае переменная "r" результат умножения.
        
        elif f == 4:
        # elif f == 4 - фоункцїꙗ дѣлѥнїꙗ.     
            try:
                ch1 = int(input('Введите первоѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = int(input('Введите первоѥ число: '))
            try:
                ch2 = int(input('Введите ​втраѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch2 = int(input('Введите ​втраѥ число: '))
            if ch2 != 0:
            # != 0 ​ꙁапрѣтъ​ конкретого ꙁначѥнїꙗ ​въ​ ​данномъ​ ​слѫчаѥ​ ​ноулѧ​ т.къ. делить на ​ноль​ нельꙁѧ!
            # != математическꙑи ѻператоръ которꙑи ѡꙁначаѥтъ ​не​ ​ровно​! Проверѧѥтъ ​вѣрно​ ли что ѻбъѥктꙑ ​не​ равнꙑ x = 2; y = 3; x != y даѥтъ Tru.
                r = float(ch1 / ch2)
            else:
                print('На ​ноль​ делить нельzѧ!')
                ask = input('​Продолжить?(Да/Нѣтъ): ')
                # ask - прѣменнаꙗ ​въ​ ​котраи​ мꙑ ​спрашиваѥмъ​ ​хотимъ​ ли ​продолжить​ испольꙁовать ​сеꙗ​ проиꙁведенїꙗ кодинга.
                if ask == 'Да' or ask == 'да':
                    calc()
                    # ꙗще ввѫдитсѧ ѿвѣтъ да/да мꙑ воꙁвращаѥмсѧ ​въ​ начало ѻперацїи.   
                else:
                    g = int(input('<=== To be continued...')) 
        
            # / (дробь наклоненаꙗ палочка на 45 градоусовъ ѿносительно ​строкꙑ​) - ѻператоръ дѣлѥнїꙗ.
            # // - ѻператоръ целочисленного дѣлѥнїꙗ даѥтъ ​толико​ цѣлоѥ число.
            # float - ​ꙁначенїѥ​ съ плавоющеи ​точкои​. напрнимеръ: 3,1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091....
            print('Вашъ реzоультатъ:',r)
        
        elif f == 5:
        # элиф ф == 5 фоункцїꙗ ​воꙁведенїꙗ​ ​въ​ степень. (​типо​ маленькаꙗ цифорка надъ ​больнои​ виситъ).
            try:
                ch1 = int(input('Введите первоѥ число '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = int(input('Введите первоѥ число: '))
            try:
                ch2 = int(input('Введите ​втраѥ число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch2 = int(input('Введите ​втраѥ число: '))
            r = ch1 ** ch2
            # ** (двѣ ꙁвеꙁдочкꙑ ​не​ ѻдна, ​не​ три, а двѣ) - ѻператоръ ​воꙁведенїꙗ​ ​въ​ ​стпень​. воꙁвращаѥтъ число X ​воꙁведенноѥ​ ​въ​ степень Y (X**Y).
            print('Вашъ реzоультатъ:',r)
        
        elif f == 6:
        # эльф Ф == 6 - фоункцїꙗ логарифма (​ѧ​ ​въ​ ​доушѣ​ ​не​ ​ебу что такоѥ логарифмъ =) ).     
            try:
                ch1 = int(input('введите логарифмъ: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = int(input('введите логарифмъ: '))
            try:
                ch2 = int(input('введите ​ѻснованїѥ​: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch2 = int(input('введите ​ѻснованїѥ​:: '))
            r = math.log(ch1, ch2)
            print(f'Вашъ реzоультатъ: log{ch2}({ch1}) = {r}')
                # .log(x, base) - фоункцїꙗ ​въ​ модоуле 'math' длѧ вꙑчесленїꙗ логарифма.
                # ​оу​ ​менѧ​ ѥсть небольшїѥ пѫдоꙁрѣнїꙗ что логарифмъ ​ѻнъ​ ​не​ правильнѡ ​считаѥтъ​ но ​ꙗꙁъ​ ​хꙁ​ ​поѥтомоу​ ​и​ такъ ​соидетъ​)))
            
        elif f == 7:
        # эльф ф == 7 - фоункцїꙗ ѻкрѫгленїꙗ числа ​въ​ большоую страноу до ближаишего целого числа.  
            try:
                ch1 = float(input('введите число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = float(input('введите число: '))
            r = math.ceil(ch1)
            # .ceil - фоункцїꙗ иꙁъ модоулѧ math ​котораꙗ​ ѻкрѫглѧѥтъ ꙁначѥнїꙗ ​въ​ большоую страноу.
            print('Вашъ реzоультатъ:',r)
        
        elif f == 8:
        # эльф ф == 8 - ѻкрѫгленїѥ ​въ​ меньшоую страноу.    
            try:
                ch1 = float(input('введите число: '))
            except:
                print('Введенныи ѥлементъ ​не​ явлѧѥтсѧ числомъ введите ​втраи​ ѥлементъ: ')
                ch1 = float(input('введите число: '))
            r = math.floor(ch1)
            # .floor - фоункцїꙗ иꙁъ модоулѧ math ​котораꙗ​ ѻкрѫглѧѥтъ ꙁначѥнїꙗ ​въ​ меньшоую страноу.
            print('Вашъ реzоультатъ:',r)
calc()
# ебать, воно працює!
