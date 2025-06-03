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
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
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
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
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
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
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
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
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
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
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
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
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

es_mx = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Herramientas", callback_data="tools"),
            InlineKeyboardButton("Información", callback_data="description")
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
            InlineKeyboardButton("Atrás", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("¿Quieres generar otra vez?", callback_data="re_gen"),
            InlineKeyboardButton("Canal del Bot", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Canal del Bot", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Descripción", callback_data="informacion"),
            InlineKeyboardButton("Idiomas", callback_data="lenguaje"),
            InlineKeyboardButton("Atrás", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
        ],
        [
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Auth", callback_data="Auth"),
            InlineKeyboardButton("Charge", callback_data="Charge"),
            InlineKeyboardButton("CCN Gates", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("Chequeo Masivo", callback_data="Mass_Check"),
            InlineKeyboardButton("Atrás", callback_data="home")
        ]
    ]),
}

in_ = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("गेटवे", callback_data="gateways"),
            InlineKeyboardButton("टूल्स", callback_data="tools"),
            InlineKeyboardButton("जानकारी", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("बंद करें", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("होम", callback_data="home"),
            InlineKeyboardButton("अगला", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("पीछे", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("भाषाएँ", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("पीछे", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("क्या आप फिर से जनरेट करना चाहते हैं?", callback_data="re_gen"),
            InlineKeyboardButton("बॉट चैनल", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("बॉट चैनल", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("विवरण", callback_data="informacion"),
            InlineKeyboardButton("भाषाएँ", callback_data="lenguaje"),
            InlineKeyboardButton("पीछे", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
    [
        InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
        InlineKeyboardButton("ES MX [🇲🇽]", callback_data="es_mx"),
        InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
        InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
    ],
    [
        InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
        InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
        InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
    ],
    [
        InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
        InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
        InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("प्रमाणीकरण", callback_data="Auth"),
            InlineKeyboardButton("चार्ज", callback_data="Charge"),
            InlineKeyboardButton("CCN गेट्स", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("द्रव्यमान जांच", callback_data="Mass_Check"),
            InlineKeyboardButton("पीछे", callback_data="home")
        ]
    ]),
}

fr = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Passerelles", callback_data="gateways"),
            InlineKeyboardButton("Outils", callback_data="tools"),
            InlineKeyboardButton("Information", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Fermer", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Accueil", callback_data="home"),
            InlineKeyboardButton("Suivant", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Retour", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Langues", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Retour", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Voulez-vous générer à nouveau?", callback_data="re_gen"),
            InlineKeyboardButton("Chaîne du bot", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Chaîne du bot", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Description", callback_data="informacion"),
            InlineKeyboardButton("Langues", callback_data="lenguaje"),
            InlineKeyboardButton("Retour", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Auth", callback_data="Auth"),
            InlineKeyboardButton("Charge", callback_data="Charge"),
            InlineKeyboardButton("Portes CCN", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("Vérification de masse", callback_data="Mass_Check"),
            InlineKeyboardButton("Retour", callback_data="home")
        ]
    ]),
}

de = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateways", callback_data="gateways"),
            InlineKeyboardButton("Werkzeuge", callback_data="tools"),
            InlineKeyboardButton("Informationen", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Schließen", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Startseite", callback_data="home"),
            InlineKeyboardButton("Weiter", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Zurück", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Sprachen", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Zurück", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Möchten Sie erneut generieren?", callback_data="re_gen"),
            InlineKeyboardButton("Bot-Kanal", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Bot-Kanal", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Beschreibung", callback_data="informacion"),
            InlineKeyboardButton("Sprachen", callback_data="lenguaje"),
            InlineKeyboardButton("Zurück", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Auth", callback_data="Auth"),
            InlineKeyboardButton("Gebühr", callback_data="Charge"),
            InlineKeyboardButton("CCN-Tore", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("Massentest", callback_data="Mass_Check"),
            InlineKeyboardButton("Zurück", callback_data="home")
        ]
    ]),
}

it = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gateway", callback_data="gateways"),
            InlineKeyboardButton("Strumenti", callback_data="tools"),
            InlineKeyboardButton("Informazioni", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Chiudi", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Home", callback_data="home"),
            InlineKeyboardButton("Avanti", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Indietro", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Lingue", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Indietro", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Vuoi generare di nuovo?", callback_data="re_gen"),
            InlineKeyboardButton("Canale Bot", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Canale Bot", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Descrizione", callback_data="informacion"),
            InlineKeyboardButton("Lingue", callback_data="lenguaje"),
            InlineKeyboardButton("Indietro", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Auth", callback_data="Auth"),
            InlineKeyboardButton("Carica", callback_data="Charge"),
            InlineKeyboardButton("Cancelli CCN", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("Controllo di massa", callback_data="Mass_Check"),
            InlineKeyboardButton("Indietro", callback_data="home")
        ]
    ]),
}

ar = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("البوابات", callback_data="gateways"),
            InlineKeyboardButton("الأدوات", callback_data="tools"),
            InlineKeyboardButton("معلومات", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("إغلاق", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("الرئيسية", callback_data="home"),
            InlineKeyboardButton("التالي", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("عودة", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("اللغات", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("عودة", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("هل تريد التوليد مرة أخرى؟", callback_data="re_gen"),
            InlineKeyboardButton("قناة البوت", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("قناة البوت", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("الوصف", callback_data="informacion"),
            InlineKeyboardButton("اللغات", callback_data="lenguaje"),
            InlineKeyboardButton("عودة", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("المصادقة", callback_data="Auth"),
            InlineKeyboardButton("الشحن", callback_data="Charge"),
            InlineKeyboardButton("بوابات CCN", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("الفحص الجماعي", callback_data="Mass_Check"),
            InlineKeyboardButton("عودة", callback_data="home")
        ]
    ]),
}

ja = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ゲートウェイ", callback_data="gateways"),
            InlineKeyboardButton("ツール", callback_data="tools"),
            InlineKeyboardButton("情報", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("閉じる", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ホーム", callback_data="home"),
            InlineKeyboardButton("次へ", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("戻る", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("言語", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("戻る", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("再生成しますか？", callback_data="re_gen"),
            InlineKeyboardButton("ボットチャンネル", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("ボットチャンネル", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("説明", callback_data="informacion"),
            InlineKeyboardButton("言語", callback_data="lenguaje"),
            InlineKeyboardButton("戻る", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("認証", callback_data="Auth"),
            InlineKeyboardButton("チャージ", callback_data="Charge"),
            InlineKeyboardButton("CCNゲート", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("大量チェック", callback_data="Mass_Check"),
            InlineKeyboardButton("戻る", callback_data="home")
        ]
    ]),
}

tr = {
    'mainstart': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Geçitler", callback_data="gateways"),
            InlineKeyboardButton("Araçlar", callback_data="tools"),
            InlineKeyboardButton("Bilgi", callback_data="description")
        ],
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="ryas_cloud"),
            InlineKeyboardButton("Kapat", callback_data="close")
        ]
    ]),
    'atras': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Ana Sayfa", callback_data="home"),
            InlineKeyboardButton("Sonraki", callback_data="next")
        ]
    ]),
    'back': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Geri", callback_data="home")
        ]
    ]),
    'back_lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Diller", callback_data="lenguaje"),
        ]
    ]),
    'backvR': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Geri", callback_data="home")
        ]
    ]),
    're_genbt': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Tekrar oluşturmak ister misiniz?", callback_data="re_gen"),
            InlineKeyboardButton("Bot Kanalı", url="t.me/Astrozdev")
        ]
    ]),
    'gen_but': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
            InlineKeyboardButton("Bot Kanalı", url="t.me/Astrozdev")
        ]
    ]),
    'vryasx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Açıklama", callback_data="informacion"),
            InlineKeyboardButton("Diller", callback_data="lenguaje"),
            InlineKeyboardButton("Geri", callback_data="home")
        ]
    ]),
    'lang': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("EN [🇺🇸]", callback_data="en"),
            InlineKeyboardButton("ES [🇪🇸]", callback_data="es"),
            InlineKeyboardButton("PT [🇧🇷]", callback_data="pt"),
            InlineKeyboardButton("RU [🇷🇺]", callback_data="ru"),
        ],
        [
            InlineKeyboardButton("CH [🇨🇳]", callback_data="zh"),
            InlineKeyboardButton("KO [🇰🇷]", callback_data="ko"),
            InlineKeyboardButton("MX [🇲🇽]", callback_data="es_mx"),
            InlineKeyboardButton("FR [🇫🇷]", callback_data="fr"),
        ],
        [
            InlineKeyboardButton("DE [🇩🇪]", callback_data="de"),
            InlineKeyboardButton("IT [🇮🇹]", callback_data="it"),
            InlineKeyboardButton("AR [🇸🇦]", callback_data="ar"),
            InlineKeyboardButton("JA [🇯🇵]", callback_data="ja"),
        ],
        [
            InlineKeyboardButton("TR [🇹🇷]", callback_data="tr"),
            InlineKeyboardButton("xCloud [☁️]", callback_data="homevR"),
        ]
    ]
),
    'gatewaysx': InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Yetkilendirme", callback_data="Auth"),
            InlineKeyboardButton("Ücretlendirme", callback_data="Charge"),
            InlineKeyboardButton("CCN Kapıları", callback_data="CCN"),
        ],
        [
            InlineKeyboardButton("Toplu Kontrol", callback_data="Mass_Check"),
            InlineKeyboardButton("Geri", callback_data="home")
        ]
    ]),
}
