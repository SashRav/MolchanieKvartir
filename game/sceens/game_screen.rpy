## Дисклеймер ##########################################################
## Выводит дисклеймер в начале игры                                   ##
########################################################################

screen GameGuide():
    add "gui/images/d_1/d_1_valya.png" 
    vbox xpos 387 ypos 160:
        add "gui/images/d_1/instructions.png"
     

#######################################################################
## Добавление картинка в глалерею                                    ##
####################################################################### 

screen ill_note():
    #style_prefix "notify_text"     
    #add "gui/notify1.png" ########### переписать на добавление картинки из атрибута. Функция должна принимать значиние img
    text "Галерея обновлена" xpos 20 ypos 7 size 20


#######################################################################
##         Выбор персонажа                                           ##
####################################################################### 
screen ChoiceChar():
    tag menu
    modal True 
    add "gui/images/char_choice/choice_char_bg.png"
    add "gui/images/char_choice/choice_char_card.png" xpos 387 ypos 160
    imagebutton auto "gui/images/char_choice/misha_%s.png" xalign 0.1 yalign 1.1 action Jump("misha_root"), Hide ("ChoiceChar")
    imagebutton auto "gui/images/char_choice/valya_%s.png" xalign 0.85 yalign 1.1 action Jump("valya_root"), Hide ("ChoiceChar")


#######################################################################
##         Экран быстрого меню                                       ##
####################################################################### 

screen quick_menu():
    
    ## Ensure this appears on top of other screens.
    zorder 100

    hbox:
        xpos 70
        ypos 609
        hbox: 
            imagebutton auto "gui/button/game_menu/text_back_%s.png" action Rollback()
            #textbutton _("Авто") xpos 760 ypos 40 action Preference("auto-forward", "toggle")
            imagebutton auto "gui/button/game_menu/main_menu_button_%s.png" xpos 910 ypos -5  action MainMenu()
    if quick_menu_button:
        use quick_menu_button

    textbutton _("Авто") xpos 938 ypos 550 action Preference("auto-forward", "toggle")    
    
default quick_menu = True

style quick_button is default
style quick_button_text is button_text


###############################################################
##       Кнопка открытия игровог внутреннего меню            ##
###############################################################

default quick_menu_button = True

screen quick_menu_button():
    imagebutton auto "gui/button/game_menu/game_menu_button_%s.png" xalign 1.0 focus_mask True action Show("game_menu_small"), SetVariable("quick_menu_button", False)

###############################################################
##       Игровое внутреннее меню                             ##
###############################################################

screen game_menu_small():
    add "gui/button/game_menu_small/game_menu_small.png" xalign 1.0
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xalign 1.0 focus_mask True action Hide("game_menu_small"),  SetVariable("quick_menu_button", True)
    vbox xalign 0.882 ypos 42 spacing 30:
        imagebutton auto "gui/button/game_menu_small/game_skip_%s.png" xpos -3 action Skip() alternate Skip(fast=True, confirm=True), Hide("game_menu_small")
        imagebutton auto "gui/button/game_menu_small/game_save_%s.png" action ShowMenu('save')
        
    vbox xalign 0.97 ypos 35 spacing 27:
        imagebutton auto "gui/button/game_menu_small/game_options_%s.png" action ShowMenu('preferences'), Hide("game_menu_small")
        imagebutton auto "gui/button/game_menu_small/game_load_%s.png" action ShowMenu('load'), Hide("game_menu_small")


init python:
    import time

screen ill_note():
    add "gui/images/notify.png"
    text "Галерея обновлена" xpos 20 ypos 7 size 20
    timer 2.0 action Hide("ill_note")