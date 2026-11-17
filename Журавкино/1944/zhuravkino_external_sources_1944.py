from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1944 г.
# Катаев (в МК — Котаев) Михаил Иванович — сын Ивана Гаврииловича, брат Степана Ивановича
# Маркова; на памятнике «Катаев М. И.». В МК родился 17.05.1907, карточки пишут 1906.
zhuravkino_external_sources_1944 = external_source_records(
    "Журавкино",
    wwii_record(
        person("Михаил", "Иванович", "Катаев", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie60157333/",
        scan_file="scans/pamyat_058-0977520-0092_00000094.jpg",
        birth_date=EventDate(1906),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        casualty_date=EventDate(1944, Month.DECEMBER),
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JULY, 3),
        date=EventDate(1944, Month.DECEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="977520",
        case="92",
        comment=(
            "Строка 41: «Катаев Михаил Иванович, красноарм., стрелок, 1906, Мордовская АССР, "
            "Зубово-Полянский р-н, село Журавкино; призван 2.7.41; считать пропавшим без вести в "
            "декабре 1944 г.» (указатель сайта — 02.1945). Жена: Катаева Евгения Ивановна, "
            "с. Журавкино. В Книге памяти Мордовии — то же село."
        ),
    ),
)
