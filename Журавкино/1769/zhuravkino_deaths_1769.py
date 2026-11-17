from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import (PEASANT_MAIDEN, PEASANT_MALE, YASAK_PEASANT_FEMALE,
                                   YASAK_PEASANT_MALE)

avdalovo_deaths_1769 = death_records(
    "ГАРО", "627", "255", "10", "Авдалово", "Николая Чудотворца",
    1769,
    *page("?",
          *death_month(Month.MARCH,
                       death(1, Gender.FEMALE, 16, None,
                             deceased=person("Марфа", "Гаврилова", status=PEASANT_MAIDEN)),
                       ),
          *death_month(Month.NOVEMBER,
                       death(2, Gender.MALE, 20, None,
                             deceased=person("Алексей", "Кондратьев", status=PEASANT_MALE), age=5),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
