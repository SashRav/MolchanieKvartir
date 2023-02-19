## Основные персонажи
define m = Character("Миша", color="#d9f1ff", image="misha")
define v = Character("Валик", color="#ffd9ff", image="valya")
define e = Character("Егор", color="#ffffff", image="egor")
define k = Character("Катя", color="#ffffff", image="katya")
define s = Character("Саша", color="#ffffff", image="sasha")
define o = Character("Отeц", color="#ffffff", image="dad")
define t = Character("Толик", color="#ffffff", image="tolya")
define ka = Character("Кабан", color="#ffffff", image="kaban")
define a = Character("Андрюсёк", color="#ffffff", image="andrusek")
## Второстепенные персонажи
define de = Character("Девочка", color="#ffffff", image="devochka")
define ma = Character("Мать", color="#ffffff", image="mama")
define u = Character("Учитель", color="#ffffff", image="uchitel")
define ne = Character("Некто", color="#ffffff", image="nekto")
define so = Character("Сосед", color="#ffffff", image="sosed")
define se = Character("Соседка", color="#ffffff", image="sosed")
define kv = Character("Катя и Валик", color="#ffffff", image="kiv")
define me = Character("Милиционер", color="#ffffff", image="mil")
define h = Character("Хулиганы", color="#ffffff", image="hul")
define tr = Character("Тренер", color="#ffffff", image="trener")
define vo = Character("Водитель", color="#ffffff", image="voditel")
## Звуки
define audio.musstreet = "audio/sounds/street.mp3"
define audio.musstreet_birds = "audio/sounds/street_birds.mp3"
define audio.muswind = "audio/sounds/wind.mp3"
define audio.musslap = "audio/sounds/slap.mp3"
define audio.musring = "audio/sounds/ring.mp3"
define audio.musschool = "audio/sounds/school.mp3"
define audio.musschool_outside = "audio/sounds/school_outside.mp3"
define audio.musnoise = "audio/sounds/noise.mp3"
define audio.muspool = "audio/sounds/pool.mp3"
define audio.musdoor = "audio/sounds/door.mp3"
define audio.muslock = "audio/sounds/lock.mp3"
define audio.musknock = "audio/sounds/knock.mp3"
define audio.musmetal = "audio/sounds/metal.mp3"
define audio.musdoor_ring = "audio/sounds/door_ring.mp3"

## Музыка
define audio.maintheme = "audio/music/main_theme.OGG"
define audio.musnorm = "audio/music/norm.OGG"
define audio.muslove = "audio/music/love.OGG"
define audio.mussad = "audio/music/sad.OGG"
define audio.musstress = "audio/music/stress.OGG"
define audio.musradio = "audio/music/elvis.OGG"

#классы и расположeниe спрайтов
init:
    $ right2=Position(xalign=0.85, yalign=1.1)
    $ left2=Position(xalign=0.1, yalign=1.1)
    $ up=Position(xalign=0, yalign=0)

# Игра начинается здесь:
label start:

    stop music fadeout 2.0
    #scene "gui/images/d_1_valya.png"

    show screen GameGuide with dissolve
    pause (2)
    hide screen GameGuide with dissolve

    call screen ChoiceChar

    return
