from corpus.statuses import SLEPTSOV_GM_PEASANT_BOY, SLEPTSOV_GM_PEASANT_GIRL
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import (YASAK_PEASANT_BOY, YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL,
                                   YASAK_PEASANT_MALE)

zhuravkino_marriages_1814 = marriage_records(
    "ЦГАРМ", "57", "1", "393", "Журавкино", "Николаевская",
    1814,
    *page("?",
          *marriage_month(Month.JULY,
                          marriage(1, 25,
                                   groom=person("Иван", "Иванов", status=YASAK_PEASANT_BOY),
                                   bride=person("Марфа", "Денисова", residence="Анаево")),
                          marriage(2, 28,
                                   groom=person("Митрий", "Гаврилов", status=YASAK_PEASANT_BOY),
                                   bride=person("Катерина", "Петрова", residence="Каргашино")),
                          ),
          *marriage_month(Month.NOVEMBER,
                          marriage(3, 1,
                                   groom=person("Савелий", "Егоров", status=SLEPTSOV_GM_PEASANT_BOY),
                                   bride=person("Дарья", "Борисова", status=SLEPTSOV_GM_PEASANT_GIRL)),
                          marriage(4, 1,
                                   groom=person("Иван", "Архипов", status=SLEPTSOV_GM_PEASANT_BOY),
                                   bride=person("Аграфена", "Семенова", status=SLEPTSOV_GM_PEASANT_GIRL)),
                          marriage(5, 4,
                                   groom=person("Афанасий", "Степанов", status=YASAK_PEASANT_BOY),
                                   bride=person("Пелагея", "Давыдова", residence="Анаево")),
                          marriage(6, 8,
                                   groom=person("Матфей", "Васильев", status=YASAK_PEASANT_BOY),
                                   bride=person("Ирина", "Алексеева", residence="Каргашино")),
                          marriage(7, 10,
                                   groom=person("Ефим", "Нестеров", status=YASAK_PEASANT_BOY),
                                   bride=person("Агафья", "Акимова", residence="Каргашино")),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
