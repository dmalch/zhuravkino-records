from corpus.statuses import (SLEPTSOV_AI_PEASANT_FEMALE, SLEPTSOV_AI_PEASANT_GIRL,
                             SLEPTSOV_AI_PEASANT_MALE)
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1824 = marriage_records(
    "ЦГАРМ", "57", "6", "114", "Журавкино", "Николая Чудотворца",
    1824,
    *page("64",
          *marriage_month(Month.APRIL,
                          marriage(1, 13,
                                   groom=person("Федор", "Матвеев", status=YASAK_PEASANT_BOY),
                                   bride=person("Марья", "Прокопиева"),
                                   witness1=person("Егор", "Иванов"),
                                   witness2=person("Ияков", "Никитин"),
                                   witness4=person("Мавра", "Фокина")),
                          ),
          *marriage_month(Month.SEPTEMBER,
                          marriage(2, 8,
                                   groom=person("Петр", "Спиридонов", status=SLEPTSOV_AI_PEASANT_MALE), groom_marriage_num=2,
                                   bride=person("Федосья", "Сергеева", status=SLEPTSOV_AI_PEASANT_GIRL),
                                   witness1=person("Тит", "Константинов", status=SLEPTSOV_AI_PEASANT_MALE),
                                   witness2=person("Матвей", "Тимофеев", status=SLEPTSOV_AI_PEASANT_MALE),
                                   witness4=person("Параскева", "Григорьева", status=SLEPTSOV_AI_PEASANT_FEMALE)),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
