image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "Сегодня день фестиваля."
    "Больше всех прочих, я рассчитывал, что именно в этот день я буду идти в школу вместе с Сайори."
    "Но Сайори не берёт трубку."
    "Я думал прийти к ней домой и разбудить её, но решил, что это будет уже слишком."
    "Тем временем, подготовка к мероприятию должна быть почти завершена."
    if ch4_scene == "natsuki":
        "Я смог принести все кексы сам, аккуратно поставив один поднос на другой."
        "Нацуки уже отправляет мне кучу сообщений, но у меня заняты руки, я не могу ответить."
    else:
        "Баннер, который мы с Юри рисовали, уже высох, и я аккуратно свернул его, чтобы взять с собой."
        "Она отправила мне сообщение, ненавязчиво напоминающее о том, чтобы я ничего не забыл."
    "Как ни странно, я, наверное, чувствовал по отношению к мероприятию то же самое, что и Нацуки."
    "Я больше ждал, чтобы оно закончилось, и я смог провести время с Сайори и [ch4_name] на фестивале."
    "Но, зная Монику, я был уверен, что мероприятие тоже будет отличным."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "Ты сегодня первый."
    m "Спасибо, что пришёл так рано!"
    mc "Забавно, я думал, что, по крайней мере, Юри уже придёт к этому времени."
    "Моника раскладывает маленькие буклеты на каждый стол в классной комнате."
    "Это, должно быть, те, которые она подготовила, в них все поэмы, которые мы будем исполнять."
    "В конце концов, я взял первую попавшуюся поэму из интернета, и мне показалось, что она понравится Монике, и я предложил её."
    "Эту поэму я и буду исполнять."
    m 1d "Странно, что ты не привёл Сайори с собой."
    mc "Да, она опять проспала..."
    mc "Глупышка."
    mc "Казалось бы, в такие важные дни она могла хотя бы постараться..."
    "Я сказал это и внезапно вспомнил, что Сайори сказала мне вчера..."
    "И вдруг я почувствовал себя ужасно, зная, что всё это совсем не просто для неё."
    "Я сказал это только потому, что привык так думать."
    "Но..."
    "Может, мне всё же следовало зайти и разбудить её?"
    m 1k "Ахаха."
    m 4b "Тебе стоит лучше приглядывать за ней, [player]!"
    m "В смысле, особенно после ваших с ней откровений вчера..."
    m "Ты как бы оставил её в подвешенном состоянии дома этим утром, знаешь ли?"
    show monika 4a
    mc "Откровений?.."
    mc "Моника -- ты знаешь об этом??"
    m 2a "Конечно знаю."
    m "Я ведь президент клуба, как-никак."
    mc "Но--!"
    "Смущённый, я запинаюсь."
    "Сайори правда так быстро рассказала ей об этом?"
    if sayori_confess:
        "Что мы... теперь пара?"
        "Пока что я не планировал кому-либо рассказывать об этом..."
    else:
        "О том, как я, по сути, отверг её признание?"
        "Это правда выставляет меня плохим парнем..."
        "Но ведь это я тот, кто знает, что для неё лучше, да?"
    mc "Блин..."
    mc "Ты не знаешь всю историю, так что..."
    m 2j "Не волнуйся."
    m "Возможно, я знаю намного больше, чем ты думаешь."
    mc "Э-э?.."
    "Моника дружелюбна, как всегда, но почему-то после её слов по моей спине прошёлся холодок."
    m 5 "Эй, не хочешь посмотреть брошюры?"
    m "Они получились очень хорошими!"
    mc "Да, конечно."
    "Я взял одну из брошюр, лежавших на столе."
    mc "Ох да, они и правда хороши."
    mc "Что-то такое точно поможет людям серьёзней относится к клубу."
    m "Да, я тоже так подумала!"
    show monika zorder 1 at thide
    hide monika
    "Я пролистал страницы."
    "Поэма каждого члена клуба аккуратно напечатана на собственных страницах, что придаёт им почти профессиональный вид."
    "Я узнал поэмы Нацуки и Юри, которые они исполняли во время практики."
    mc "Что это?.."
    "Я открыл поэму Сайори."
    "Эта отличается от той, которую она практиковала."
    "Я не читал её раньше..."
    call showpoem (poem_s3, music=False) from _call_showpoem
    mc "Ах--"
    "Что это такое?.."
    "От прочтения этой поэмы у меня закрутило живот."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "Что-то не так?"
    mc "Ах, ничего..."
    "Эта поэма совершенно не похожа на всё, что писала Сайори."
    "Но более того..."
    mc "Я-я передумал!"
    mc "Я собираюсь привести Сайори, поэтому..."
    m "Ах--"
    m 1b "Ну, хорошо!"
    m "Постарайся не задерживаться, ладно?"
    scene bg corridor with wipeleft
    "Я быстро покинул классную комнату."
    m "Держи себя в руках~"
    "Моника сказала мне это вслед."
    "Я ускорил свой шаг."

    scene bg residential_day with wipeleft_scene
    "О чём я только думал?"
    "Ради Сайори, я должен был стараться сильнее."
    "Хотя бы дождаться её или помочь ей проснуться, это несложно."
    "Даже такой простой поступок, как пойти в школу вместе, уже сделает её счастливой."
    "К тому же..."
    "Вчера я сказал ей, что всё будет так, как было всегда."
    "Это всё, в чем она нуждалась, и я хотел дать ей это."

    scene bg house with wipeleft
    "Я добрался до дома Сайори и постучал в дверь."
    "Я не ждал ответа, поскольку на телефон она также не отвечала."
    "Как и вчера, я открыл дверь и вошёл сам."
    scene black with wipeleft
    mc "Сайори?"
    "Она и правда крепко спит..."
    "Я вздохнул."
    "Я не мог поверить, что в конечном итоге я делаю это."
    "Бужу её в её собственном доме..."
    if sayori_confess:
        "Это ведь что-то, что сделал бы парень, правда?"
    else:
        "Разве это не что-то, что скорее сделает её парень?"
    "В любом случае..."
    "Я просто чувствую, что поступаю правильно."

    "Стоя перед комнатой Сайори, я постучал в её дверь."
    mc "Сайори?"
    mc "Просыпайся, глупышка..."
    "Ответа нет."
    "Не хочу вот так врываться в её комнату..."
    "Это ведь практически вторжение в личную жизнь?"
    "Но она действительно не оставляет мне выбора."
    "Я медленно открыл дверь."
    mc "{cps=30}...Сайо--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("Sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("О боже... Я ведь ничего не сломала, да? Погоди секунду, я, наверное, могу это починить... Думаю...\nНо знаешь что? Будет намного проще, если я просто удалю её. Это из-за неё всё так сложно. Ахаха! Ну, понеслась.", False)
        except: pass
    pause 6.0


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "Какого чёрта?.."
    "{i}Какого чёрта??{/i}"
    "Это какой-то кошмар?"
    "Это... должно быть, он."
    "Это всё не взаправду."
    "Это не может быть реальным."
    "Сайори не сделала бы этого."
    "Всё было нормально всего несколько дней назад."
    "Поэтому я не могу поверить в то, что видят мои глаза!.."
    scene black with dissolve_cg
    "Я подавил рвотный позыв."
    "Только вчера..."
    "Я сказал Сайори, что буду рядом с ней."
    "Я сказал ей, что знаю, как будет лучше, и что всё будет хорошо."
    "Тогда почему?.."
    "Почему она сделала это?.."
    "Как я могу быть таким беспомощным?"
    "Что я сделал не так?"
    if sayori_confess:
        "Признался ей..."
        "Я не должен был признаваться ей в любви."
        "Это совсем не то, что нужно было Сайори."
        "Она даже сказала мне, насколько это больно, когда о ней заботятся другие."
        "Тогда зачем я признался ей и заставил её чувствовать себя ещё хуже?"
    else:
        "Отверг её признание..."
        "Должно быть, это и было тем, что столкнуло её с края."
        "Её мучительные крики всё ещё отдаются эхом в моих ушах."
        "Почему я сделал такое с ней, когда она больше всего нуждалась во мне?"
    "Почему я был таким эгоистом?"
    "Это моя вина--!"
    "Мои мысли копошились, продолжая показывая мне всё, что я мог сделать, чтобы предотвратить это."
    "Если бы я проводил больше времени с ней."
    "Ходил бы вместе с ней в школу."
    if sayori_confess:
        "И оставался бы её другом, как это было всегда..."
    else:
        "И дал бы ей то, чего она хотела в наших отношениях..."
    "...Тогда я бы предотвратил это."
    "Я знаю, что мог бы предотвратить это!"
    "К чёрту Литературный Клуб."
    "К чёрту фестиваль."
    "Я только что... потерял моего лучшего друга."
    "Кого-то, с кем я вырос."
    "Её больше нет и не будет."
    "Нет ничего, что я мог бы сделать, чтобы вернуть её."
    "Это не какая-то игра, где я могу начать всё заново и попробовать сделать что-то другое."
    "У меня был только один шанс, и я не был достаточно осторожен."
    "И теперь я буду нести эту вину до самой смерти."
    "Ничто в моей жизни не стоило больше, чем её..."
    "Но я всё равно не смог сделать то, чего она хотела."
    "И теперь..."
    "Я никогда не смогу вернуть её."
    "Никогда."
    "Никогда."
    "Никогда."
    "Никогда."
    "Никогда..."
    $ in_sayori_kill = False


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
