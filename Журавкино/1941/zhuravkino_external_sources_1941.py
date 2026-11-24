from verso.ru.dsl import (EventDate, Month, WwiiDocumentType, external_source_records, person, wwii_record)

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
    # ВОВ — pamyat-naroda.ru, добавлено 18.11.2026: люди, найденные в корпусе (реестр —
    # EXTERNAL_SOURCES.md и external_sources/vov_pamyat.tsv).
    wwii_record(
        person("Алексей", "Осипович", "Бармин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok11280298/",
        reviewed=False,
        birth_date=EventDate(1908),
        rank="ст. лейтенант",
        military_unit="447 осапб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.DECEMBER),
        date=EventDate(1941, Month.DECEMBER),
        archive="ЦАМО",
        fund="33060",
        inventory="185137",
        case="5",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Журавкино. Корпус: рождение 14.03.1908 (МК 1908 № 38), отец Бармин Иосиф Захарович, мать "
            "Бармина Фекла Захаровна."
        ),
    ),
    wwii_record(
        person("Алексей", "Осипович", "Бармин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok11280299/",
        reviewed=False,
        birth_date=EventDate(1908),
        rank="ст. лейтенант",
        military_unit="447 осапб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.DECEMBER),
        date=EventDate(1941, Month.DECEMBER),
        archive="ЦАМО",
        fund="33060",
        inventory="185137",
        case="5",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Журавкино. Корпус: рождение 14.03.1908 (МК 1908 № 38), отец Бармин Иосиф Захарович, мать "
            "Бармина Фекла Захаровна."
        ),
    ),
    wwii_record(
        person("Алексей", "Осипович", "Бармин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/kld-card_uchet_officer121738/",
        reviewed=False,
        birth_date=EventDate(1908, Month.MARCH, 14),
        rank="ст. лейтенант",
        military_unit="штаб МВО; 129 опмб; 447 отд. сан. б-н ЛенФ; ВК",
        document_type=WwiiDocumentType.SERVICE_CARD,
        date=EventDate(1941, Month.OCTOBER, 23),
        comment=(
            "Дата — поступления на службу. Окончание службы 19.09.1946. Награда на карточке: Медаль «За "
            "оборону Ленинграда»; Медаль «За победу над Германией в Великой Отечественной войне 1941–1945 "
            "гг.». Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. Журавкино. "
            "Корпус: рождение 14.03.1908 (МК 1908 № 38), отец Бармин Иосиф Захарович, мать Бармина Фекла "
            "Захаровна."
        ),
    ),
    wwii_record(
        person("Михаил", "Сергеевич", "Блохин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342309/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000408.jpg",
        birth_date=EventDate(1908),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_date=EventDate(1941, Month.JUNE, 28),
        date=EventDate(1941, Month.SEPTEMBER),
        casualty_date=EventDate(1941, Month.SEPTEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список военнослужащих рядового и сержантского состава, семьи которых потеряли с "
            "ними связь в период ВОВ, по Зубово-Полянскому РВК МАССР (приложение к вх. № 91495с(?)), "
            "строка № 13): Кр-ц, стрелок, 1908 г.р., МАССР Зубово-Полянского р-на с. Авдалово; призван "
            "?-ским РВК Моск. области (название не читается, «Ш…чинским»?) ?6.6.41г.; можно считать "
            "пропавшим без вести в сентябре 1941 г. (на поле «9/41», «проп. б/в»). Родные: жена Блохина "
            "Праск. Павловна, МАССР Зубово-Полянск. р-на с. Авдалово. Место рождения на карточке: "
            "Мордовская АССР, Зубово-Полянский р-н, с. Авдалово. Корпус: рождение 05.09.1908 (МК 1908 № "
            "98), отец Блохин Сергей Иванович, мать Блохина Евдокия Никитична."
        ),
    ),
    wwii_record(
        person("Федор", "Петрович", "Блохин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok10137847/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="106 омотоиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269842",
        case="1",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 21.02.1907 (МК 1907 № 31), отец Блохин Петр Васильевич, мать "
            "Блохина Ирина Степановна."
        ),
    ),
    wwii_record(
        person("Федор", "Петрович", "Блохин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok2298369/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="рядовой",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269839",
        case="1",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, д. "
            "Авдалово. Корпус: рождение 21.02.1907 (МК 1907 № 31), отец Блохин Петр Васильевич, мать "
            "Блохина Ирина Степановна."
        ),
    ),
    wwii_record(
        person("Федор", "Петрович", "Блохин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok3473768/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269840",
        case="2",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, д. "
            "Авдалово. Корпус: рождение 21.02.1907 (МК 1907 № 31), отец Блохин Петр Васильевич, мать "
            "Блохина Ирина Степановна."
        ),
    ),
    wwii_record(
        person("Федор", "Петрович", "Блохин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok6507991/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269841",
        case="1",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, д. "
            "Авдалова. Корпус: рождение 21.02.1907 (МК 1907 № 31), отец Блохин Петр Васильевич, мать "
            "Блохина Ирина Степановна."
        ),
    ),
    wwii_record(
        person("Федор", "Петрович", "Блохин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok7973350/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269841",
        case="2",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, д. "
            "Авдалово. Корпус: рождение 21.02.1907 (МК 1907 № 31), отец Блохин Петр Васильевич, мать "
            "Блохина Ирина Степановна."
        ),
    ),
    wwii_record(
        person("Егор", "Васильевич", "Букин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok3690049/",
        reviewed=False,
        birth_date=EventDate(1908),
        rank="красноармеец",
        military_unit="1170 сп 348 сд",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 26),
        date=EventDate(1941, Month.JUNE, 26),
        archive="ЦАМО",
        fund="7829",
        inventory="254942с",
        case="3",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Заполянский р-н, с. Журавкино. "
            "Корпус: рождение 18.04.1908 (МК 1908 № 54), отец Букин Василий Степанович, мать Букина Анна "
            "Васильевна."
        ),
    ),
    wwii_record(
        person("Иван", "Степанович", "Булдыжов", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_kartoteka_memorial78900137/",
        reviewed=False,
        birth_date=EventDate(1914),
        casualty_reason="попал в плен (освобожден)",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        date=EventDate(1941, Month.JUNE, 29),
        casualty_date=EventDate(1941, Month.JUNE, 29),
        archive="ГА Республики Мордовия",
        comment=(
            "Сводная картотека «Мемориала». Место рождения на карточке: Мордовская АССР, Зубово-Полянский "
            "р-н, с. Журавкино. Корпус: рождение 19.02.1915 (МК 1915 № 19), отец Булдыжов Степан "
            "Михайлович, мать Булдыжова Евдокия Максимовна."
        ),
    ),
    wwii_record(
        person("Федор", "Васильевич", "Ермошин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/kld-card_ran73258187/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="268 гв. сп 90 гв. сд",
        document_type=WwiiDocumentType.WOUND_CARD,
        archive="Филиал ЦАМО (военно-медицинских документов)",
        fund="Картотека общего учета",
        archive_location="шкаф: Ермошичева Варвара - Ермилов Ник Алекс, ящик 074-27",
        comment=(
            "Документ без даты; файл 1941 г. — по другому документу того же человека. Госпиталь: ЭГ 1448. "
            "Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. Авдалово. Корпус: "
            "рождение 15.09.1907 (МК 1907 № 98), отец Ермошин Василий Иванович, мать Ермошина Агафья "
            "Максимовна."
        ),
    ),
    wwii_record(
        person("Федор", "Васильевич", "Ермошин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok8066781/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="172 сп 13 сд",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JULY, 4),
        date=EventDate(1941, Month.JULY, 4),
        archive="ЦАМО",
        fund="6560",
        inventory="62651с",
        case="8",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 15.09.1907 (МК 1907 № 98), отец Ермошин Василий Иванович, мать "
            "Ермошина Агафья Максимовна."
        ),
    ),
    wwii_record(
        person("Николай", "Иванович", "Калинкин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok2630817/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="1273 сп",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="7916",
        inventory="90930с",
        case="1",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 24.11.1907 (МК 1907 № 124), отец Калинкин Иван Михайлович, мать "
            "Калинкина Феодосия Тимофеевна."
        ),
    ),
    wwii_record(
        person("Иван", "Максимович", "Лескин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342263/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000406.jpg",
        birth_date=EventDate(1907),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 28),
        date=EventDate(1941, Month.AUGUST),
        casualty_date=EventDate(1941, Month.AUGUST),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список военнослужащих рядового и сержантского состава, семьи которых потеряли с "
            "ними связь в период ВОВ, по Зубово-Полянскому району Мордовской АССР (приложение к вх. № "
            "91495с), л. 406): Лескин Иван Максимович, красноармеец, стрелок, 1907 г.р., уроженец МАССР, "
            "Зубово-Полянского р-на, с. Авдалово. Призван Зубово-Полянским РВК МАССР 28.6.41 г. Можно "
            "считать пропавшим без вести в августе 1941 г.; на полях: «Проп. б/в 8/41». Родные: Жена "
            "Лескина Евдокия Агеевна, МАССР, Зубово-Пол. р-на, с. Авдалово. Место рождения на карточке: "
            "Мордовская АССР, Зубово-Полянский р-н, с. Авдалово. Корпус: рождение 24.06.1907 (МК 1907 № "
            "68), отец Лескин Максим Максимович, мать Лескина Акилина Архипповна."
        ),
    ),
    wwii_record(
        person("Иван", "Андреевич", "Митрошин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok6508347/",
        reviewed=False,
        birth_date=EventDate(1906),
        rank="красноармеец",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269841",
        case="1",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, "
            "Авдаловский с/с, д. Авдалово. Корпус: рождение 13.01.1906 (МК 1906 № 2), отец Митрошин "
            "Андрей Эрастович, мать Митрошина Прасковья Гаврииловна."
        ),
    ),
    wwii_record(
        person("Дмитрий", "Николаевич", "Мыськов", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_kartoteka_memorial80164503/",
        reviewed=False,
        birth_date=EventDate(1909),
        rank="рядовой",
        military_unit="12 А 2 див. 454 осб",
        casualty_reason="попал в плен (освобожден)",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        date=EventDate(1941, Month.OCTOBER, 12),
        casualty_date=EventDate(1941, Month.OCTOBER, 12),
        archive="РГВА",
        comment=(
            "Сводная картотека «Мемориала». Место рождения на карточке: Мордовская АССР, Зубово-Полянский "
            "р-н, д. Леон-Авдалово. Корпус: рождение 24.10.1909 (МК 1909 № 99), отец Мыськов Николай "
            "Прокопиевич, мать Мыськова Анастасия Феофановна."
        ),
    ),
    wwii_record(
        person("Егор", "Игнатьевич", "Нокин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok2893270/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="красноармеец",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269840",
        case="3",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубовский р-н, с. Журавкино. "
            "Корпус: рождение 29.03.1907 (МК 1907 № 39), отец Нокин Игнатий Максимович, мать Нокина "
            "Ксения Александровна."
        ),
    ),
    wwii_record(
        person("Герасим", "Федорович", "Пушкин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie1161462479/",
        reviewed=False,
        scan_file="scans/pamyat_11004022_00001121.jpg",
        birth_date=EventDate(1909),
        rank="рядовой",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        date=EventDate(1941, Month.OCTOBER),
        casualty_date=EventDate(1941, Month.OCTOBER),
        archive="ВК Московской обл.",
        fund="Отдел ВК по гг. Серпухов, Пущино, Протвино и Серпуховскому р-ну",
        case="11004022",
        comment=(
            "На скане (Извещение Управления по учету погибшего и пропавшего без вести рядового и "
            "сержантского состава МВС СССР (ф. № 4а), наш исх. № 12480-42729с, бланк ЦТ МВС СССР "
            "4346-46): «Известите гр. Пушкину ? 301 (адресат не читается), что военнослужащий рядовой "
            "Пушкин Герасим Федорович, уроженец с. Журавкино Зубовополянск. р-н, 1909 года рождения, "
            "находясь на фронте, пропал без вести в октябре 1941 г.». Родные: адресат извещения: "
            "Пушкин(а) ? (имя не читается). Место рождения на карточке: Мордовская АССР, Зубово-Полянский "
            "р-н, с. Журавкино. Корпус: рождение 04.03.1909 (МК 1909 № 25), отец Пушкин Федор Васильевич, "
            "мать Пушкина Прасковья Карповна."
        ),
    ),
    wwii_record(
        person("Герасим", "Федорович", "Пушкин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie62295786/",
        reviewed=False,
        scan_file="scans/pamyat_058-0977520-0479_00000180.jpg",
        birth_date=EventDate(1909),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_date=EventDate(1941, Month.JUNE, 22),
        date=EventDate(1941, Month.OCTOBER),
        casualty_date=EventDate(1941, Month.OCTOBER),
        archive="ЦАМО",
        fund="58",
        inventory="977520",
        case="479",
        comment=(
            "На скане (Список военнослужащих, пропавших без вести (лист 2; шапка — только номера граф "
            "1–13, заголовка и даты на кропе нет); последняя графа — «считать пропавшим без вести с …»; "
            "строка № 30): № 30 Пушкин Герасим Федорович, звание «-\"-» (кр-ц, как выше), 1909 г.р., "
            "уроженец с. Журавкино Зубополянский р.; призван Борским РВК 22.06.41г. «со слов(?)»; "
            "последнее письмо от 08.1941г. (помета «X-41»), г. Гомель; жена Пушкина, п. Шарапова-Охота; "
            "считать пропавшим без вести с 10.1941г. Родные: жена Пушкина (имя не указано), п. "
            "Шарапова-Охота. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Журавкино. Корпус: рождение 04.03.1909 (МК 1909 № 25), отец Пушкин Федор Васильевич, мать "
            "Пушкина Прасковья Карповна."
        ),
    ),
    wwii_record(
        person("Иван", "Иванович", "Пушкин", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok2893297/",
        reviewed=False,
        birth_date=EventDate(1906),
        rank="красноармеец",
        military_unit="106 омиб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE),
        date=EventDate(1941, Month.JUNE),
        archive="ЦАМО",
        fund="32552",
        inventory="269840",
        case="3",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубовский р-н, с. Журавкино. "
            "Корпус: рождение 01.10.1906 (МК 1906 № 78), отец Пушкин Иван Яковлевич, мать Пушкина "
            "Прасковья Игнатиевна."
        ),
    ),
    wwii_record(
        person("Прокопий", "Федорович", "Семкин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342274/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000407.jpg",
        birth_date=EventDate(1910),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 23),
        date=EventDate(1941, Month.SEPTEMBER),
        casualty_date=EventDate(1941, Month.SEPTEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список Зубово-Полянского РВК о пропавших без вести (дополнительное донесение), № "
            "строки 23; «шапка» — те же строки 23–28, без заголовков граф и даты): Семкин Прокопий "
            "Федорович, кр-ц, стрелок, 1910 г.р., уроженец МАССР Зуб.-Полянского р-на с. Авдалово; "
            "призван Зуб.-Полянским РВК МАССР ?.6(?).41; «можно считать пропавшим без вести в сентябре "
            "1941 г.»; помета «Проп. б/в 9/41». Родные: жена Семкина Екатерина Захаровна, МАССР, "
            "Зубово-Полянск. р-на, с. Авдалово. Место рождения на карточке: Мордовская АССР, "
            "Зубово-Полянский р-н, с. Авдалово. Корпус: рождение 07.07.1910 (МК 1910 № 46), отец Семкин "
            "Федор Павлович, мать Семкина Ефросиния Алексеевна."
        ),
    ),
    wwii_record(
        person("Федор", "Алексеевич", "Сенаторов", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok251575/",
        reviewed=False,
        birth_date=EventDate(1907),
        rank="мл. ком. состав",
        military_unit="в/ч 2940",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Кандалакшский РВК, Мурманская обл., Кандалакшский р-н",
        draft_date=EventDate(1941, Month.JULY),
        date=EventDate(1941, Month.JULY),
        archive="ЦАМО",
        fund="32881",
        inventory="194969",
        case="2",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 11.07.1907 (МК 1907 № 79), отец Сенаторов Алексей Феофанович, "
            "мать Сенаторова Акилина Петровна."
        ),
    ),
    wwii_record(
        person("Иван", "Матвеевич", "Сураев", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok14707580/",
        reviewed=False,
        birth_date=EventDate(1909),
        rank="красноармеец",
        military_unit="1174 сп",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.JUNE, 26),
        date=EventDate(1941, Month.JUNE, 26),
        archive="ЦАМО",
        fund="7833",
        inventory="254968с",
        case="3",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Журавкино. Корпус: рождение 22.02.1909 (МК 1909 № 20), отец Сураев Матвей Прокопиевич, мать "
            "Сураева Марфа Тимофеевна."
        ),
    ),
    wwii_record(
        person("Иван", "Матвеевич", "Сураев", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie61813135/",
        reviewed=False,
        scan_file="scans/pamyat_058-0977520-0601_00000183.jpg",
        birth_date=EventDate(1908),
        rank="рядовой",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.AUGUST, 23),
        date=EventDate(1941, Month.NOVEMBER),
        casualty_date=EventDate(1941, Month.NOVEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="977520",
        case="601",
        comment=(
            "Отчество на карточке — «Матвеич». На скане (Именной список военнослужащих рядового и "
            "сержантского состава, семьи которых потеряли с ними связь в период Великой Отечественной "
            "войны, по Зубово-Полянскому району Мордовской АССР; строка № 3 (даты списка на снимке нет; "
            "вх. № 44790-с)): Рядовой, стрелок, 1908 г.р.; уроженец Мордовской АССР, З.-Полянского р-на, "
            "с. Журавкино; призван Зубово-Полянским РВК Морд. АССР 2?.8.1941 г.; «Можно считать пропавшим "
            "б/вести в сентябре 1941 г.». Рядом рукописная пометка с датой «XI-41 г.» — читается не "
            "полностью. Родные: Жена Сураева Пелагея Мих., МАССР З.-Пол. р-н, с. Журавкино. Место "
            "рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. Журавкино. Корпус: рождение "
            "22.02.1909 (МК 1909 № 20), отец Сураев Матвей Прокопиевич, мать Сураева Марфа Тимофеевна."
        ),
    ),
    wwii_record(
        person("Илья", "Петрович", "Сураев", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok2062959/",
        reviewed=False,
        birth_date=EventDate(1906),
        rank="красноармеец",
        military_unit="167 ап 85 сд",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 26),
        date=EventDate(1941, Month.JUNE, 26),
        archive="ЦАМО",
        fund="10988",
        inventory="2",
        case="29",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Журавкино. Корпус: рождение 19.07.1906 (МК 1906 № 57), отец Сураев Петр Митрофанович, мать "
            "Сураева Елена Дмитриевна."
        ),
    ),
    wwii_record(
        person("Федор", "Петрович", "Сураев", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_kartoteka_memorial79893383/",
        reviewed=False,
        birth_date=EventDate(1901),
        rank="рядовой",
        military_unit="303 озб",
        casualty_reason="попал в плен (освобожден)",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        date=EventDate(1941, Month.OCTOBER, 7),
        casualty_date=EventDate(1941, Month.OCTOBER, 7),
        archive="РГВА",
        comment=(
            "Сводная картотека «Мемориала». Место рождения на карточке: Мордовская АССР, Зубово-Полянский "
            "р-н, с. Журавкино. Корпус: рождение 02.03.1903 (МК 1903 № 22), отец Сураев Петр "
            "Митрофанович, мать Сураева Елена Дмитриевна."
        ),
    ),
    wwii_record(
        person("Петр", "Петрович", "Тараканов", residence="Журавкино"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok11518804/",
        reviewed=False,
        birth_date=EventDate(1914),
        rank="мл. сержант",
        military_unit="28 ошисапб",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_date=EventDate(1941, Month.AUGUST, 30),
        date=EventDate(1941, Month.AUGUST, 30),
        archive="ЦАМО",
        fund="33417",
        inventory="146947с",
        case="11",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Журавкино. Корпус: рождение 08.10.1914 (МК 1914 № 108), отец Тараканов Петр Ильич, мать "
            "Тараканова Елена Федоровна."
        ),
    ),
    wwii_record(
        person("Кузьма", "Осипович", "Трушин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342276/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000407.jpg",
        birth_date=EventDate(1906),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 23),
        date=EventDate(1941, Month.SEPTEMBER),
        casualty_date=EventDate(1941, Month.SEPTEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список военнослужащих рядового и сержантского состава, семьи которых потеряли с "
            "ними связь в период ВОВ, по Зубово-Полянскому району МАССР (заголовок — на соседнем листе "
            "406, № 91495), лист 407, строка 25): Кр-ц, стрелок, 1906 г.р., МАССР, Зуб.-Полянского р-на, "
            "с. Авдалово; призван Зуб.-Полянским РВК МАССР ?6.6.41 года; можно считать пропавшим без "
            "вести в августе 1941 года; пометка «проп. б/в 9/41». Родные: Жена Трушина Анна Тимофеевна, "
            "МАССР, Зубово-Полянск. р-на, с. Авдалово. Место рождения на карточке: Мордовская АССР, "
            "Зубово-Полянский р-н, с. Авдалово. Корпус: рождение 28.10.1906 (МК 1906 № 89), отец Трушин "
            "Иосиф Иванович, мать Трушина Степанида Дмитриевна."
        ),
    ),
    wwii_record(
        person("Иван", "Матвеевич", "Филин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342256/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000406.jpg",
        birth_date=EventDate(1908),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.AUGUST, 8),
        date=EventDate(1941, Month.SEPTEMBER),
        casualty_date=EventDate(1941, Month.SEPTEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список в/служащих рядового и сержантского состава, семьи которых потеряли с ними "
            "связь в период ВОВ, по Зубово-Полянскому району Мордовской АССР (приложение к вх. № 91495), "
            "строка 5): Красноармеец, стрелок, 1908 г.р., уроженец МАССР, Зуб.-Полянского р-на, с. "
            "Авдалово; призван Зуб.-Полянским РВК МАССР 8.8.41 г. Можно считать пропавшим без вести в "
            "августе 1941 года (на полях: 9/41). Родные: Жена Филина Ксения Федоровна, МАССР, Зуб.-Пол. "
            "р-на, с. Авдалово. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 20.08.1907 (МК 1907 № 94), отец Филин Матвей Иродионович, мать "
            "Филина Пелагея Васильевна."
        ),
    ),
    wwii_record(
        person("Иван", "Ефимович", "Филин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342301/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000408.jpg",
        birth_date=EventDate(1907),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 30),
        date=EventDate(1941, Month.SEPTEMBER),
        casualty_date=EventDate(1941, Month.SEPTEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список военнослужащих рядового и сержантского состава, семьи которых потеряли с "
            "ними связь в период ВОВ, по Зубово-Полянскому РВК МАССР (приложение к вх. № 91495), строка "
            "5): Красноармеец, стрелок, 1907 г.р., уроженец МАССР, Зуб.-Полянского р-на, с. Авдалово; "
            "призван Зуб.-Полянским РВК МАССР 30(?).6.41 г. Можно считать пропавшим без вести в сентябре "
            "1941 г. (на полях: 9/41). Родные: Жена Филина Мария Тимофеевна, МАССР, Зубово-Полянск. р-на, "
            "с. Авдалово. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. Авдалово. "
            "Корпус: рождение 22.08.1909 (МК 1909 № 74), отец Филин Ефим Герасимович, мать Филина "
            "Анастасия Ивановна."
        ),
    ),
    wwii_record(
        person("Петр", "Николаевич", "Филин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/isp-chelovek_spisok1299839/",
        reviewed=False,
        birth_date=EventDate(1908),
        rank="рядовой",
        military_unit="996 сп 286 сд",
        document_type=WwiiDocumentType.UNIT_ROSTER,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 22),
        date=EventDate(1941, Month.JUNE, 22),
        archive="ЦАМО",
        fund="7656",
        inventory="70087",
        case="4",
        comment=(
            "Дата — призыва. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 16.05.1908 (МК 1908 № 60), отец Филин Николай Герасимович, мать "
            "Филина Анисья Степановна."
        ),
    ),
    wwii_record(
        person("Федор", "Васильевич", "Филин", residence="Авдалово"),
        source_url="https://pamyat-naroda.ru/heroes/memorial-chelovek_dopolnitelnoe_donesenie58342302/",
        reviewed=False,
        scan_file="scans/pamyat_058-0018004-0601_00000408.jpg",
        birth_date=EventDate(1909),
        rank="красноармеец",
        casualty_reason="пропал без вести",
        document_type=WwiiDocumentType.CASUALTY_CLARIFICATION,
        draft_board="Зубово-Полянский РВК, Мордовская АССР, Зубово-Полянский р-н",
        draft_date=EventDate(1941, Month.JUNE, 30),
        date=EventDate(1941, Month.SEPTEMBER),
        casualty_date=EventDate(1941, Month.SEPTEMBER),
        archive="ЦАМО",
        fund="58",
        inventory="18004",
        case="601",
        comment=(
            "На скане (Список военнослужащих рядового и сержантского состава, семьи которых потеряли с "
            "ними связь в период ВОВ, по Зубово-Полянскому РВК МАССР (приложение к вх. № 91495), строка "
            "6): Красноармеец, стрелок, 1909 г.р., уроженец МАССР, Зуб.-Полянск. р-на, село Авдалово; "
            "призван Зуб.-Полянским РВК МАССР 30.6.41 года. Можно считать пропавшим без вести в сентябре "
            "1941 г. (на полях: 9/41). Родные: Жена Филина Мария Семеновна, МАССР, Зубово-Полянского "
            "р-на, с. Авдалово. Место рождения на карточке: Мордовская АССР, Зубово-Полянский р-н, с. "
            "Авдалово. Корпус: рождение 15.02.1910 (МК 1910 № 9), отец Филин Василий Герасимович, мать "
            "Филина Елена Иосифовна."
        ),
    ),
)
