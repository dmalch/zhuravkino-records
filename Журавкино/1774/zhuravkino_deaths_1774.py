from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE

avdalovo_deaths_1774 = death_records(
    "ГАРО", "627", "255", "18", "Авдалово", "Николая Чудотворца",
    1774,
    *page("28",
          *death_month(Month.SEPTEMBER,
                       death(1, Gender.MALE, 4, None,
                             deceased=person("Яков", "Савинов", residence="Журавкино"), age=52),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
