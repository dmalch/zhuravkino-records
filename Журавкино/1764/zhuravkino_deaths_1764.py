from verso.ru.dsl import (Gender, Month, RecordDefaults, death, death_month, death_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE, YASAK_PEASANT_WIDOW

avdalovo_deaths_1764 = death_records(
    "ГАРО", "627", "255", "3", "Авдалово", "Николая Чудотворца",
    1764,
    *page("?",
          *death_month(Month.JANUARY,
                       death(1, Gender.MALE, 10, None,
                             deceased=person("Корнилий", "Евстафиев", residence="Журавкино"), age=90),
                       ),
          *death_month(Month.MARCH,
                       death(2, Gender.FEMALE, 20, None,
                             deceased=person("Марья", "Иванова", residence="Журавкино", status=YASAK_PEASANT_WIDOW)),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
