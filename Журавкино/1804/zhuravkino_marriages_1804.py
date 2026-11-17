from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1804 = marriage_records(
    "ЦГАРМ", "57", "1", "389а", "Журавкино", "Николаевская",
    1804,
    *page("?",
          *marriage_month(Month.JANUARY,
                          marriage(1, 8,
                                   groom=person("Игнат", "Климов", status=YASAK_PEASANT_BOY),
                                   bride=person("Анна", "Петрова", residence="Анаево")),
                          ),
          *marriage_month(Month.FEBRUARY,
                          marriage(2, 28,
                                   groom=person("Михаил", "Казмин", status=YASAK_PEASANT_BOY),
                                   bride=person("Василиса", "Петрова", residence="Вадовские Селищи")),
                          marriage(3, 29,
                                   groom=person("Иван", "Савельев", status=YASAK_PEASANT_BOY),
                                   bride=person("Устина", "Стефанова", residence="Каргашино")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
