from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1942 г. (гибель, пропажа без вести).
# Все трое — на памятнике участникам ВОВ в Журавкине (фото из Telegram, сообщения 1411/1412).
zhuravkino_external_sources_1942 = external_source_records(
    "Журавкино",
    # Степан Иванович Марков (Котаев), 1904 — муж Евдокии Ивановны Тюжиной; на памятнике «Катаев С. И.».
    # Донесения пишут Шацкий р-н Рязанской обл. — адрес семьи в 1941 г.; родство решает жена.
    wwii_record(
        person("Степан", "Иванович", "Марков", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_donesenie51644486/",
        scan_file=[
            "scans/pamyat_058-0818883-0951_00000046.jpg",
            "scans/pamyat_058-0818883-0951_00000047.jpg",
        ],
        birth_date=EventDate(1904),
        rank="красноармеец",
        military_unit="324 стрелковая дивизия",
        casualty_reason="убит",
        place_of_casualty="д. Татаринцы, Сухиничский р-н, Смоленская обл. (ныне Калужская)",
        casualty_date=EventDate(1942, Month.JANUARY, 1),
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1942, Month.JANUARY, 1),
        archive="ЦАМО",
        fund="58",
        inventory="818883",
        case="951",
        comment=(
            "Строка 360 (лл. 46–47): «Рязанской обл., Шацкий район, Красн… с/с, 1904 г.»; "
            "«убит в бою 1.1.1942 у дер. Татаринцы Сухиничского р-на Смоленской обл.», похоронен "
            "в братской могиле в северо-восточной части фруктового сада колхоза «Ким» там же. "
            "Жена: Маркова Евдокия Ивановна, Рязанская обл., Шацкий район."
        ),
    ),
    wwii_record(
        person("Степан", "Иванович", "Марков", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_donesenie1163793193/",
        scan_file="scans/pamyat_1637-0000002-0006_00000015.jpg",
        birth_date=EventDate(1904),
        rank="красноармеец",
        military_unit="1093 стрелковый полк",
        casualty_reason="убит",
        place_of_casualty="д. Татаринцы, Сухиничский р-н, Смоленская обл. (ныне Калужская)",
        casualty_date=EventDate(1942, Month.JANUARY, 1),
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Шацкий РВК, Рязанская обл., Шацкий р-н",
        date=EventDate(1942, Month.JANUARY, 1),
        archive="ЦАМО",
        fund="1637",
        inventory="2",
        case="6",
        comment=(
            "Строка 23: «1904, Красноз…(?) с/с Шацкого р-на Ряз. обл.», призван Шацким РВК; "
            "жена Маркова Евдок. Иван., там же. Перезахоронен: Калужская обл., Сухиничский р-н, "
            "д. Татаринцы, братская могила; в Книгах памяти Калужской (т. 13) и Рязанской обл."
        ),
    ),
    # Тюжин Михаил Иванович, 1907 — брат Евдокии Ивановны Тюжиной; на памятнике «Тюжин М. И.».
    wwii_record(
        person("Михаил", "Иванович", "Тюжин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie8139041/",
        scan_file=[
            "scans/pamyat_058-0018004-1186_00000429.jpg",
            "scans/pamyat_058-0018004-1186_00000430.jpg",
        ],
        birth_date=EventDate(1907),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        casualty_date=EventDate(1942, Month.MARCH),
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 25),
        date=EventDate(1942, Month.MARCH),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="1186",
        comment=(
            "Анкета розыска: «Морд. АССР, З.-Полянский р-н, с. Журавкино», стрелок; письма "
            "прекратились в 1942 г. Разыскивает жена — Тюжина Варвара Никитовна, с. Журавкино; "
            "заключение военкома от 29.04.1946 — судьбу установить нельзя, штамп «пропал без вести»."
        ),
    ),
    # Тюжин Леонтий Епифанович, 1895 — брат Ивана Епифановича; на памятнике «Тюжин Л. Е.».
    # Донесение пишет «Леонид»; жених 1914 г. (18 л. 6 мес.) и карточка ПМВ 1916 — он же.
    wwii_record(
        person("Леонид", "Епифанович", "Тюжин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_donesenie51780135/",
        scan_file="scans/pamyat_058-0818883-0978_00000142.jpg",
        birth_date=EventDate(1895),
        rank="красноармеец",
        military_unit="372 стрелковая дивизия",
        casualty_reason="убит",
        place_of_casualty="500 м юго-западнее д. Гайтолово, Мгинский р-н, Ленинградская обл.",
        casualty_date=EventDate(1942, Month.SEPTEMBER, 29),
        document_type=WwiiDocumentType.CASUALTY_REPORT,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        date=EventDate(1942, Month.SEPTEMBER, 29),
        archive="ЦАМО",
        fund="58",
        inventory="818883",
        case="978",
        comment=(
            "Строка 104: «МАССР, Зубово-Полянский р-н, с. Журавлино, 1895 г.» (так в машинописи). "
            "Жена: Тюжина Надежда Дмитриевна, с. Журавлино. В 1914 г. он венчался с Дарьей "
            "Гавриловной Сямакиной — Надежда, видимо, вторая жена. Перезахоронен: Ленинградская "
            "обл., Кировский р-н, п. Синявино-1, Синявинские высоты."
        ),
    ),
)
