## Экран Галереи ##############################################################
##
## Экран Галереи содержит персонажей и иллюстрации
##
###############################################################################

screen galery():
    add "gui/images/galery/galery_bg.png" 
    imagebutton auto "gui/button/return_button_%s.png" xpos 43 ypos 24 focus_mask True action ShowMenu("main_menu"), Hide ("galery")   