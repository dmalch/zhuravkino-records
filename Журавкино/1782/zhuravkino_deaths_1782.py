from corpus.statuses import SLEPTSOV_GM_PEASANT_FEMALE
from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_deaths_1782 = death_records(
    "ГАРО", "627", "298", "12", "Авдалово", "Николая Чудотворца",
    1782,
    *page("29",
          *death_month(Month.APRIL,
                       death(1, Gender.FEMALE, 23, None,
                             deceased=person("Марфа", "Егорова", residence="Журавкино", status=SLEPTSOV_GM_PEASANT_FEMALE), age=40),
                       ),
          *death_month(Month.JULY,
                       death(2, Gender.FEMALE, 13, None,
                             deceased=person("Марфа", "Лазарева", residence="Журавкино"), age=72,
                             source_age_error="«72» при 30 годах в РС 1762 и 49 в 1782 по РС 1795 (двор 44) — "
                                              "возраст завышен. Тождество держит состав двора: у Никифора Келгаева "
                                              "от второй жены Софьи дочь Прасковья р. ок. 1783, Марфе было бы 50 — "
                                              "значит, к 1782–83 она умерла, а «умре въ 1787» в РС 1795 — ошибка сказки."),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
