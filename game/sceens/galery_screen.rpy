## Экран Галереи ##############################################################
##
## Экран Галереи содержит персонажей и иллюстрации
##
###############################################################################

screen galery():
    add "gui/images/galery/galery_bg.png" 
    add "gui/button/name_line.png" xpos 25 ypos 17  
    imagebutton auto "gui/button/return_button_%s.png" xpos 43 ypos 24 focus_mask True action ShowMenu("main_menu"), Hide ("galery")   
    add "gui/button/name_galery.png" xpos 90 ypos 32 

    add "gui/images/galery/galery_ribbon.png" ypos -20
    imagebutton auto "gui/images/galery/char_galery_%s.png" xpos 139 ypos 205 focus_mask True action ShowMenu("char_galery"), Hide ("galery")
    imagebutton auto "gui/images/galery/ill_galery_%s.png" xpos 668 ypos 94 focus_mask True action ShowMenu("ill_galery"), Hide ("galery")


screen char_galery():
    add "gui/images/galery/char_galery_bg.png"

    add "gui/button/name_line.png" xpos 25 ypos 17  
    imagebutton auto "gui/button/return_button_%s.png" xpos 43 ypos 24 focus_mask True action ShowMenu("galery"), Hide ("char_galery")   
    add "gui/button/name_char_galery.png" xpos 90 ypos 32 

    hbox xalign 0.5 ypos 75 spacing 20:
        imagebutton auto "gui/images/galery/characters/side_valya_%s.png" focus_mask True action ShowMenu("valya_char_galery")
        imagebutton auto "gui/images/galery/characters/side_misha_%s.png" focus_mask True action ShowMenu("misha_char_galery")
        imagebutton auto "gui/images/galery/characters/side_katya_%s.png" focus_mask True action ShowMenu("katya_char_galery")
        imagebutton auto "gui/images/galery/characters/side_tolya_%s.png" focus_mask True action ShowMenu("tolya_char_galery")
        imagebutton auto "gui/images/galery/characters/side_sasha_%s.png" focus_mask True action ShowMenu("sasha_char_galery")
        imagebutton auto "gui/images/galery/characters/side_egor_%s.png" focus_mask True action ShowMenu("egor_char_galery")
        imagebutton auto "gui/images/galery/characters/side_kaban_%s.png" focus_mask True action ShowMenu("kaban_char_galery")


screen misha_char_galery():
    modal True
    add "gui/images/galery/characters/misha_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("misha_char_galery")

screen valya_char_galery():
    modal True
    add "gui/images/galery/characters/valya_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("valya_char_galery")    
    
screen katya_char_galery():
    modal True
    add "gui/images/galery/characters/katya_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("katya_char_galery")   

screen tolya_char_galery():
    modal True
    add "gui/images/galery/characters/tolya_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("tolya_char_galery")    

screen sasha_char_galery():
    modal True
    add "gui/images/galery/characters/sasha_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("sasha_char_galery")   

screen egor_char_galery():
    modal True
    add "gui/images/galery/characters/egor_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("egor_char_galery") 

screen kaban_char_galery():
    modal True
    add "gui/images/galery/characters/kaban_char_galery.png"
    imagebutton auto "gui/button/game_menu_small/game_close_%s.png" xpos 1090 ypos 83 focus_mask True action ShowMenu("char_galery"), Hide("kaban_char_galery")    



screen ill_galery():

    add "gui/images/galery/char_menu.png" 

    add "gui/button/name_line_black.png" xpos 25 ypos 17  
    imagebutton auto "gui/button/return_button_%s.png" xpos 43 ypos 24 focus_mask True action ShowMenu("galery"), Hide ("ill_galery")   
    add "gui/button/name_ill_galery.png" xpos 90 ypos 32 
    add "gui/images/galery/ill_gallery/ill_galery_pagecount.png"  xpos 800 ypos 12 

    #pages ConditionSwitch (
    #    "current_page = 1", "ill_gallery_scr_1",
     #   "current_page = 2", "ill_gallery_scr_2",
     #   )
    default current_page = 1
    
    if current_page == 1:
        use ill_gallery_scr_1
    if current_page == 2:
        use ill_gallery_scr_2
    if current_page == 3:
        use ill_gallery_scr_3
    if current_page == 4:
        use ill_gallery_scr_4
    if current_page == 5:
        use ill_gallery_scr_5
    if current_page == 6:
        use ill_gallery_scr_6

    textbutton _("1"):
        text_size 36 
        xpos 850 
        ypos 22
        text_idle_color "#ffffff"
        text_hover_color "#c0c0c0"
        action SetScreenVariable("current_page", 1)


    textbutton _("2"):
        text_size 36 
        xpos 900 
        ypos 22
        text_idle_color "#ffffff"
        text_hover_color "#c0c0c0"
        text_selected_idle_color "#c0c0c0"
        action SetScreenVariable("current_page", 2)

    textbutton _("3"):
        text_size 36 
        xpos 950 
        ypos 22
        text_idle_color "#ffffff"
        text_hover_color "#c0c0c0"
        text_selected_idle_color "#c0c0c0"
        action SetScreenVariable("current_page", 3)
    
    textbutton _("4"):
        text_size 36 
        xpos 1000 
        ypos 22
        text_idle_color "#ffffff"
        text_hover_color "#c0c0c0"
        text_selected_idle_color "#c0c0c0"
        action SetScreenVariable("current_page", 4)

    textbutton _("5"):
        text_size 36 
        xpos 1050 
        ypos 22
        text_idle_color "#ffffff"
        text_hover_color "#c0c0c0"
        text_selected_idle_color "#c0c0c0"
        action SetScreenVariable("current_page", 5)

    textbutton _("6"):
        text_size 36 
        xpos 1100 
        ypos 22
        text_idle_color "#ffffff"
        text_hover_color "#c0c0c0"
        text_selected_idle_color "#c0c0c0"
        action SetScreenVariable("current_page", 6)




screen ill_gallery_scr_1():
    add "gui/images/galery/ill_gallery/ill_locked.png" xpos 150 ypos 150

screen ill_gallery_scr_2():
    add "gui/images/galery/ill_gallery/ill_locked.png" xpos 150 ypos 500

screen ill_gallery_scr_3():
    add "gui/images/galery/ill_gallery/ill_locked.png" xpos 750 ypos 150

screen ill_gallery_scr_4():
    add "gui/images/galery/ill_gallery/ill_locked.png" xpos 750 ypos 500

screen ill_gallery_scr_5():
    add "gui/images/galery/ill_gallery/ill_locked.png" xpos 300 ypos 150

screen ill_gallery_scr_6():
    add "gui/images/galery/ill_gallery/ill_locked.png" xpos 300 ypos 500