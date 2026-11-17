from corpus.statuses import SLEPTSOV_TI_PEASANT_FEMALE, SLEPTSOV_TI_PEASANT_MALE
from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_deaths_1766 = death_records(
    "ГАРО", "627", "255", "6", "Авдалово", "Николая Чудотворца",
    1766,
    *page("?",
          *death_month(Month.JANUARY,
                       death(1, Gender.MALE, 16, None,
                             deceased=person("Лорионъ", "Васильевъ", status=SLEPTSOV_TI_PEASANT_MALE), age=100),
                       ),
          *death_month(Month.APRIL,
                       death(2, Gender.MALE, 10, None,
                             deceased=person("Филипъ", "Стефановъ", status=SLEPTSOV_TI_PEASANT_MALE), age=5),
                       ),
          *death_month(Month.NOVEMBER,
                       death(3, Gender.FEMALE, 6, None,
                             deceased=person("Марфа", "Никитина", status=SLEPTSOV_TI_PEASANT_FEMALE)),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
