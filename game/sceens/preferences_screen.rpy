## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
###############################################################################

screen preferences():

    add "gui/images/preferences/bg.png"
    modal True  
    
    add "gui/button/name_line_black.png" xpos 25 ypos 17  
    imagebutton auto "gui/button/return_button_%s.png" xpos 43 ypos 24 focus_mask True action Return()    
    add "gui/button/name_options.png" xpos 90 ypos 30
    
    tag menu
    #use game_menu(_("Настройки"), scroll="viewport"):
    vbox xalign 0.5 yalign 0.5: 
        add "gui/images/preferences/settings_bg.png"
    hbox xalign 0.5 yalign 0.5:
        vbox:
            if config.has_music:
                style_prefix "slider"
                label _("Музыка")
                hbox:
                    bar: 
                        value Preference("music volume")
                        left_bar "gui/slider/bar_empty.png"
                        right_bar "gui/slider/bar_hover.png"

            if config.has_sound:
                style_prefix "slider"
                label _("Звуки")
                hbox:
                    bar:
                        value Preference("sound volume")
                        left_bar "gui/slider/bar_empty.png"
                        right_bar "gui/slider/bar_hover.png"   
            vbox:
                style_prefix "slider"
                label _("Скорость текста")
                bar: 
                    value Preference("text speed")
                    left_bar "gui/slider/bar_empty.png"
                    right_bar "gui/slider/bar_hover.png"   
                
                label _("Скорость авточтения")
                bar:
                    value Preference("auto-forward time")
                    left_bar "gui/slider/bar_empty.png"
                    right_bar "gui/slider/bar_hover.png"   
            vbox:
                style_prefix "radio"
                label _("Режимы экрана")
                hbox:
                    textbutton _("Полный") action Preference("display", "fullscreen")
                    textbutton _("Оконный") action Preference("display", "window")
    
    imagebutton auto "gui/images/preferences/exit_button_%s.png" xpos 535 ypos 590 focus_mask True action Return()    


style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox


style radio_hbox:
    spacing 150
    xcenter 0.7

style radio_label:
    top_margin 30
    xcenter 0.7

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style slider_slider:
    xsize 523

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_label:
    xcenter 0.5 