from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1813 = marriage_records(
    "ЦГАРМ", "57", "6", "80", "Журавкино", "Николаевская",
    1813,
    *page("?",
          *marriage_month(Month.JANUARY,
                          marriage(1, 12,
                                   groom=person("Василий", status=YASAK_PEASANT_BOY),
                                   bride=person("Екатерина", "Иванова", residence="Пичевка")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
