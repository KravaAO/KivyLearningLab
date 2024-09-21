''' розрахунки результатів проби Руфіє.

Сума вимірювань пульсу у трьох спробах (до навантаження, одразу після та після короткого відпочинку)
в ідеалі має бути не більше 200 ударів на хвилину.
Ми пропонуємо дітям вимірювати свій пульс протягом 15 секунд,
і наводимо результат до ударів за хвилину множенням на 4:
    S = 4* (P1 + P2 + P3)
Що далі цей результат від ідеальних 200 ударів, то гірше.
Традиційно таблиці даються для величини, поділеної на 10.


Індекс Руф’є
   IR = (S - 200) / 10
оцінюється за таблицею відповідно до віку:
           7-8             9-10             11-12          13-14                15+
                                                                      (тільки для підлітків!)
чуд.    6.4 і менше    4.9 і менше       3.4 і менше    1.9 і менше          0.4 і менше
доб.    6.5 - 11.9     5 - 10.4          3.5 - 8.9      2 - 7.4              0.5 - 5.9
задов.  12 - 16.9      10.5 - 15.4       9 - 13.9       7.5 - 12.4           6 - 10.9
слабкий 17 - 20.9      15.5 - 19.4       14 - 17.9      12.5 - 16.4          11 - 14.9
незад.  21 і більше    19.5 і більше     18 і більше    16.5 і більше        15 і більше


для будь-якого віку результат "незадовільно" віддалений від "слабкого" на 4,
той від "задовільного" на 5, а "добрий" від "чуд" - на 5.5


тому напишемо функцію ruffier_result(r_index, level), яка отримуватиме
розрахований індекс Руф'є та рівень "незадовільно" для віку тестованого, і віддавати результат '''
# тут задаються рядки, за допомогою яких викладено результат:
txt_nodata = ''' Немає даних для такого віку '''
txt_res = []
txt_res.append(''' Низька. Терміново зверніться до лікаря! ''')
txt_res.append(''' Задовільна. Зверніться до лікаря! ''')
txt_res.append(''' Середня. Можливо, варто додатково обстежитись у лікаря. ''')
txt_res.append(''' Вище середнього ''')
txt_res.append(''' Висока ''')
def rufier_ind(a,b,c):
    return int((4*(a+b+c)-200)/10)


def heartwork (age,ind):
    global text_res
    if age <7 or age>18:
        return txt_nodata
    if age==7 or age==8:
        if ind<=6.4:
            return text_res[4]
        if ind>6.4 and ind<12:
            return text_res[3]
        if ind>11.9 and ind<17:
            return text_res[2]
        if ind>16.9 and ind<21:
            return text_res[1]
        if ind>20.9 :
            return text_res[0]
    if age==9 or age==10:
        if ind<=6.4:
            return text_res[4]
        if ind>6.4 and ind<12:
            return text_res[3]
        if ind>11.9 and ind<17:
            return text_res[2]
        if ind>16.9 and ind<21:
            return text_res[1]
        if ind>20.9 :
            return text_res[0]
    if age==11 or age==12:
        if ind<=6.4:
            return text_res[4]
        if ind>6.4 and ind<12:
            return text_res[3]
        if ind>11.9 and ind<17:
            return text_res[2]
        if ind>16.9 and ind<21:
            return text_res[1]
        if ind>20.9 :
            return text_res[0]
    if age==13 or age==14:
        if ind<=6.4:
            return text_res[4]
        if ind>6.4 and ind<12:
            return text_res[3]
        if ind>11.9 and ind<17:
            return text_res[2]
        if ind>16.9 and ind<21:
            return text_res[1]
        if ind>20.9 :
            return text_res[0]
    if age>=15:
        if ind<=6.4:
            return text_res[4]
        if ind>6.4 and ind<12:
            return text_res[3]
        if ind>11.9 and ind<17:
            return text_res[2]
        if ind>16.9 and ind<21:
            return text_res[1]
        if ind>20.9 :
            return text_res[0]
