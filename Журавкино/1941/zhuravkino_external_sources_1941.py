from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person,
                          wwii_record)

# WWII (ВОВ) участники — pamyat-naroda.ru, событие 1941 г. (призыв, пересыльные пункты).
# Тюжин Михаил Иванович (1907) — брат Евдокии Ивановны Тюжиной; его судьба — в 1942/.
zhuravkino_external_sources_1941 = external_source_records(
    "Журавкино",
    wwii_record(
        person("Михаил", "Иванович", "Тюшин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok14707754/",
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="1174 стрелковый полк",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 26),
        date=EventDate(1941, Month.JUNE, 26),
        archive="ЦАМО",
        fund="7833",
        inventory="254968с",
        case="3",
        comment=(
            "Место рождения по карточке: Мордовия, Зубово-Полянский р-н, с. Журавкино. "
            "Фамилия в списке — «Тюшин»; тот же Тюжин Михаил Иванович 1907 г. р. "
            "Скан на сайте не выложен (документ в ЦАМО)."
        ),
    ),
    wwii_record(
        person("Михаил", "Иванович", "Тюжин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_vpp19346631/",
        scan_file="scans/pamyat_179520-0001_00000008.jpg",
        birth_date=EventDate(1907),
        military_unit="пересыльный пункт Московского ГВК",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        date=EventDate(1941, Month.OCTOBER, 16),
        archive="ЦАМО",
        fund="СПП Московского ГВК",
        inventory="179520",
        case="1",
        comment=(
            "Строка 89: «Тюжин М. И., 1907, ВУС 116», призван Зубово-Полянским РВК; "
            "выбыл из пункта 16.10.1941."
        ),
    ),
    wwii_record(
        person("Михаил", "Иванович", "Тюжин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_vpp19117843/",
        scan_file="scans/pamyat_179520-0003_00000105.jpg",
        birth_date=EventDate(1907),
        rank="рядовой",
        military_unit="46 запасная стрелковая бригада",
        document_type=WwiiDocumentType.TRANSIT_POINT,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        date=EventDate(1941, Month.OCTOBER, 29),
        archive="ЦАМО",
        fund="СПП Московского ГВК",
        inventory="179520",
        case="3",
        comment=(
            "Строка 64: «Тюжин М. И., 1907, б/п, ВУС 116, рядовой», призван Зубово-Полянским РВК; "
            "29.10.1941 выбыл с пересыльного пункта Московского ГВК в 46 зсбр."
        ),
    ),
)
