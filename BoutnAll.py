from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

en = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Tools", callback_data="tools"),
            InlineKeyboardButton("Information", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Close", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Home", callback_data="home"),
            InlineKeyboardButton("Next", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Back", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Languages", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Back", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Do you want to generate again?", callback_data="re_gen"),
            InlineKeyboardButton("Bot Channel", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Bot Channel", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Description", callback_data="informacion"),
                InlineKeyboardButton("Languages", callback_data="lenguaje"),
                InlineKeyboardButton("Back", callback_data="home")
            ]
        ]
    ),
    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("English [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("Español [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Auth", callback_data="Auth"),
                InlineKeyboardButton("Charge", callback_data="Charge"),
                InlineKeyboardButton("CCN Gates", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("Mass Checking", callback_data="Mass_Check"),
                InlineKeyboardButton("Back", callback_data="home")
            ]
        ]
    ),
}

es = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Herramientas", callback_data="tools"),
            InlineKeyboardButton("Informacion", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Cerrar", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Inicio", callback_data="home"),
            InlineKeyboardButton("Siguiente", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Atrás", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Idiomas", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Atras", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("¿Quieres generar de nuevo?", callback_data="re_gen"),
            InlineKeyboardButton("Bot Canal", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Bot Canal", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Descripcion", callback_data="informacion"),
                InlineKeyboardButton("Idioma", callback_data="lenguaje"),
                InlineKeyboardButton("Atras", callback_data="home")
            ]
        ]
    ),
    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("English [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("Español [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Auth", callback_data="Auth"),
                InlineKeyboardButton("Charge", callback_data="Charge"),
                InlineKeyboardButton("CCN Gates", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("Mass Checking", callback_data="Mass_Check"),
                InlineKeyboardButton("Atrás", callback_data="home")
            ]
        ]
    ),
}

pt = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Portais", callback_data="gateways"),
            InlineKeyboardButton("Ferramentas", callback_data="tools"),
            InlineKeyboardButton("Informação", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Fechar", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Início", callback_data="home"),
            InlineKeyboardButton("Próximo", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Voltar", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Idiomas", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Voltar", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Quer gerar novamente?", callback_data="re_gen"),
            InlineKeyboardButton("Canal do Bot", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Canal do Bot", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Descrição", callback_data="informacion"),
                InlineKeyboardButton("Idiomas", callback_data="lenguaje"),
                InlineKeyboardButton("Voltar", callback_data="home")
            ]
        ]
    ),
    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Inglês [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("Espanhol [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Autenticação", callback_data="Auth"),
                InlineKeyboardButton("Cobrar", callback_data="Charge"),
                InlineKeyboardButton("Portões CCN", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("Verificação em Massa", callback_data="Mass_Check"),
                InlineKeyboardButton("Voltar", callback_data="home")
            ]
        ]
    ),
}

ru = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Шлюзы", callback_data="gateways"),
            InlineKeyboardButton("Инструменты", callback_data="tools"),
            InlineKeyboardButton("Информация", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Закрыть", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Домой", callback_data="home"),
            InlineKeyboardButton("Следующий", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Назад", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Языки", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Назад", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Хотите сгенерировать снова?", callback_data="re_gen"),
            InlineKeyboardButton("Канал бота", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Канал бота", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Описание", callback_data="informacion"),
                InlineKeyboardButton("Языки", callback_data="lenguaje"),
                InlineKeyboardButton("Назад", callback_data="home")
            ]
        ]
    ),
    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Английский [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("Испанский [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("Авторизация", callback_data="Auth"),
                InlineKeyboardButton("Оплата", callback_data="Charge"),
                InlineKeyboardButton("CCN Ворота", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("Массовая проверка", callback_data="Mass_Check"),
                InlineKeyboardButton("Назад", callback_data="home")
            ]
        ]
    ),
}

zh = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("网关", callback_data="gateways"),
            InlineKeyboardButton("工具", callback_data="tools"),
            InlineKeyboardButton("信息", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("关闭", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("主页", callback_data="home"),
            InlineKeyboardButton("下一个", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("返回", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("语言", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("返回", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("是否重新生成？", callback_data="re_gen"),
            InlineKeyboardButton("机器人频道", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("机器人频道", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("描述", callback_data="informacion"),
                InlineKeyboardButton("语言", callback_data="lenguaje"),
                InlineKeyboardButton("返回", callback_data="home")
            ]
        ]
    ),
    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("英语 [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("西班牙语 [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("认证", callback_data="Auth"),
                InlineKeyboardButton("收费", callback_data="Charge"),
                InlineKeyboardButton("CCN 门", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("批量检查", callback_data="Mass_Check"),
                InlineKeyboardButton("返回", callback_data="home")
            ]
        ]
    ),
}

ko = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("게이트웨이", callback_data="gateways"),
            InlineKeyboardButton("도구", callback_data="tools"),
            InlineKeyboardButton("정보", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("닫기", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("홈", callback_data="home"),
            InlineKeyboardButton("다음", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("뒤로", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("언어", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("뒤로", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("다시 생성 하시겠습니까?", callback_data="re_gen"),
            InlineKeyboardButton("봇 채널", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("봇 채널", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("설명", callback_data="informacion"),
                InlineKeyboardButton("언어", callback_data="lenguaje"),
                InlineKeyboardButton("뒤로", callback_data="home")
            ]
        ]
    ),
    'lang': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("영어 [🇺🇸]", callback_data="en"),
                InlineKeyboardButton("스페인어 [🇪🇸]", callback_data="es"),
                InlineKeyboardButton("xCloud [☁️]", callback_data="homevR")
            ]
        ]
    ),
    'gatewaysx': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton("인증", callback_data="Auth"),
                InlineKeyboardButton("충전", callback_data="Charge"),
                InlineKeyboardButton("CCN 게이트", callback_data="CCN"),
            ],
            [
                InlineKeyboardButton("대량 검사", callback_data="Mass_Check"),
                InlineKeyboardButton("뒤로", callback_data="home")
            ]
        ]
    ),
}
