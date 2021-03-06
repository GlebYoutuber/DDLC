label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s") from _call_showpoem_14
    y 2q "Ахаха..."
    y "На самом деле не важно, о чём она."
    y "В последнее время мой мозг чрезмерно активен, поэтому я выплеснула это с помощью твоей ручки."
    y 2o "Ах--"
    y 2q "Эта... р-ручка упала из твоего портфеля вчера... И я решила взять её домой, для сохранности и..."
    y "Мне, эм..."
    y 2y6 "Мне просто... очень понравилось... то... как она пишет."
    y "Так что я написала эту... поэму... с её помощью."
    y "И теперь ты её трогаешь..."
    y 2y5 "Ахаха."
    y 3p "Я-я в порядке!!"
    y 3o "Что я только что..."
    y "..."
    y 4c "...Можешь притвориться, что этого разговора не было?"
    y "Хотя... можешь оставить поэму себе..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter) from _call_showpoem_15
    y "Тебе нравится?"
    y "Я написала её специально для тебя!!"
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "Если ты не понял, то эта поэма о [gtext]"
    y 1y6 "Гораздо важнее, что я одарила её своим запахом."
    y "Видишь, разве не я самая разумная в клубе?"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    pause 0.2
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "Меня..."
    y "Кажется, меня... сейчас стошнит."
    show yuri at lhide
    hide yuri
    pause 1.0
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2) from _call_showpoem_16
        n 2a "Неплохо, правда?"
        mc "А она на порядок длиннее вчерашней."
        n 2w "Вчерашняя была короткой, потому что..."
        n "Я просто разогревалась!"
        n 2c "Надеюсь, ты не подумал, что это мой максимум."
        mc "Нет, конечно нет!.."
        n 2a "В любом случае, она получилась очень незамысловатой."
        n "Сомневаюсь, что нужно объяснять."
        n 2g "Полагаю, все согласятся с тем, что автор - невежественный придурок."
        n "У каждого есть свои необычные увлечения или предосудительные удовольствия."
        n 5q "Что-то, что люди выставят на смех, если узнают об этом."
        n 1e "...Но это лишь покажет людей с их тупой стороны!"
        n "Никого не должно волновать, что у человека на уме, если ему это нравится, и это не мешает остальным."
        n 1q "Думаю, людям стоит учиться уважать любителей странных вещей."
        n 1x "...Прямо как двум девушкам из этого самого клуба, на которых я из уважения не покажу пальцем."
        n 1s "Это типа иронично, что в единственном месте, где я могу чувствовать себя комфортно, даже нет людей, уважающих меня..."
        n 1u "...Господи, из-за тебя я столько жалуюсь!.."
        "{i}(...Я-то что не так сделал?){/i}"
        mc "Но, по крайней мере, я уважаю тебя..."
        n 1h "Ну--"
        n "Спасибо, полагаю..."
        n 1s "...Но это типа заметно, что ты 'уважаешь' Юри больше, так что..."
        n 42c "Неважно... Мы уже поделились стихами друг с другом, так что можешь идти."
    return
label ch22_n_end2:
    call showpoem (poem_n2b, revert_music=False) from _call_showpoem_17
    $ style.say_dialogue = style.edited
    n 1g "[player]..."
    n "Почему ты сегодня не пришёл почитать со мной?"
    n 1m "Я ждала тебя."
    n "Я о-очень долго тебя ждала."
    n "Это было единственное, чего я ждала сегодня."
    n "Почему ты всё испортил?"
    n "Юри нравится тебе больше?"
    n 1k "Лучше тебе перестать водиться с ней."
    n "Ты меня вообще слушаешь?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "Юри больная на голову."
    n "Теперь это должно быть очевидно."
    n "Так поиграй со мной вместо неё."
    n "Ладно?"
    n "Ты же не ненавидишь меня, [player]?"
    n "Ты меня ненавидишь?"
    show natsuki_ghost_blood zorder 3
    n "Хочешь, чтобы я ушла домой в слезах?"
    n "Этот клуб - единственное место, где я могу чувствовать себя в безопасности."
    n "Не порть этого, ради меня."
    n "Просто не испорть этого."
    n "Прошу."
    n "Перестань общаться с Юри."
    n "Лучше поиграй со мной."
    n "Это всё, что у меня есть..."
    n "Поиграй со мной."
    stop music
    hide n_rects_ghost3
    n ghost2 "ПОИГРАЙ СО МНОЙ!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23, revert_music=False) from _call_showpoem_18
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "Я передумала."
    n "Забудь всё, что ты только что прочитал."
    n "Нет смысла что-либо делать."
    n "Юри сама виновата в том, что она такая неприятная."
    n "Ты меня слышишь, [player]?"
    n "Если ты просто станешь проводить больше времени вместе с Моникой, все эти проблемы уйдут."
    n "Ни Юри, ни я не подходим для такого замечательного человека, как ты."
    n "С этого момента думай только о Монике."
    n "Только о Монике."
    hide natsuki
    $ style.say_dialogue = style.edited
    "Только Моника."
    menu:
        "Только Моника."
        "Только Моника.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Только Моника.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Только Моника." with Dissolve(0.5, alpha=True)
    pause 1.0
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21) from _call_showpoem_19
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22, revert_music=False) from _call_showpoem_20
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    pause 2
    show screen tear(20, 0.3, 0.3, 0, 40)
    pause 0.5
    hide screen tear
    play music t5c
    m 5 "Прости, знаю, что это слегка абстрактно..."
    m "Я просто пыталась... эм..."
    m 1r "Ну, не важно."
    m "Нет смысла объяснять."
    m 1i "Итак..."
    m 3b "Вот тебе Писательский Совет Дня от Моники."
    m "Иногда тебе нужно будет принять сложное решение..."
    m "В таких случаях не забывай сохранять свою игру!"
    m 3k "Ведь никогда не знаешь, что... эм..."
    m 3i "...С кем я говорю?"
    m "Ты меня слышишь?"
    m 3g "Скажи, что слышишь."
    m "Хоть что-нибудь."
    $ renpy.call_screen("dialog", "Пожалуйста, помоги мне.", ok_action=Return())
    m 3k "...Это мой совет на сегодня!"
    m "Спасибо за внимание~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        pause 3.0
    else:
        show black zorder 1
        pause 2.0
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "Боже мой! Это смогло меня поразить!{fast}"
    window auto
    m "Эм..."
    m 1m "Ну, полагаю, я типа накосячила, пока, ну... 'писала' эту поэму."
    m "Я просто пыталась..."
    m 1i "...Неважно."
    m "Давай просто продолжим..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n 1r "..."
        n "Да. Всё точно так, как я и предполагала..."
        mc "?.."
        n 2w "[player], слушай."
        n "Я не настолько тупая."
        n 2h "Я знаю, как много времени ты проводишь с Юри..."
        n "Очевидно же, что ты больше пытаешь впечатлить её, чем улучшить свои писательские способности."
        n 2w "Говорю прямо - на это жалко смотреть."
        n 4h "Зачем ты вообще вступил в этот клуб, [player]?"
        n "Ну серьёзно..."
        n "Я думала, что новый член поможет сплотить всех."
        n 4s "А не отодвинуть нас друг от друга ещё дальше."
        n 1u "Это всё такая дурацкая деятельность..."
        n 12c "...Послушай, я сейчас не в лучшем расположении духа, чтобы разговаривать."
        n "Пожалуйста, уходи."
        $ skip_poem = True
        return
    else:


        n 1k "...Хм."
        n "Твоя прошлая понравилась мне больше."
        mc "Да? Серьёзно?"
        n 2c "Угу. Могу сказать, что ты подошёл посмелее к этой поэме."
        n "Но ты всё ещё недостаточно хорош для этого. Она кажется пустой."
        mc "Это правда, но я лишь пытался попробовать что-нибудь новое."
        mc "Всё ещё пытаюсь понять."
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "...Хм."
        n 2k "Ну, признаю, что эта куда лучше прошлой."
        n "Приятно видеть, как ты вкладываешь свои силы."
        mc "Это хорошо..."
        label ch22_n_med_shared:
            n 2c "Просто убедись в том, что ты берёшь от каждого из нас понемногу."
            n "По крайней мере, от Юри ты берёшь немного больше опыта."
            n 5q "Имею в виду, что знаю, как вы..."
            n "Проводите время вместе, или что там у вас..."
            n 1w "Но знаешь, мы с Моникой ничуть не хуже её!"
            n 1q "В т-творчестве, имею в виду!"
            n 1h "Поэтому тебе стоит учиться и учиться, иначе лучше не станешь!"
            n "Вот, кстати, что я написала..."
            n "Прослежу за тем, чтобы ты извлёк из моей поэмы хоть что-нибудь."
            return


    elif n_poemappeal[0] == 0:
        n "...Хм."
        n 2k "Ну, она не хуже, чем твоя предыдущая..."
        n "Но я и не могу сказать, что она лучше."
        mc "Фух..."
        n 2c "А? Что ты имел в виду под своим 'фух'?"
        mc "А... Ну, так как это не столь ужасно, засчитаем мою победу."
        mc "И теперь мне кажется, что ты самая критичная из всех."
        n 1p "Эй! С чего это ты--"
        n 1q "{i}(Погодите-ка, разве это был не комплимент?..){/i}"
        n 4y "А-ха-ха! Рада видеть, что хоть кто-то признаёт мой опыт!"
        n "Ну, тогда продолжай работать над собой, и, возможно, в один день ты станешь на мой уровень!"
        mc "Это... ну..."
        "Что-то подсказывает мне, что Нацуки не совсем поняла, что я имел в виду."
        jump ch22_n_med_shared
    else:


        n "...Хм."
        n 2c "Ну, она не ужасна."
        n "Но разочаровывает, если сравнивать её с предыдущей."
        n 2s "Опять же, если бы она была столь хорошей, как вчерашняя, я была бы раздосадована."
        mc "Ну, полагаю, я всего лишь попробовал что-то другое в этот раз."
        label ch22_n_med_shared2:
            n 2c "Хорошо. Ты всё ещё новичок в этом, так что я и не рассчитывала на то, что ты найдёшь свой стиль должным образом."
            n "Я имею в виду, что все в клубе пишут совершенно по-разному..."
            n "Возможно, ты получил частичку опыта от каждого из нас."
            n 2q "К примеру..."
            n 5q "Я заметила, как ты проводил время с Юри сегодня..."
            n "Не то чтобы мне было дело, с кем ты проводишь время."
            n 5w "Как-никак, я получила ценный урок - не ожидать от людей чего-либо."
            n 5s "Не то чтобы я ждала тебя, или типа того."
            n 5h "Но тебе хотя бы стоит глянуть на то, что я написала..."
            n "Ты, возможно, сможешь извлечь из неё что-нибудь для себя."
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "Я даже думать не буду о том, чтобы прочитать твою поэму-подлизку к Юри."
        n 5s "Но я всё ещё хочу, чтобы ты прочитал мою."
        n "На то есть причина."
        n 5x "Хотелось бы мне не делать этого..."
        n "Но, к сожалению, у меня нет выбора."
        n 5h "Просто... внимательно прочитай её, хорошо?"
        n "Потом можешь уходить."
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n 2c "...Хмех."
        n "Полагаю, в итоге, ты вообще ничему не научился."
        n "Если честно, я не знаю, зачем надеялась на тебя."
        label ch23_n_bad_shared:
            n 42c "Это всё влияние Юри..."
            n "Я даже не предполагала, что тебя так легко впечатлить."
            n "Сначала ты проводил с ней много времени в клубе..."
            n "Теперь копируешь её стиль письма..."
            n 1s "Как же это тупо."
            n "По крайней мере Монике нравится моё творчество..."
            n 1r "...Эх."
            n 1q "Ну ладно... Видимо, сейчас мне придётся показать тебе свою поэму."
            n "Как же не хочется этого делать."
            n "Но, к сожалению, у меня нет другого выбора."
            n 1h "Просто... внимательно прочитай её, хорошо?"
            n "Потом можешь уходить."
            return
    else:

        n "..."
        n 2r "Ну блин."
        n "Это серьёзный шаг назад."
        mc "Ась?"
        n 2c "Твои последние две были куда лучше этой."
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n 2k "...Эта ничего так."
        mc "Ничего?"
        n "Да, по крайней мере лучше вчерашней."
        label ch23_n_shared:
            n 2c "По-прежнему не могу сказать, насколько ты заморачиваешься с писательством, но у тебя действительно неплохо выходит."
            n 4r "Даже несмотря на то, что ты проводишь время с одной лишь Юри..."
            n 4h "Я всё ещё думаю, что было бы неплохо устроить нечто такое, где мог бы поучаствовать каждый из нас."
            n 4w "Так что продолжай усердно работать!"
            n "То есть..."
            n 1h "Понимаю, что я не вице-президент клуба, или типа того..."
            n "Но это не значит, что ты можешь меня подвести, ясно?"
            n 1q "Так что, хотя бы прочитай мою."
            n "Но если честно..."
            n 1h "Эта поэма... значит очень много для меня."
            n "Поэтому читай её внимательно, хорошо?"
            return
    else:
        n "..."
        n 2k "...А эта ничего такая."
        mc "Ничего?"
        n "Ну, да."
        n "Примерно на уровне вчерашней."
        jump ch23_n_shared

label ch23_n_ygave:
    n 1h "Что?"
    n "Ты отдал свою поэму Юри?"
    n 4x "Отвратительно!"
    n "Да что с вами двумя?"
    n 1s "Хмпф..."
    n "Всё равно не хотела её читать."
    n 1r "Просто немного раздражает, что ты даже не подумал показать её мне."
    n 1x "...Ух."
    n 1q "Ладно... полагаю, мне в любом случае придётся делиться своей."
    n "Как же не хочется этого делать."
    n "Но, к сожалению, у меня нет другого выбора."
    n 1h "Просто... внимательно прочитай её, хорошо?"
    n "Потом можешь уходить."
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "Я ждала этого..."
    y "Посмотрим, что ты написал сегодня."
    y 3m "..."
    "Юри улыбнулась и сделала глубокий вздох."
    y "Мне нравится просто держать её в руках."
    mc "?.."
    y 3p "А, в смысле--"
    y "Поэма вышла хорошо!"
    y 3o "Эм... здесь..."
    y 2q "...Ну, здесь всё ещё есть вещи, над которыми стоит поработать..."
    y "Но это уже не важно."
    y 2s "Мне кажется, что бы ты ни написал, это сокровище."
    y 2d "Ахаха..."
    y 2o "Неловко вышло..."
    y "Д-давай продолжим..."
    y 2t "Вот поэма, которую я написала."
    y "Она не должна обязательно понравиться тебе, или вроде того..."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y 2b "Я ждала этого..."
        y "Посмотрим, что ты написал на сегодня."
        y 2e "..."
        y "......"
        "Юри уставилась на поэму с удивлённым выражением лица."
        mc "Она тебе... нравится?"
        y "[player]..."
        y "...Как ты так быстро разобрался?"
        label ch22_y_good_shared:
            y 2v "Ещё только вчера я рассказывала тебе о техниках, которые стоит практиковать..."
            mc "Наверное в этом и есть причина..."
            mc "Ты доходчиво объясняешь."
            mc "Я действительно хотел представить это более образно."
            show yuri 4b zorder 2 at t11
            "Юри заметно сглотнула."
            "Даже её ладони начали потеть."
            y 4e "А-ах..."
            y "Я так счастлива..."
            y 3y5 "Так здорово чувствовать, что тебя ценят, [player]!"
            y "Всё, что ты пишешь - сокровище для меня."
            y 3m "Моё сердце бьётся сильнее, даже когда я просто держу листок в руках..."
            y 3q "Ахаха..."
            y "Хочу написать поэму об этом чувстве..."
            y 3y6 "Разве это плохо, [player]?"
            y "Я ведь не веду себя странно, правда?"
            y 3s "Т-теперь мне стало гораздо сложнее скрывать свои эмоции..."
            y 3m "Я, вроде, смущена."
            y 3y6 "Но прямо сейчас я очень хочу, чтобы ты прочитал мою поэму."
            y 3y5 "Ладно?"
            return
    else:

        y 2b "Я ждала этого..."
        y "Посмотрим, что ты написал сегодня."
        y 2e "..."
        y "......"
        "Юри уставилась на поэму с удивлённым выражением лица."
        mc "Она тебе... нравится?"
        y "[player]..."
        y 2t "Эта, пожалуй, даже лучше вчерашней..."
        y "...Как ты так быстро вник в суть?"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y 1d "Наконец-то..."
    y 3y5 "Ахаха..."
    show yuri 3m
    "Юри прижала мою поэму к своему лицу и сделала глубокий вдох."
    y 3y6 "Мне нравится."
    y "Мне всё в ней нравится."
    y 3y5 "[player], я хочу взять её к себе домой."
    y "Можно мне её оставить?"
    y "Пожалуйста?"
    mc "Конечно, я не против..."
    y 2y5 "Ахаха."
    y "Ты слишком мил со мной, [player]..."
    y "Никогда не встречала кого-либо столь милого."
    y 2y6 "Я могу умереть..."
    y 3y5 "Н-не на самом деле, но всё же--!"
    y "Я просто не знаю, как описать это."
    y "Это же нормально -- чувствовать нечто подобное?"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "Это ведь не плохо, да?"
    "Юри прижала мою поэму к своей груди."
    y 3m "Я хочу забрать её домой и хранить в своей комнате."
    y "Надеюсь, ты будешь радоваться, вспоминая, что поэма у меня."
    $ style.say_dialogue = style.normal
    y 3y5 "Я хорошо о ней позабочусь!"
    $ style.say_dialogue = style.edited
    y 3y6 "Я даже буду трогать себя, перечитывая её снова и снова."
    $ _history_list.pop()
    y "Я порежу себя бумагой, чтобы твои телесные жидкости, проникли в мой кровоток."
    $ _history_list.pop()
    y 3y1 "Ахахахаха."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "Ты тоже можешь оставить мою поэму себе."
    y "Впрочем, когда прочитаешь, ты сам захочешь оставить её."
    y 2y6 "Вот, держи. Не могу больше ждать."
    y 2y5 "Ну же! Читай!"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "Привет, [player]!"
    m "Хорошо проводишь время?"
    mc "А... угу."
    m 1k "Отлично! Рада слышать!"
    m 4a "Между прочим, так как ты новенький, и всё такое..."
    m "Если у тебя есть какие-либо предложения для клуба, вроде новых занятий, или вещей, которые мы можем делать лучше..."
    m 4b "Я всегда слушаю!"
    m "Не бойся поднимать такие вопросы, хорошо?"
    show monika 4a
    mc "Понятно... Я запомню."
    "Конечно же, я не собираюсь делать нечто подобное."
    "Мне гораздо приятнее просто следовать течению до тех пор, пока я не привыкну."
    m 1a "В любом случае..."
    m "Хочешь показать мне свою поэму?"
    mc "Это немного смущает, но, видимо, я должен."
    m 5a "Ахахаха!"
    m "Не волнуйся, [player]!"
    m "Ты ведь знаешь, все мы сегодня немного стесняемся."
    m "Но это тот барьер, который мы все вместе научимся преодолевать."
    mc "Да, пожалуй."
    "Я передал Монике свою поэму."
    m 2a "...Ммм!"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_15

    m 1a "В любом случае, хочешь теперь прочитать мою?"
    m 1e "Не бойся, я не совсем хороша в этом..."
    mc "Ты звучишь довольно уверенной в себе для человека, который заявляет, что не хорош."
    m 1j "Ну... Это потому что я должна казаться уверенной в себе."
    m 1b "Это означает, что я не всегда такая, ясно?"
    mc "Понятно..."
    mc "Ну, давай тогда прочту."
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "И снова здравствуй, [player]!"
        m "Как продвигается писательство?"
        mc "Хорошо, наверное..."
        m 2k "Ну, ладно."
        m 2b "Главное, чтобы не плохо!"
        m 2a "Я рада, что ты показываешь себя."
        m "Возможно, совсем скоро у тебя выйдет шедевр!"
        mc "Ахаха, я на это даже и не рассчитываю..."
        m 2a "Кто знает!"
        m "Хочешь поделиться тем, что ты написал сегодня?"
        mc "Конечно... держи."
        "Я передаю свою поэму Монике."
        m "..."
        m "...Ладненько!"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_16

    m 1a "Но в любом случае..."
    m "Хочешь теперь прочитать мою?"
    m "Мне понравилось то, как получилось, так что, надеюсь, тебе тоже~"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_17
    if y_appeal < 3:
        m 1a "В любом случае..."
        if y_gave:
            m 1m "Думаю, о твоей поэме беспокоиться больше не стоит..."
            m "Юри стоило бы быть учтивее, и дать тебе поделиться со всеми, прежде чем забирать домой."
            m 1r "...Ну, неважно."
            m "Если это делает её счастливее, я не против."
            m 1a "А насчёт меня..."
        m 1e "Я работала очень... очень усердно над этой поэмой, так что..."
        m "Надеюсь, что, эм, она не пропадёт даром."
        m 1r "Вот..."
        $ persistent.seen_colors_poem = True
    return



label m2_natsuki_1:
    m 2b "Мне понравилось, [player]!"
    mc "Серьёзно?.."
    m 2e "Она гораздо милее, чем я предполагала."
    m 2k "Ахахаха!"
    mc "О, Господи..."
    m 1b "Нет, нет!"
    m "Кажется, что нечто подобное могла написать Нацуки."
    m "И она тоже очень хороший писатель."
    m 5a "Так что прими это за комплимент!"
    mc "Ахаха..."
    mc "Если ты так считаешь."
    m "Агась!"
    m 3b "Если ты заинтересован в Нацуки, то всегда храни при себе закуску."
    m "Она прилипнет к тебе, как собачка."
    m 3k "Ахаха!"
    m 1a "Отец Нацуки не даёт ей карманных денег и даже не оставляет еду дома, поэтому она довольно часто в нервном состоянии..."
    m "Но иногда она просто теряет всю силу и вырубается."
    m "Как недавно произошло."
    m 2d "Это просто догадка, но мне кажется, что она такая маленькая из-за того, что её недоедание ведёт к проблемам с ростом..."
    m 2b "...Но, слушай, многим парням ведь нравятся маленькие девушки, ты знал?"
    m 5a "Прости... Пытаюсь показать всё с лучшей стороны!"

    return

label m2_yuri_1:
    m 1a "Отличная работа, [player]!"
    m "В моей голове проносилось 'ого', пока я читала это."
    m 1j "Получилось очень многозначительно!"
    m 1a "Не знаю, почему, но я не ожидала от тебя чего-то столь глубокого."
    m 3b "Полагаю, я недооценивала тебя!"
    mc "Мне весьма просто заставить других недооценивать меня."
    mc "Таким образом, это идёт в плюс, когда я прикладываю усилия."
    m 5a "Ахаха! Не очень-то честно!"
    m "Но, как видишь, работает."
    m 2a "Ты знал, что Юри нравится этот стиль письма?"
    m "Творения, наполненные образностью и символизмом."
    m 2d "Иногда мне кажется, что разум Юри полностью отстранён от реальности."
    m "Однако, я не выставляю это как нечто плохое."
    m 2a "Но иногда у меня появляется чувство, что она разочаровалась в людях."
    m "Она проводит столько времени внутри своей головы, что, кажется, там ей куда интересней..."
    m 2b "Но это объясняет, почему она становится счастливой, когда ты проявляешь к ней доброту."
    m "Не думаю, что она привыкла к такому."
    m 2j "Она, должно быть, очень устала от взаимодействий с социумом, так что не вини её за излишнюю строгость."
    m 2d "Как до этого..."
    m "Думаю, если её простимулировать, она прекратит тратить время впустую в одиночестве."
    "Дверь неожиданно распахнулась."
    m 2b "Юри!"
    show monika 2a
    show yuri 1s zorder 3 at f31
    y "Я вернулась..."
    y "Я ничего не пропустила?"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "Не совсем..."
    m "Ну, мы уже начали делиться поэмами друг с другом."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 2t "А?"
    y "Уже?"
    y 2v "П-простите, что опоздала..."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2j "Не стоит!"
    m 2a "У нас ещё много времени, так что я рада, что ты потратила столько времени, сколько было нужно."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 1s "Хорошо..."
    y "Спасибо, Моника."
    y "Полагаю, теперь я должна достать свою поэму."
    show yuri zorder 1 at thide
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player], думаю, ты только что увидел то, что не должен был видеть."
    m "Я не хотела рассказывать тебе это, но, видимо, у меня нет выбора."
    m 1r "Становится опасно для тебя проводить столько времени вместе с Юри."
    m 1i "Не знаю почему, но она становится легковозбудимой, будучи рядом с тобой..."
    m 3d "Что по сути своей не должно быть проблемой."
    m "Но когда Юри становится слишком возбуждённой, она находит место, где спрятаться, и начинает резать себя карманным ножом."
    m 2e "Это всё портит, так?"
    m "Она даже приносит каждый день разные ножи, будто у неё есть коллекция, или типа того..."
    m 2d "Имею в виду, это не потому, что она в депрессии, или вроде того!"
    m "Я думаю, она просто получает от этого какое-то удовольствие."
    m 2m "Знаешь, это может быть даже чем-то вроде сексуального возбуждения..."
    m 1i "Но причина в том, что ты это позволяешь ей."
    m 1d "Я не хочу сказать, что это твоя вина!"
    m 1a "Но, полагаю, поэтому мне и пришлось рассказать тебе всё..."
    m "Поэтому, я считаю, если ты будешь сохранять дистанцию, для неё это будет лучший вариант."
    m 5 "И раз уж мы об этом заговорили, не стесняйся проводить больше времени со мной..."
    m "Мягко говоря, у меня хотя бы всё в порядке с головой... и я понимаю, как надо относиться к членам клуба."
    return

label m2_yuri_3:
    stop music
    m 1i "И не говори, что я не предупреждала тебя, [player]."
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
