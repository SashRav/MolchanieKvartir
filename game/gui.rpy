################################################################################
## Инициализация
################################################################################

## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.
init offset = -2

## Вызываю gui.init, чтобы сбросить стили, чувствительные к стандартным
## значениям, и задать высоту и ширину окна игры.
init python:
    gui.init(1280, 720)



################################################################################
## Конфигурируемые Переменные GUI
################################################################################


## Цвета #######################################################################
##
## Цвета текста в интерфейсе.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = u'#db027c'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = u'#5f5f5f'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = u'#a1a1a1'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = u'#db027c'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = u'#a5a5a5'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = u'#bebebe'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = u'#003d51'
define gui.hover_muted_color = u'#005b7a'

## The colors used for dialogue and menu choice text.
define gui.text_color = u'#3f4576'
define gui.interface_text_color = u'#3f4576'


## Шрифты и их размеры #########################################################

## The font used for in-game text.
define gui.text_font = "fonts/RobotoSlab-Regular.ttf"

## The font used for character names.
define gui.name_text_font = "fonts/RobotoSlab-Medium.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "fonts/RobotoSlab-Regular.ttf"

## The size of normal dialogue text.
define gui.text_size = 22

## The size of character names.
define gui.name_text_size = 30

## The size of text in the game's user interface.
define gui.interface_text_size = 22

## The size of labels in the game's user interface.
define gui.label_text_size = 24

## The size of text on the notify screen.
define gui.notify_text_size = 16

## The size of the game's title.
define gui.title_text_size = 50


## Главное и игровое меню. #####################################################

## Изображения, используемые в главном и игровом меню.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Диалог ######################################################################
##
## Эти переменные контролируют, как диалог появляется на отдельной строчке.

## The height of the textbox containing dialogue.
define gui.textbox_height = 185

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 300
define gui.name_ypos = -40

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.5

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = 250
define gui.namebox_height = 70

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 744

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Эти переменные, вместе с файлами изображений в gui/button, контролируют
## аспекты того, как отображаются кнопки.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## Эти переменные переписывают настройки различных видов кнопок. Пожалуйста,
## посмотрите документацию по gui для просмотра всех вариаций кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 22
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250


## Кнопки Выбора ###############################################################
##
## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 850
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(200, 40, 200, 40)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5

define gui.choice_button_text_idle_color = "#ffffff"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Кнопки Слотов ###############################################################
##
## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## The save slot button.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиционирование и Интервалы ################################################
##
## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 40

## The vertical position of the skip indicator.
define gui.skip_ypos = 10

## The vertical position of the notify screen.
define gui.notify_ypos = 45

## The spacing between menu choices.
define gui.choice_spacing = 22

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 10



## Рамки #######################################################################
##
## Эти переменные контролируют вид рамок, содержащих компоненты
## пользовательского интерфейса, когда наложения или окна не представлены.

## Generic frames.
define gui.frame_borders = Borders(4, 4, 4, 4)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(40, 30, 40, 30)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Панели, Полосы прокрутки и Ползунки #########################################
##
## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.
##
## Стандартный GUI использует только ползунки и вертикальные полосы прокрутки.
## Все остальные полосы используются только в новосозданных экранах.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vertical borders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.


## История #####################################################################
##
## Экран истории показывает диалог, который игрок уже прошёл.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 140

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Экран режима NVL показывает диалог NVL персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Максимальное число показываемых строк в режиме NVL. Когда количество строчек
## начинает превышать это значение, старые строчки очищаются.
define gui.nvl_list_length = 6

## Высота доступных строчек в режиме NVL. Установите на None, чтобы строчки
## динамически регулировали свою высоту.
define gui.nvl_height = 173

## Интервал между строчками в режиме NVL, если gui.nvl_height имеет значение
## None, а также между строчками и меню режима NVL.
define gui.nvl_spacing = 15

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Местоположение, ширина и выравнивание текста nvl_thought (текст от лица
## персонажа nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## Локализация #################################################################

## Эта настройка контролирует доступ к разрыву линий. Стандартная настройка
## подходит для большинства языков. Список доступных значений можно найти на
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"

