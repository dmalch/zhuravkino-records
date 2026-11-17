from corpus.statuses import (SLEPTSOV_EF_PEASANT_GIRL, SLEPTSOV_GM_PEASANT_BOY,
                             SLEPTSOV_GM_PEASANT_GIRL)
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1807 = marriage_records(
    "ЦГАРМ", "57", "6", "63", "Журавкино", "Николаевская",
    1807,
    *page("?",
          *marriage_month(None,
                          marriage(3, None,
                                   groom=person("Алексей", "Иванов", residence="Авдалово", status="отрок из крестьян помещицы Екатерины Фирсовны Слепцовой"),
                                   bride=person("Евдокия", "Васильева", residence="Авдалово", status=SLEPTSOV_EF_PEASANT_GIRL)),
                          marriage(4, None,
                                   groom=person("Стефан", "Иванов", status=YASAK_PEASANT_BOY),
                                   bride=person("Евдокия", "Агафонова")),
                          ),
          *marriage_month(Month.JANUARY,
                          marriage(1, 26,
                                   groom=person("Федор", "Александров", residence="Авдалово", status="отрок из крестьян помещицы Марии Ивановны Енгалычевой", comment="статус исправлен: в подлиннике — «полсела Авдалова госпожи Анны Ивановны Кугушевой» (скан л. 231 сверен 25.09.2026); по ревизиям 1811 (ГАТО 12-1-434), 1816 и 1834 — крестьянин Енгалычевых, как и брат Антон в МК 1801 и 1806"),
                                   bride=person("Анна", residence="Чермные", status="девка из крестьян помещицы Анны Ивановны Кугушевой", comment="отчество не видно из-за повреждения страницы")),
                          ),
          *marriage_month(Month.FEBRUARY,
                          marriage(2, 7,
                                   groom=person("Петр", "Романов", status=SLEPTSOV_GM_PEASANT_BOY),
                                   bride=person("?", "Иванова", status=SLEPTSOV_GM_PEASANT_GIRL, comment="имя и населенный пункт не видно из-за повреждения страницы")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
