from corpus.statuses import SLEPTSOV_GM_PEASANT_GIRL, SLEPTSOV_GM_PEASANT_MALE
from verso.ru.dsl import (Month, RecordDefaults, marriage, marriage_month, marriage_records, page,
                          person)
from verso.ru.dsl.statuses import YASAK_PEASANT_FEMALE, YASAK_PEASANT_GIRL, YASAK_PEASANT_MALE

zhuravkino_marriages_1799 = marriage_records(
    "ГАТО", "1049", "10", "85", "Журавкино", "Николая Чудотворца",
    1799,
    *page("34",
          *marriage_month(Month.JANUARY,
                          marriage(1, 9,
                                   groom=person("Иосиф", "Титов", status=SLEPTSOV_GM_PEASANT_MALE), groom_age=16, groom_marriage_num=1,
                                   bride=person("Матрена", "Феодотова", status=SLEPTSOV_GM_PEASANT_GIRL), bride_age=15),
                          marriage(2, 16,
                                   groom=person("Иван", "Константинов"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Ефросинья", "Михайлова"), bride_age=17),
                          ),
          *marriage_month(Month.NOVEMBER,
                          marriage(3, 1,
                                   groom=person("Василий", "Иванов"), groom_age=17, groom_marriage_num=1,
                                   bride=person("Елена", "Устинова"), bride_age=16),
                          marriage(4, 8,
                                   groom=person("Ксенофонт", "Васильев"), groom_age=28, groom_marriage_num=1,
                                   bride=person("Анна", "Андреева"), bride_age=20),
                          ),
          ),
    defaults=RecordDefaults(
        residence="Журавкино",
        status_male=YASAK_PEASANT_MALE,
        status_female=YASAK_PEASANT_FEMALE,
        status_bride=YASAK_PEASANT_GIRL
    ),
)
