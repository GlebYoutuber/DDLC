label yuri_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    "Мне очень хочется поговорить с Юри побольше..."
    "Но, с другой стороны, мне неудобно отвлекать её от чтения."
    "Мой взгляд упал на обложку её книги."
    "Кажется, это та самая книга, которую она дала мне..."
    "Более того, она прочитала всего пару страниц."
    play music t6 fadeout 1.0
    show yuri 4a zorder 2 at t11
    y "Ах..."
    "Чёрт--"
    "Кажется, она заметила, что я на неё смотрю..."
    "Она бросает на меня ещё один взгляд, и наши глаза встречаются на долю секунды."
    y 4b "..."
    "И это заставляет её спрятать своё лицо ещё глубже в книгу."
    mc "Прости..."
    mc "Я просто задумался..."
    "Я говорю это, чувствуя, что ей неуютно."
    y oneeye "Ох..."
    y "Всё хорошо..."
    y 1a "Если бы я была сосредоточена, то всё равно бы ничего и не заметила."
    y "Я просто перечитываю книгу..."
    mc "Это та же книга, что ты дала мне?"
    y "Угу."
    y "Я хотела в ней кое-что перечитать."
    y 2q "Без какого-либо повода!.."
    mc "Как так вышло, что у тебя две копии одной и той же книги?"
    y "Эм..."
    y "Ну, когда я вчера зашла в книжный магазин--"
    y 3o "Ах, я не это имела в виду..."
    y "В смысле--"
    y 1w "Я... Так вышло, что я купила две."
    mc "А, понятно."
    "Юри явно что-то недоговаривает, но я решаю не обращать на это внимания."
    mc "Я обязательно начну читать эту книгу!"
    y 2u "Я рада это слышать..."
    y "Как только действия книги начнут набирать обороты, тебе будет тяжело от неё оторваться."
    y 2c "У неё очень атмосферная и цепляющая история."
    mc "Правда?.."
label yuri_exclusive2_1_ch22:
    mc "А о чём она?"
    y 1f "Ну..."
    y "Ммм..."
    "Я смотрю на обложку книги."
    "Книга называется \"Портрет Маркова\"."
    "У неё на обложке изображён символ зловеще выглядящего глаза."
    y 1a "Проще говоря, она про религиозную секту, которая была превращена в лабораторию по испытаниям на людях..."
    y "И у людей, которые туда попадали, есть черта, которая превращает их в машины для убийства, жаждующих крови."
    y 1m "Но всё становится ещё хуже, и они начинают селективно размножать людей, отрезая их конечности и прикрепляя их к--"
    y 1q "О-ох, это, наверное, уже был спойлер..."
    y 3q "В любом случае, м-мне это очень нравится!"
    y 3n "...То есть книга!"
    y 3q "Н-не часть про конечности..."
    mc "Это немного--!"
    "Это немного жутковато."
    "Звучало так, будто это должна быть хорошая история, но этот жуткий поворот событий появился из ниоткуда."
    y 1c "Ахаха."
    y "Разве ты не фанат таких историй, [player]?"
    mc "Не совсем..."
    mc "Хотя, мне может и понравиться такое, так что не беспокойся."
    y 2u "Я надеюсь..."
    "Да... я совсем забыл, что Юри любит такие вещи."
    "Она такая застенчивая и отчуждённая снаружи, но внутри она совершенно другая."
    y "Просто такие истории..."
    y 1a "Они позволяют взглянуть на жизнь с совершенно новой, необычной перспективы."
    $ style.say_dialogue = style.normal
    y "Когда ужасные вещи происходят не просто из-за того, что кто-то хочет быть злым..."
    $ style.say_dialogue = style.edited
    y "А потому, что мир полон ужасных людей, и мы все всё равно ничего не стоим."
    y "А потом, когда тыыыыыыыыыыыыыыыыыы ыыыыыыыыыыыыыыыы{nw}"
    $ style.say_dialogue = style.normal
    y 3v "Я... я заговорилась, да?"
    y "Только не снова..."
    y 4b "Прости..."
    mc "Эй, не нужно извиняться!.."
    mc "Я вовсе не потерял интерес."
    y "Тогда..."
    y "Я думаю, всё в порядке..."
    y 4a "Мне кажется, я должна тебе рассказать о своей проблеме..."
    $ style.say_dialogue = style.normal
    y "Когда я позволяю чему-то вроде книг и поэм заполнить мои мысли..."
    $ gtext = glitchtext(24)
    $ style.say_dialogue = style.edited
    y "Всё моё тело становится невероятно [gtext]{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    y "Я перестаю обращать внимание на других людей..."
    y 3t "Так что, я прошу прощения, если сказала что-то странное!"
    y "И, пожалуйста, останови меня, если я начну слишком много говорить!"
    mc "Это--"
    mc "Я уверен, что тебе не нужно об этом беспокоиться..."
    mc "Это просто значит, что у тебя страсть к чтению."
    mc "Всё, что я могу сделать -- это слушать."
    mc "Это ведь Литературный Клуб, в конце концов..."
    y 4a "Ах--"
    y "Ну..."
    y "Ты прав..."
    mc "К слову..."
    mc "Не пора бы мне начать читать твою книгу?"
    play sound "sfx/glitch3.ogg"
    y dragon "Д-да!"
    y 3n "Т-ты не должен, но!.."
    mc "Aхаха, о чём ты говоришь?"
    y 3o "..."
    mc "Сейчас, я её достану..."
    "Я быстро вынимаю книгу из своей сумки."
    mc "Отлично... не против, если я сяду здесь?"
    "Я сажусь на место рядом с Юри."
    y 3n "Ах!.."
    y "Ладно..."
    mc "Ты уверена?"
    mc "Ты словно опасаешься..."
    y "Это..."
    y 4b "Прости..."
    y "Не то чтобы я не хочу, чтобы ты сел рядом!"
    y "Просто я не привыкла к такому..."
    y "К чтению с кем-то в компании."
    mc "Понятно..."
    mc "Хорошо, просто дай мне знать, если я буду тебя отвлекать."
    y "Л-ладно..."
    show yuri zorder 1 at thide
    hide yuri
    "Я открываю книгу и начинаю читать пролог."
    "Вскоре я понимаю, что Юри имела в виду, когда говорила про совместное чтение."
    "Я постоянно чувствую, что она находится рядом."
    "Это не то чтобы плохо."
    "Может, немного отвлекает, но чувство довольно успокаивающее."
    "Я замечаю Юри краем глаза."
    "И понимаю, что она не смотрит в свою книгу."
    "Я поворачиваюсь."
    "Похоже, что она читает из моей книги--"
    show yuri 3n zorder 2 at t11
    y "П-прости!"
    $ style.say_dialogue = style.normal
    y "Я просто--!{nw}"
    $ style.say_dialogue = style.edited
    y "Я просто{fast} наслаждалась ощущением тепла твоего тела аааааааааааааатела елааааааааа{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    mc "Юри, ты так много извиняешься!"
    y "Я... Правда?"
    y 4a "Я не хотела..."
    y "Прости..."
    y 4c "Я хотела сказать--!"
    mc "Ахаха."
    mc "Вот, так лучше, правда?"
    "Я пододвигаю свой стол к её и стараюсь держать книгу между нами."
    y 2v "Ах..."
    y "Думаю, да..."
    "Юри закрывает свою копию книги."
    "Мы оба немного наклоняемся, и наши плечи теперь почти соприкасаются."
    "Кажется, что моя левая рука мешает, поэтому я беру книгу в правую."
    mc "Ах, похоже, что так будет сложно листать страницы..."
    y "Сейчас..."
    $ persistent.clear[2] = True
    scene y_cg1_base with dissolve_cg
    "Юри берёт левую сторону книги своей левой рукой и держит её между большим и указательным пальцами."
    mc "Ах..."
    "Я делаю то же самое своей правой рукой."
    "Таким образом, я переворачиваю страницу, и Юри кладёт её под свой большой палец."
    "Но, сидя в таком положении..."
    "Мы находимся ещё ближе друг к другу, чем раньше."
    "А ведь это, на самом деле, меня отвлекает!.."
    "Как будто я могу чувствовать тепло лица Юри, и она постоянно находится в поле моего зрения..."
    show y_cg1_exp1 at cgfade
    y "...Ты готов?"
    mc "А?"
    y "Перевернуть страницу..."
    mc "Ах... извини!"
    mc "Я на секунду отвлёкся..."
    "Я смотрю на лицо Юри, и наши взгляды встречаются."
    "Я не знаю, как я должен успевать за ней..."
    y "Ах..."
    show y_cg1_exp2 at cgfade
    y "Всё хорошо."
    y "Ты не привык читать?"
    y "Я могу подождать тебя..."
    y "Это меньшее, что я могу сделать..."
    y "Раз ты был со мной так терпелив..."
    mc "Д-да..."
    mc "Спасибо."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "Мы продолжаем читать."
    "Юри больше не спрашивает, готов ли я переворачивать страницу."
    "Вместо этого, я предполагаю, что она уже закончила читать страницу быстрее меня, и переворачиваю её."
    "Мы читаем первую главу в полной тишине."
    "Даже так, пролистывание страниц ощущается как нечто интимное..."
    "Мой палец нежно отпускает страницу, которая начинает порхать на другую сторону, и Юри ловит её своим пальцем.."
    mc "Эй, Юри..."
    mc "Это может показаться глупым, но..."
    mc "Главная героиня немного напоминает тебя."
    show y_cg1_exp3 at cgfade
    y "Ч-что??"
    y "Я-я совершенно на неё не похожа!"
    y "Абсолютно не похожа!"
    mc "Правда?.."
    mc "Она дважды думает перед тем, как что-то сказать или сделать..."
    show y_cg1_exp1 at cgfade
    y "А-ах..."
    y "Так ты про это..."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "Прости..."
    y "Я думала... что ты хотел сказать что-то другое."
    mc "Другое?.."
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "Н-не обращай внимания!"
    y "Мы даже ещё не дошли до этого момента..."
    y "Я не понимаю, как такие мысли могли придти ко мне в голову..."
    y "Ахаха!"
    mc "Юри, ты хорошо себя чувствуешь?"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "А--?"
    "Юри выглядит какой-то беспокойной с того момента, как мы начали читать..."
    mc "Ты можешь отдохнуть, если плохо себя чувствуешь."
    mc "Твоё дыхание немного..."
    y "Моё дыхание?.."
    hide y_cg1_exp1
    "Юри кладёт свои руки на грудь, чтобы почувствовать своё сердцебиение."
    y "Я-я этого... даже не заметила..."
    show y_cg1_exp3 at cgfade
    y "...Неважно, со мной всё нормально!"
    y "Мне просто нужно выпить воды!.."
    mc "Хорошо... не перетруждай себя."
    scene bg club_day
    with dissolve_cg
    "Юри встаёт и выбегает из класса."
    mc "Что это, чёрт возьми, было?.."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "Что сейчас произошло?"
    mc "А?"
    mc "Без понятия..."
    mc "Юри немного странно себя ведёт..."
    m 1r "Значит, ты не знаешь, почему..."
    mc "Извини, я не уверен."
    mc "Ты волнуешся за неё?"
    m 1a "Ох... не совсем."
    m "Я просто хотела удостовериться, что ты не сделал ей ничего плохого."
    mc "Н-нет, вообще ничего!"
    m 5 "Ахаха, не волнуйся... я тебе верю, глупый."
    m "С Юри такое иногда случается, ничего страшного."
    mc "Хорошо... как скажешь."
    m 2b "Ладно, почему бы нам не начать делиться своими поэмами?"
    mc "Эм?"
    mc "Не стоит ли нам дождаться Юри?"
    m 2a "Ну, она может задержаться, так что, думаю, стоит начать без неё."
    m "Ты не против?"
    mc "Я просто спросил..."
    "Я встаю."
    "Запомнив страницу, на которой мы остановились, я убираю книгу в сумку."
    $ y_ranaway = True
    return

label yuri_exclusive2_2:
    $ y_exclusivewatched = True
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    mc "Эй, Юри."
    show yuri 2f zorder 2 at t11
    y "А?"
    mc "Ах..."
    "Я замечаю, что Юри читает не ту книгу, что мы читали вместе."
    mc "Извини! Я не хотел отвлекать..."
    y 2m "Нет..."
    y "Я ждала тебя..."
    show yuri 2a
    mc "Тогда..."
    mc "Тогда, может, начнём?"
    y 2c "Да, давай!"
label yuri_exclusive2_2_ch22:
    y 3a "И ещё, у меня есть просьба..."
    y "...Не против, если я сделаю чаю?"
    mc "Совсем не против."
    y 1c "Спасибо большое."
    y 1a "Если и есть что-то, что помогает сделать моё время за чтением лучше, то это, определённо -- чашечка чая."
    y "Для тебя, разумеется, тоже."
    show yuri zorder 1 at thide
    hide yuri
    "Юри встаёт и подходит к шкафчику."
    "Я слежу за тем, как она достает небольшой кувшин для воды -- тот, что с фильтром внутри."
    show yuri 1f zorder 2 at t11
    y "Можешь подержать?"
    mc "Конечно..."
    "Юри даёт мне кувшин и достает электрический чайник."
    y "Я подключу его у стола учителя, ещё надо набрать немного воды."
    show yuri zorder 1 at thide
    hide yuri
    "Она проходит мимо меня и ставит чайник на стол учителя."
    "Я просто слежу за её движениями."
    "К моему удивлению, её движения контрастируют с её манерой говорить."
    "Особенно из-за её длинных ног, Юри выглядит элегантной и методичной."
    show yuri 1f zorder 2 at t11
    y "Хорошо, можно я возьму кувшин?"
    y 1a "Спасибо. Я сейчас вернусь."
    mc "Ах, давай я с тобой схожу..."
    y 1q "В-всё хорошо!"
    y "Оставайся здесь..."
    y "Я быстро."
    show yuri zorder 1 at thide
    hide yuri
    "С кувшином в руках, Юри торопливо выходит из класса."
    show monika 2i zorder 2 at t11
    m "Ах..."
    m "Юри опять сбежала?"
    mc "В этот раз всё по-другому."
    mc "Она просто набирает воду для чая."
    m 5 "Ах, хорошо!"
    m "Прости, что не так поняла~"

    scene bg club_day
    with wipeleft_scene

    "..."
    "Прошло десять минут."
    "Юри сказала, что это не займёт много времени."
    "Что-то она задерживается..."
    "Я заскучал и поэтому решил пойти поискать её."
    scene bg corridor
    with wipeleft_scene
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    mc "Так, посмотрим..."
    "Логично будет поискать Юри у ближайшего фонтанчика с водой..."
    $ y_name = "Юри"
    "Я продолжаю идти по корридору."
    $ y_name = "???"
    y "Хаах... хаах..."
    y "... Хаах... хаах..."
    "...Что это за звуки?"
    "Прямо за углом..."
    "Звучит как дыхание."
    y "Кхххххх--"
    "Долгий вздох, словно сквозь зубы."
    "Кому-то больно?.."
    "Я заглядываю за угол."
    mc "Юри?.."
    $ y_name = "Юри"
    show yuri cuts zorder 2 at t11
    y "Ах--!"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    play music t6r
    show yuri zorder 1 at thide
    hide yuri
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=*3}Юри?..{/cps}{nw}"
    "{cps=*3}Я заглядываю за угол.{/cps}{nw}"
    "{cps=*3}Кому-то больно?..{/cps}{nw}"
    "{cps=*3}Долгий вздох, словно сквозь зубы.{/cps}{nw}"
    y "{cps=*3}Кхххххх--{/cps}{nw}"
    "{cps=*3}Звучит как дыхание.{/cps}{nw}"
    "{cps=*3}Прямо за углом...{/cps}{nw}"
    "{cps=*3}...Что это за звуки?{/cps}{nw}"
    y "{cps=*3}... Хаах... хаах...{/cps}{nw}"
    y "{cps=*3}Хаах... хаах...{/cps}{nw}"
    $ y_name = "Юри"
    "{cps=*3}Я продолжаю идти по корридору.{/cps}{nw}"
    "{cps=*3}Логично будет поискать Юри у ближайшего фонтанчика с водой...{/cps}{nw}"
    mc "{cps=*3}Так, посмотрим...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=*3}Я заскучал и поэтому решил пойти поискать её.{/cps}{nw}"
    "{cps=*3}Что-то она задерживается...{/cps}{nw}"
    "{cps=*3}Юри сказала, что это не займет много времени...{/cps}{nw}"
    "{cps=*3}Прошло десять минут.{/cps}{nw}"
    "{cps=*3}...{/cps}{nw}"

    $ del _history_list[-37:]
    if poemwinner[0] == "yuri" and chapter == 3:
        jump yuri_exclusive2_2_ch23
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    play music t6r
    hide noise
    hide vignette
    show layer master
    show yuri 1a zorder 2 at t11
    y "Я вернулась."
    y "Спасибо, что подождал."
    y "[player], тебе нравится чай улун?"
    mc "А, да."
    mc "Любой пойдёт."
    y "Очень хорошо."
    "Юри выставляет на чайнике температуру в 90 градусов."
    y 1f "Теперь нужно взять заварочный чайник."
    mc "Ты что, завариваешь чай по всем правилам?"
    y 1u "Конечно..."
    y "Я должна сделать всё как нужно, когда завариваю чай для других."
    mc "Даже если я совсем не эксперт в чаях?.."
    y 2m "Ухуху."
    y 2a "В таком случае, ты будешь удивлён ещё сильнее."
    mc "Ах... ну посмотрим!"
    show yuri zorder 1 at thide
    hide yuri
    "Юри достаёт заварочный чайник и начинает отмерять количество чайных листьев."
    "К моему удивлению, она даже начинает напевать песенку."
    show yuri 1c zorder 2 at t11
    mc "У тебя, видимо, сейчас хорошее настроение..."
    y 1a "Правда?"
    y "Я хотела это показать..."
    y "И ты это заметил."
    y 2u "Я немного подумала..."
    y "И решила, что попробую выражать свои эмоции немного выразительнее."
    y "Оказалось, что это не так уж и сложно..."
    y 1c "Если делать это в твоей компании."
    show yuri 1a
    mc "Ах..."
    mc "Это замечательно, Юри!"
    mc "Только не напрягай себя слишком сильно."
    y 3u "Ты всегда заботишься обо мне, [player]..."
    y "Это очень приятно."
    mc "Ну..."
    "Юри не шутит..."
    "Я даже не уверен, смогу ли со всем этим справиться!.."
    "Я наблюдаю, как Юри наполняет наши чашки."
    y 1a "[player], у меня есть ещё одна просьба."
    y "Ты не против, если мы посидим сегодня на полу?"
    mc "Эм? С чего это вдруг?"
    y 1h "Нагрузка на мою спину будет меньше..."
    y "Я смогу читать, уперевшись о стену, вместо того, чтобы наклоняться над партой."
    mc "Ах, прости, я не сразу понял."
    y 1a "Не беспокойся."
    y "Просто моя спина частенько побаливает, так что я стараюсь это исправить."
    mc "Правда?"
    mc "Интересно, почему..."
    y 1f "Это, скорее всего, из-за моей--"
    y 1n "Ах--"
    y 1o "М-моей..."
    mc "Твоей осанки, да?"
    mc "Всегда сутулишься, когда читаешь..."
    y 2p "Да!"
    y 2q "У меня ужасная осанка, когда я читаю!"
    y "Поэтому мы должны сесть на пол."
    mc "Логично."
    mc "Я схожу за книгой."
    show yuri zorder 1 at thide
    hide yuri
    "Я достаю книгу из моей сумки."
    mc "Ах, у меня с собой есть немного шоколада..."
    "Это пакетик небольших шоколадных конфет."
    "Я взял их к чаю."
    "Мы с Юри садимся напротив стены, чашки с чаем по бокам."
    "Мы синхронно принимаем ту же позу для чтения, где каждый из нас держит половину книги."
    "Но в этот раз..."
    "Наши тела ещё ближе друг к другу."
    show yuri 2h zorder 2 at t11
    y "Я не очень хорошо вижу..."
    mc "--!"
    show yuri 2e at d11
    "Юри пододвигается ближе до тех пор, пока наши плечи не начинают соприкасаться."
    "Как я должен сосредоточиться на чтении?..!"
    "Юри всегда казалась мне немного милой, но..."
    "Сейчас она не такая замкнутая; ещё немного, и я не смогу сдерживаться!"
    y 2f "Твоя чашка..."
    "Юри подаёт мне мою чашку."
    "Держа её рукой, что не держит книгу, я оказываюсь в положении, в котором ещё сложнее сосредоточиться."
    "Теперь мне приходится следить за тем, чтобы случайно не дотронуться до её груди!.."
    "Тем временем, Юри даже ничего и не замечает."
    "По её серьёзному и увлечённому выражению лица я могу догадаться, что мир вокруг неё просто исчез."
    "Я использую всю свою силу воли, чтобы сосредоточиться на чтении."
    "..."
    "После нескольких минут, у меня получается немного расслабиться."
    "Я ставлю чашку между своих ног и начинаю возиться с упаковкой шоколадных конфет."
    mc "Ах, прости..."
    "Я медленно отпускаю книгу, чтобы закончить с упаковкой."
    mc "Можешь взять столько, сколько захочешь."
    y 2s "Ах, это..."
    y "Всё хорошо, я не буду брать..."
    mc "Эм? Ты уверена?"
    y 2v "Ну..."
    y "Если я возьму шоколад, то могу оставить пятна на страницах..."
    mc "Да, ты права..."
    mc "Я даже об этом не подумал."
    mc "Виноват..."
    y 2a "Не нужно извиняться."
    y "Я подержу книгу, хорошо?"
    mc "Ты уверена?.."
    y "Конечно."
    $ persistent.clear[3] = True
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "Юри берёт книгу в обе руки."
    "Она держит её так, чтобы мне было проще читать."
    "Но в итоге, её левая рука практически лежит на моей ноге."
    mc "Ну, в таком случае..."
    "Юри уже полностью сфокусировалась на чтении."
    "Я беру конфету и кладу её себе в рот."
    "После, я беру ещё одну..."
    "И даю её Юри."
    "Она даже не отрывает свой взгляд от книги."
    "Она просто открывает свой рот, словно такая ситуация совершенно естественна."
    "Это значит, что я не могу на этом остановиться!"
    hide y_cg2_nochoc
    "Я опасливо кладу конфету ей в рот."
    "И как ни в чём не бывало, Юри берёт её губами."
    y "Эм?.."
    show y_cg2_exp2
    "Выражение Юри внезапно меняется."
    y "Я..."
    y "Я сейчас..."
    "Юри смотрит на меня, словно желая удостовериться в том, что сейчас произошло."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "Э-эм..."
    y "[player]..."
    mc "П-прости!"
    mc "Думаю, мне не стоило так делать..."
    stop music
    y "А-Ах..."
    "Юри начинает глубоко дышать."
    y "Я..."
    y "Я не могу..."
    y "[player]..."
    "Внезапно, Юри вцепляется в мою руку и поднимает меня на ноги."
    "Моя чашка опрокидывается."
    scene bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "Моё сердце..."
    y 2y6 "Моё сердце не перестает биться, [player]..."
    y "Я не могу успокоиться."
    y "Я не могу ни о чем думать!.."
    y "Ты чувствуешь это, [player]?"
    "Юри внезапно прикладывает мою руку к своей груди."
    play music hb
    show layer master at heartbeat
    y 3t "Почему это со мной происходит?"
    y "Такое ощущение, словно я теряю рассудок..."
    y 3y4 "Я не могу это остановить."
    y 3y6 "Я даже не хочу больше читать..."
    y "Я просто..."
    y 3s "...хочу смотреть..."
    y "...на тебя."
    hide yuri
    show yuri eyes
    pause 3.0
    y "...Хаах..."
    pause 3.0
    y "...Хаах..."
    pause 3.0
    y "...Хаах..."
    pause 3.0
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    hide dark
    show monika 3l zorder 3 at f31
    with wipeleft
    m "Э-эм..."
    m "Настало время... поделиться поэмами..."




    return

label yuri_exclusive2_2_ch23:
    $ config.skipping = False
    scene black
    with None
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    play music t6g
    pause 4.62
    scene bg corridor
    show yuri eyes_base
    pause 1.0
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show yuri glitch at i11
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    play music g1
    y "[gtext]{nw}"
    stop music
    scene bg corridor
    show yuri 2n at i11
    y "Эм..."
    y "Подожди..."
    y 2o "Как я..."
    y 2y6 "...Прости, у меня просто было странное дежавю..."
    y "Этого всего не происходило раньше... Так ведь??"
    y 2t "В моей голове в последнее время полный беспорядок..."
    y 3t "Я надеюсь, что это не слишком заметно!"
    y "Мне будет очень неприятно, если ты подумаешь, что я странная, когда мы ещё и не успели начать общаться..."
    y "Я имею в виду..."
    show bg corridor:
        xoffset 0
        parallel:
            0.36
            xoffset 1
            repeat
        parallel:
            0.49
            xoffset 0
            repeat
    show black zorder 5:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat

    play music t9
    y "У каждого есть свои особенности."
    y 1v "Но {i}выражение{/i} этих особенностей вскоре после встречи с кем-то обычно выглядит плохо... или неприятно."
    y "По крайней мере, это то, что я заметила."
    y "Когда я была младше, я думала, что смогу показать себя с сильной стороны..."
    y "Но это заставляло людей отворачиваться, отказываться от моей компании."
    y 2w "Так что... Я начала ненавидеть эти особенности в себе."
    y "Моя страсть к некоторым увлечениям."
    y "И то, что я не могу себя контролировать, когда чем-то очень сильно увлечена."
    y "Так что..."
    y 1v "В итоге я перестала разговаривать с людьми."
    y "Если я никому не смогу понравится за то, что мне больше всего небезразлично..."
    y 1u "...Тогда мне проще будет отстраниться."
    y 1h "Но с недавних пор, что-то пошло не так."
    y "Я не знаю что."
    y 2y6 "Но каждый раз, когда мы приходим в клуб, моё сердце сходит с ума."
    y "Будто оно вот-вот вырвется из моей груди."
    y "Это переполняет меня энергией и эмоциями, которыя я не могу выпустить."
    y "Это заставляет меня делать странные вещи."
    y 2t "Я не знаю, почему это происходит!"
    stop music
    y 1t "[player]..."
    y "Со мной что-то не так, или Моника в последнее время странно себя ведёт??"
    y 1v "Она всегда была такой доброй, с самого моего вступления в клуб..."
    y "Но недавно я начала чувствовать какую-то острую атмосферу, когда она находится рядом."
    y 2y4 "Я ведь не сошла с ума?"
    y 2y1 "Пожалуйста, скажи, что нет!"
    y "Я не могла сказать что-то раньше, потому что она всегда слушает"
    y 2y3 "Но наконец, мы одни..."
    y "Мы можем остаться здесь ещё немного?"
    y 1m "Да..."
    y "..."
    play music hb
    show layer master at heartbeat
    show yuri as yuri_eyes zorder 4:
        "yuri/eyesfull.png"
        i11
        alpha 0.0
        block:
            2.012 * 4 - 1.49
            alpha 1.0
            0.52
            alpha 0.0
            1.49
            repeat
    pause 2.0
    $ ad = 40.0
    $ ac = 1.0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Я просто хочу остаться здесь."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "Только ты и я."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "Мы можем остаться здесь, пока не закончится встреча клуба."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "И потом в нашем распоряжении будет вся клубная комната."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Никто не сможет помешать нашему чтению."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Никто не заставит меня хотеть перерезать себе горло."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1q "Ахаха..."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Это была шутка!"
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Просто шутка."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1i "Хотя, мне нравятся ножи..."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "Это звучит странно, но ты никогда не поймёшь меня, если никогда не видел, насколько красивыми они могут быть."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1f "У меня есть идея."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Не хочешь как-нибудь зайти ко мне домой?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Я могу показать тебе свою коллекцию."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Я получила их от различных мастеров."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Я тщательно ухаживаю за каждым."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Я не хочу, чтобы они чувствовали себя одинокими..."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Никто не заслуживает одиночества."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Никто."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1c "И поэтому я так счастлива, что ты вступил в Литературный Клуб, [player]."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Теперь нам не нужно быть одинокими."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Потому что у нас есть мы."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Каждый день."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Это всё, что нам нужно."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "Знаешь, что?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Давай уйдём из Литературного Клуба."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Нам больше не нужно быть рядом с вездесущей Моникой."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "Не говоря уже об этом жалком ребёнке."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Мы можем ходить домой вместе после школы."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "И читать вместе."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "Вместе есть."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "Вместе спать."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "Разве это не идеально?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Это всё, что мы могли бы хотеть."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "Разве не из-за этого ты вступил в Литературный Клуб?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Словно это всё было предрешено судьбой."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "То, что мы сможем встретить друг друга."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "И теперь у нас будет счастливый конец, которого я терпеливо ждала все эти годы."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "Ты сделаешь это ради меня, [player]?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    $ gtext = glitchtext(200)
    y "Ты с{space=60}[gtext]{nw}"
    hide monika onlayer front
    window hide(None)
    $ poemsread = 0
    $ y_gave = False
    play music t5
    scene bg club_day
    window show(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
