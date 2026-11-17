from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_MALE, YASAK_PEASANT_SON

avdalovo_deaths_1754 = death_records(
    "ГАТО", "1049", "12", "4", "Авдалово", "Николая Чудотворца",
    1754,
    *page("87об",
          *death_month(Month.SEPTEMBER,
                       death(1, Gender.MALE, None, None,
                             deceased=person("Алексей", residence="Журавкино", status=YASAK_PEASANT_SON), age=3,
                             relatives=[relative(person("Иван" ), Relationship.FATHER)]),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Авдалово",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
    ),
)
