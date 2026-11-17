from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_deaths_1760 = death_records(
    "ГАРО", "627", "255", "2", "Авдалово", "Николая Чудотворца",
    1760,
    *page("?",
          *death_month(Month.MARCH,
                       death(1, Gender.MALE, 5, None,
                             deceased=person("Ефим", "Михайлов", residence="Журавкино"), age=33),
                       ),
          *death_month(Month.APRIL,
                       death(2, Gender.MALE, 3, None,
                             deceased=person("Артем", "Казмин", residence="Журавкино"), age=50),
                       death(3, Gender.FEMALE, 6, None,
                             deceased=person("Матрона", "Петрова", residence="Журавкино")),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
